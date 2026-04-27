# OnlineSelfCodingGroup 작업 규칙

매주 토요일 모각코 진행 후 두 파일을 업데이트하는 작업입니다.
작업 시작 시 해당 주차의 GitHub issue link가 주어집니다.

## 작업 파일

1. `README.md` — 참여자 수, 랭킹 업데이트
2. `Stamp/README.md` — 스탬프 이미지, starbucks 이미지, book count 업데이트

---

## 1. README.md 업데이트

### 1-1. 해당 주차 meetup list 항목 업데이트

`## 2026 1Q meetup list` (혹은 해당 분기) 섹션에서 해당 회차를 찾아 `will be open`을 참여자 수로 변경합니다.

```
- [278th, 2026-03-14](issue_link), joined 3
```

참여자 수는 issue의 **assignees** 수로 확인합니다.

```bash
gh issue view <issue_number> --repo ThinkAboutSoftware/OnlineSelfCodingGroup
```

### 1-2. 2026 랭킹 테이블 업데이트

`### Ranking 2026, ...` 섹션에서 참여한 멤버의 Count를 1씩 증가시킵니다.

- 신규 참여자는 테이블 하단에 추가합니다.
- 신규 참여자의 초기 Count는 1입니다.

### 1-3. 전체 랭킹 테이블 업데이트

`### All from first to present` 섹션에서 참여한 멤버의 Count를 1씩 증가시킵니다.

- 신규 참여자는 테이블 하단에 추가하고 Ranking 번호를 순서대로 부여합니다.
- 신규 참여자의 초기 Count는 1입니다.

---

## 2. Stamp/README.md 업데이트

### 2-1. 참여자 확인

issue의 comments를 통해 참여자와 comment ID를 확인합니다.

```bash
gh api repos/ThinkAboutSoftware/OnlineSelfCodingGroup/issues/<issue_number>/comments \
  --jq '.[] | {id: .id, author: .user.login, url: .html_url}'
```

### 2-2. 스탬프 이미지 수 결정 (double stamp 규칙)

**jongfeel을 제외한** 참여자 수가 **1명 또는 2명**이면 모든 참여자(jongfeel 제외)에게 스탬프 2개를 부여합니다. 그 외에는 1개입니다.

| jongfeel 제외 참여자 수 | 스탬프 수 |
|------------------------|---------|
| 1명 또는 2명 | 2개 |
| 3명 이상 | 1개 |

**jongfeel은 항상 스탬프 1개**입니다.

### 2-3. book count 결정

book count는 **참여 횟수** 기준으로 증가합니다 (스탬프 수와 무관).

- 이전 book count + 1
- 신규 참여자는 book 1/20부터 시작합니다.
- book 20/20 도달 시 다음 참여부터 book 1/20으로 리셋됩니다 (책 선물 획득).

### 2-4. starbucks 이미지 추가 규칙

스탬프 누적 횟수가 **4의 배수**에 도달할 때 starbucks 이미지를 추가합니다.

- 이번 meetup에서 받은 스탬프 중 4의 배수에 해당하는 스탬프가 있으면 starbucks 이미지 삽입
- starbucks 이미지 파일: `Starbucks_americano.JPG`

**starbucks 이미지 삽입 위치:**
- 4의 배수가 되는 스탬프 **바로 뒤**에 삽입
- 스탬프 2개 중 첫 번째 스탬프가 4의 배수 도달 → `stamp, starbucks, stamp`
- 스탬프 2개 중 두 번째 스탬프가 4의 배수 도달 → `stamp, stamp, starbucks`
- book 20/20 완료 시 → `stamp, starbucks, stamp` (cycle 완료 + 새 cycle 시작)

### 2-5. 스탬프 항목 형식

```html
<a href="https://github.com/ThinkAboutSoftware/OnlineSelfCodingGroup/issues/<issue_number>#issuecomment-<comment_id>"><img src="approved_1Q.png"/>book N/20</a>
```

분기별 스탬프 이미지:
| 분기 | 이미지 |
|------|--------|
| 1Q | `approved_1Q.png` |
| 2Q | `approved_2021_2Q.png` |
| 3Q | `approved_2021_3Q.png` |
| 4Q | `approved.png` |

### 2-6. 테이블 행 순서 규칙

- **기존 참여자**: 기존 행 순서 유지
- **신규 참여자**: 해당 meetup 참여 순서(comment 순서)에 맞게 삽입

### 2-7. 신규 참여자 행 추가 형식

해당 meetup 이전 열은 모두 빈 셀(`| |`)로 채웁니다.

```
| [이름](https://github.com/username/) | | | ... | | <stamp 항목> |
```

---

## 3. Commit 규칙

파일별로 **별도 commit**합니다.

```
# README.md
Update joined count and ranking for <N>th online meetup <YYYY-MM-DD>

# Stamp/README.md
Add joined stamps for <N>th online meetup <YYYY-MM-DD>
```

---

## 4. Push & Pull Request

```bash
# push (jongfeel 계정 사용, branch는 프롬프트에서 주어진 issue 기준으로 이미 생성됨)
TOKEN=$(gh auth token --user jongfeel)
git push "https://jongfeel:$TOKEN@github.com/ThinkAboutSoftware/OnlineSelfCodingGroup.git" <branch_name>

# PR 생성
GH_TOKEN=$TOKEN gh pr create --title "..." --base main --head <branch_name> --body "..."
```

---

## 5. 작업 흐름 요약

1. issue link로 참여자 및 comment ID 확인
2. `README.md` 업데이트 후 commit
3. `Stamp/README.md` 업데이트 후 commit
4. feature branch 생성 → push → PR 생성
