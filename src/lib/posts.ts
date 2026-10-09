// 글 파일(src/posts/*.md)을 읽어 오는 도우미.
// 글을 추가하려면 이 폴더에 .md 파일 하나만 넣으면 됩니다.

export interface PostMeta {
  title: string;
  description?: string;
  date: string;
  tags?: string[];
  draft?: boolean;
}

export interface Post {
  slug: string;
  meta: PostMeta;
  Content: any;
}

export function getPosts(): Post[] {
  const files = import.meta.glob('/src/posts/*.md', { eager: true }) as Record<
    string,
    { frontmatter: PostMeta; Content: any }
  >;

  return Object.entries(files)
    .map(([path, mod]) => ({
      slug: path.split('/').pop()!.replace(/\.md$/, ''),
      meta: mod.frontmatter,
      Content: mod.Content,
    }))
    .filter((post) => !post.meta.draft)
    .sort((a, b) => new Date(b.meta.date).getTime() - new Date(a.meta.date).getTime());
}

export function formatDate(date: string): string {
  const d = new Date(date);
  return `${d.getFullYear()}.${String(d.getMonth() + 1).padStart(2, '0')}.${String(d.getDate()).padStart(2, '0')}`;
}
