// 검색용 목록(제목, 설명, 태그, 본문 글자)을 빌드 때 만들어 두는 파일입니다.
import { getPosts, getCategory } from '../lib/posts';

const raws = import.meta.glob('/src/posts/*.md', { query: '?raw', import: 'default', eager: true }) as Record<string, string>;

function plain(md: string): string {
  return md
    .replace(/^---[\s\S]*?---/, '')
    .replace(/```[\s\S]*?```/g, ' ')
    .replace(/!\[[^\]]*\]\([^)]*\)/g, ' ')
    .replace(/\[([^\]]*)\]\([^)]*\)/g, '$1')
    .replace(/[#>*_`|]/g, ' ')
    .replace(/-{3,}/g, ' ')
    .replace(/\\(.)/g, '$1')
    .replace(/\s+/g, ' ')
    .trim();
}

export function GET() {
  const posts = getPosts().map((p) => {
    const raw = raws[`/src/posts/${p.slug}.md`] ?? '';
    return {
      slug: p.slug,
      title: p.meta.title,
      description: p.meta.description ?? '',
      tags: p.meta.tags ?? [],
      category: getCategory(p.meta.category)?.name ?? '',
      date: p.meta.date,
      text: plain(raw),
    };
  });
  return new Response(JSON.stringify(posts), { headers: { 'Content-Type': 'application/json; charset=utf-8' } });
}
