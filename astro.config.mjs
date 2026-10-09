import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

// 사이트 주소. 도메인이 바뀌면 여기만 고치면 됩니다.
export default defineConfig({
  site: 'https://suwoodays.com',
  integrations: [sitemap()],
});
