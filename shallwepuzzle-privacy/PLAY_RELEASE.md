# ShallWePuzzle 출시 순서 — 0.31.29

2026-10-21 공식 안내 대조. 앱 패키지: `kr.shall.we.puzzle`.

## 준비된 항목

- 개인정보처리방침: <https://dydxo116.github.io/shallwepuzzle-privacy/>.
  앱과 웹에 19개 언어 전체 조항을 제공한다. 앱 0.31.29부터 언어 변경 즉시 반영한다.
- 전 연령 보호: 나이 입력 전 SDK 보류, 18세 미만·입력 생략 시 보호 처리,
  해당 사용자의 광고 ID 전송 방지, 성인 분석·오류진단은 기본 미동의인 선택 항목.
- 기존 Console의 정책 URL, 광고 포함, 광고 ID 사용/목적, 전 연령 대상 선택은 확인했다.
- keystore를 GitHub Secrets에 등록했다. 아래 AAB는 업로드 키를 사용하고,
  별도 APK는 기존 테스트 서명과 Google 테스트 광고를 사용한다.

## 1. Play Console 데이터 보안 설문 저장

현재 **저장 완료를 확인하지 못한 항목**이다. TinyFish는 이 콘솔의 로컬 CSV
파일 선택기를 지원하지 않아 사용자가 직접 업로드해야 한다. 다시 로그인할 문제는 아니다.

1. [준비한 CSV 다운로드](https://dydxo116.github.io/shallwepuzzle-privacy/play-data-safety-v0.31.29.csv).
   0.31.29용 수정 파일에는 계정 생성 미지원·외부 계정 로그인 미지원·삭제 요청 URL 응답도 포함했다.
   기존 파일의 필수 계정 질문 누락 오류를 보완했다.
2. Play Console → 앱 콘텐츠 → 데이터 보안 → CSV 가져오기로 업로드한다.
   가져오기는 기존 답변을 바꿀 수 있으므로 **미리보기에서 실제 답을 확인**한다.
3. 데이터 수집/공유 **예**, 전송 중 암호화 **예**를 확인한다.
4. 계정 생성 **허용하지 않음**, 외부 계정 로그인 **아니요**를 확인한다.
5. 삭제 요청 안내 URL은 <https://dydxo116.github.io/shallwepuzzle-privacy/#rights>.
6. 대략적 위치, 앱 상호작용, 비정상 종료 로그, 진단, 기기/기타 ID를 확인한다.
   비정상 종료 로그는 **선택적 수집**이고, 서비스 제공자 예외를 적용해 수집만 공개한다.
   나머지 네 유형은 광고 SDK를 포함한 전체 처리를 반영해 수집/공유로 준비했다.
7. 독립 보안 심사나 Families 약속 배지를 검증 없이 선택하지 않는다.
8. 제출 전 미리보기 → 저장을 누르고, 화면을 다시 열어 저장값을 확인한다.

상세 근거와 질문별 설명은 [PLAY_DATA_SAFETY.md](PLAY_DATA_SAFETY.md).

## 2. 스토어 등록정보와 배포 설정

- 앱 이름 ShallWePuzzle, 지원 이메일 `mozzink.support@gmail.com`, 개인정보처리방침 URL을 확인한다.
- 앱 아이콘, 실제 최신 화면의 스크린샷, 소개/짧은 설명, 지원 언어를 등록한다.
- 콘텐츠 등급 설문은 실제 게임/광고 내용과 맞는지 최종 확인한다.
- 출시 국가/지역, 무료 앱 여부와 Console의 개발자 계정 확인 등 남은 필수 항목을 완료한다.
  계정 유형·생성일과 스토어 자료의 완료 여부는 이번 코드 작업에서 확인하지 않았다.

## 3. 업로드 키로 서명한 AAB를 테스트 트랙에 업로드

- [Play 업로드용 AAB](https://github.com/bmoh95/puzzle-hub-flutter/releases/download/play-v0.31.29/ShallWePuzzle-v0.31.29.aab)
- [기기 직접 설치용 테스트 APK](https://github.com/bmoh95/puzzle-hub-flutter/releases/download/v0.31.29/PuzzleHubFlutter-v0.31.29-arm64.apk)

AAB 링크는 해당 GitHub Actions가 성공해 Release가 게시된 뒤 유효하다.
Play Console에는 **AAB**를 올린다. APK는 직접 설치 확인용이다.
처음에는 내부 테스트 트랙에서 Play 앱 서명 안내를 완료하고 AAB를 업로드한다.
정상 실행, 연령 선택/생략, 언어 즉시 변경, 게임 진행을 실제 배포 경로로 확인한다.

현재 직접 설치 APK와 Play 배포본은 서명이 다르다. 기존 앱 위에 Play 설치가
안 될 수 있으며, 기존 앱 삭제 시 로컬 진행 기록도 없어질 수 있으므로 설치 전에 주의한다.

## 4. AdMob 운영 설정

코드의 UMP 적용과 **계정에서 동의 메시지를 게시하는 작업은 별개**다.
이 계정의 메시지 게시/광고 게재 승인 상태는 아직 확인하지 않았다.

- AdMob → 개인정보 보호 및 메시지: 적용 지역의 동의/개인정보 메시지를 설정하고 게시한다.
- Google Play 등록정보가 연결 가능한 상태가 되면 AdMob 앱을 해당 스토어 앱과 연결한다.
- 개발자 웹사이트와 `app-ads.txt`를 설정하고, AdMob이 요구하는 앱 인증 및 준비 상태
  검토를 완료한다. 새 앱은 인증·검토 승인이 끝나기 전에는 광고를 완전히 게재할 수 없다.
- 인증에 쓸 파일은 AdMob **app-ads.txt 설정 방법**의 계정별 코드 스니펫을 사용한다.

**호스팅 경로 주의:** 크롤러는 개발자 웹사이트 URL의 도메인 최상위
`https://도메인/app-ads.txt`를 읽는다. 현재 개인정보처리방침 주소의 프로젝트 경로
`/shallwepuzzle-privacy/app-ads.txt`에만 파일을 올려서는 충분하지 않다.
GitHub Pages를 계속 쓰면 `https://dydxo116.github.io/app-ads.txt`를 제공하는 사용자 사이트가
필요하거나, 최상위 파일을 제공할 수 있는 별도 도메인/Firebase Hosting을 사용해야 한다.
개인정보처리방침 URL 자체는 바꿀 필요 없다.

## 5. 필요한 테스트 요건 완료 후 프로덕션 검토 요청

2023-11-13 이후 생성한 **개인 개발자 계정**에 해당한다면, 최소 12명의 테스터가
14일 연속 참여를 유지하는 비공개 테스트를 진행하고 프로덕션 액세스를 신청한다.
내부 테스트는 이 필수 비공개 테스트를 대신하지 않는다. 해당 여부는 Console
대시보드에서 확인한다. 모든 계정에 이 조건이 적용된다고 단정하지 않는다.

요건과 등록정보를 마쳤으면 프로덕션 출시 만들기 → 서명 AAB 선택 → 출시 노트와
배포 국가 검토 → 오류 해결 → Google Play 검토 요청 순서로 진행한다.
이 문서의 작성이나 GitHub Release 게시는 Play 심사 제출/공개 출시가 아니다.

## 확인한 공식 안내

- [새 개인 개발자 계정의 테스트 요건](https://support.google.com/googleplay/android-developer/answer/14151465?hl=ko)
- [AdMob 앱 인증](https://support.google.com/admob/answer/14538460?hl=ko)
- [app-ads.txt 설정과 크롤링 위치](https://support.google.com/admob/answer/9363762?hl=ko)
- [Google Play 데이터 보안](https://support.google.com/googleplay/android-developer/answer/10787469?hl=ko)
