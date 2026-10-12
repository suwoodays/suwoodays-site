# SUWOODAYS 사이트 (초보자용 안내)

가족 장기여행 노트 사이트의 뼈대입니다. 빌드까지 확인을 마쳤고, 홈 · 글 목록 · 글 상세 · 소개 페이지와 샘플 글 1개가 들어 있어요.

## 폴더 구조 (글 쓸 때 건드리는 곳만 굵게)

```
suwoodays/
├─ src/
│  ├─ posts/          ← **글은 여기에 .md 파일로 추가**
│  ├─ pages/          ← 홈(index), 소개(about), 글 목록/상세
│  ├─ layouts/Base.astro   ← 상단 메뉴, 하단 문구, 검색용 정보
│  └─ styles/global.css    ← 색상과 글꼴
├─ public/            ← 아이콘(favicon), robots.txt
└─ astro.config.mjs   ← 사이트 주소(suwoodays.com)
```

## 글 한 편 추가하는 법

1. `src/posts/` 폴더에 새 파일을 만듭니다. 파일 이름이 주소가 됩니다. (예: `vietnam-budget.md` → `suwoodays.com/blog/vietnam-budget/`)
2. 파일 맨 위에 아래 형식을 적고, 그 아래에 글을 씁니다.

```
---
title: "베트남 한 달 살기 비용 정리"
description: "검색 결과에 보이는 한두 줄 설명"
date: 2026-10-20
tags: ["비용", "베트남"]
draft: false
---

본문은 여기부터 씁니다.
```

- `draft: true`로 두면 사이트에 나타나지 않는 임시 저장 상태가 됩니다.
- 영문 소문자와 하이픈으로 파일 이름을 지으면 주소가 깔끔해요.
- `src/posts/sample-checklist.md`는 샘플이니 실제 글을 올리기 전에 지우세요.

## 내 컴퓨터에서 미리 보기 (선택)

Node.js(18 이상)가 설치되어 있을 때:

```
npm install
npm run dev
```

브라우저에서 `http://localhost:4321`을 열면 됩니다. 어렵다면 이 단계는 건너뛰고 바로 아래 배포로 가도 돼요.

## 인터넷에 올리기 (처음 한 번)

1. **GitHub 가입** 후 새 저장소(repository)를 만들고, 이 폴더의 파일을 올립니다. (GitHub 웹 화면의 "uploading an existing file"로 끌어다 놓아도 됩니다. `node_modules`와 `dist` 폴더는 올리지 마세요.)
2. **Vercel 가입** (GitHub 계정으로 로그인) → "Add New Project" → 방금 만든 저장소 선택 → Deploy. 설정은 기본값 그대로 두면 됩니다.
3. 1~2분 뒤 `xxxx.vercel.app` 주소로 사이트가 열립니다.
4. **도메인 연결**: Vercel 프로젝트의 Settings → Domains에 `suwoodays.com`을 입력하면 연결 방법(DNS 설정값)이 표시됩니다. 도메인 구입처(가비아 등)의 DNS 설정 화면에 그 값을 그대로 입력하세요.
5. 이후에는 글 파일을 GitHub에 올릴 때마다 사이트가 자동으로 갱신됩니다.

## 올린 뒤 해야 할 일

- **Google Search Console**에 `suwoodays.com`을 등록하고, 사이트맵 주소 `https://suwoodays.com/sitemap-index.xml`을 제출하세요. 검색에 노출되기 시작하는 첫걸음입니다.
- `astro.config.mjs`의 `site` 주소가 실제 도메인과 같은지 확인하세요.
- `src/pages/about.astro`의 문의 항목에 이메일 등 연락 방법을 채우세요.

## 막히면

오류 화면이나 메시지를 캡처해서 채팅에 붙여 주세요. 원인과 해결 방법을 알려 드립니다.
네이버 소유확인 반영
