# ShallWePuzzle Privacy Policy

앱의 11개 지원 언어로 제공하는 전체 개인정보처리방침. 앱: **ShallWePuzzle**, Android 패키지:
`kr.shall.we.puzzle`. 문의: **dydxo116@gmail.com**.

- 편집 원본: `policy.json`
- 빌드: `python3 build.py` (추가 패키지 불필요)
- 공개 파일: `index.html`, 각 언어 디렉터리의 `index.html`, `privacy.css`,
  `.nojekyll`
- 페이지는 로그인, 광고, 방문 분석 코드, 외부 폰트 또는 JavaScript 없이
  열립니다. GitHub 자체의 보안 접속 기록은 정책에 별도로 설명합니다.

## 무료 GitHub Pages 게시

1. GitHub에 **Public** 저장소 `dydxo116/dydxo116.github.io (shallwepuzzle-privacy/ 폴더)`를 만듭니다.
   앱 소스 저장소의 공개 여부는 변경하지 않습니다.
2. 이 저장소의 파일을 `main` 브랜치로 푸시합니다.
3. 저장소 **Settings → Pages → Build and deployment**에서
   **Deploy from a branch → main → /(root) → Save**를 선택합니다.
4. Pages 배포가 완료되면 아래 URL이 실제로 열리는지 로그인하지 않은
   브라우저에서 확인합니다. 게시 전에는 이 URL을 출시 정보에 등록하지 않습니다.

공개 URL:

- 한국어: `https://dydxo116.github.io/shallwepuzzle-privacy/`
- English: `https://dydxo116.github.io/shallwepuzzle-privacy/en/`

Google Play Console의 개인정보처리방침 필드와 앱 내 정책 링크에 최종 공개
URL을 사용합니다. 데이터 보안 설문은 앱과 포함 SDK의 실제 설정에 맞게 별도로
작성해야 합니다.

## 업데이트

`policy.json`의 11개 언어와 시행일을 함께 수정하고 `python3 build.py`를 실행한
뒤 생성된 HTML 파일도 커밋합니다. Pages는 `main` 변경을 자동으로 게시합니다.

## 공식 근거

- Google Play 사용자 데이터 정책:
  https://support.google.com/googleplay/android-developer/answer/10144311
- Google Mobile Ads 데이터 공개:
  https://developers.google.com/admob/android/privacy/play-data-disclosure
- Firebase 개인정보 처리 및 Crashlytics 보관:
  https://firebase.google.com/support/privacy
- GA4 데이터 보관:
  https://support.google.com/analytics/answer/7667196
- GitHub Pages 공개 조건과 접속 기록:
  https://docs.github.com/en/pages/getting-started-with-github-pages/about-github-pages

공식 문서 대조일: 2026-10-21.

지원 언어: 한국어, 영어, 일본어, 독일어, 프랑스어, 스페인어, 브라질 포르투갈어,
번체 중국어, 인도네시아어, 태국어, 베트남어. 한국어는 루트, 다른 언어는
`/en/`, `/ja/`, `/de/`, `/fr/`, `/es/`, `/pt-BR/`, `/zh-Hant/`, `/id/`, `/th/`, `/vi/`입니다.
각 페이지의 언어 링크로 전환할 수 있습니다. 기존 한국어·영어 주소는 유지합니다.

앱 오프라인 원본 `assets/privacy/policy.json`에는 이 저장소의 `policy.json`을 그대로
복사합니다. 버전 0.31.29는 번역·즉시 언어 변경 개선이며, 데이터 처리 방식의 적용
시점은 기존과 같이 0.31.28부터입니다. 번역은 법적 승인이나 인증을 의미하지 않습니다.

검증: `python3 -m unittest test_build.py`. 11개 페이지의 전체 조항, 언어 전환,
상대 경로, 문의처와 공식 출처를 검사합니다.
