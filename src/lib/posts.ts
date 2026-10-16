// 글 파일(src/posts/*.md)을 읽어 오는 도우미.
// 글을 추가하려면 이 폴더에 .md 파일 하나만 넣으면 됩니다.

export interface PostMeta {
  title: string;
  description?: string;
  date: string;
  tags?: string[];
  category?: string;
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

// 카테고리: 글 파일 맨 위에 category: "prep" 처럼 키만 적으면 자동으로 분류됩니다.
export interface Category {
  key: string;
  name: string;
  icon: string;
  desc: string;
}

export const CATEGORIES: Category[] = [
  { key: 'prep', name: '출발 전 준비', icon: '🧳', desc: '보험, 학교, 입국 서류, 통신처럼 떠나기 전에 정리한 것들' },
  { key: 'stay', name: '숙소·생활', icon: '🏠', desc: '숙소 고르기와 한 달 살아본 기록, 실제 비용' },
  { key: 'tour', name: '체험·투어', icon: '🗺️', desc: '아이와 다녀온 투어와 하루 코스, 실제 비용과 팁' },
];

export function getCategory(key?: string): Category | undefined {
  return CATEGORIES.find((c) => c.key === key);
}

export function getPostsByCategory(key: string): Post[] {
  return getPosts().filter((p) => p.meta.category === key);
}
