# create-svelte

## 개발하기

- Node.js 18 이후 버전 설치

### Corepack 및 pnpm 설치

```bash
corepack enable
corepack prepare pnpm@latest --activate
```

### 프로젝트 의존성 설치

```
// front 디렉토리로 이동 후
pnpm i
```

### 개발모드 실행

```bash
pnpm run dev
pnpm run dev -- --open
```

## 빌드

```bash
npm run build
```

`npm run preview`으로 빌드된 버전의 미리보기 가능

> To deploy your app, you may need to install an [adapter](https://kit.svelte.dev/docs/adapters) for your target
> environment.
