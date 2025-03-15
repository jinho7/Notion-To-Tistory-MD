# Notion-To-Tistory-Markdown-Converter

## 📝 소개
**Notion-To-Tistory-Markdown-Converter**는 Notion에서 내보낸 Markdown 파일을 Tistory 블로그에서 최적화된 형식으로 변환하는 Python 스크립트입니다. 이 도구는 Notion의 Markdown 내보내기에서 발생하는 문제를 자동으로 처리하여 이미지 정리, Markdown 형식 수정, Tistory 이미지 링크 변환을 수행합니다.

## ✨ 주요 기능
- **Notion 내보내기 자동 탐색**: `notion_folder/` 내의 `.md` 파일과 이미지 폴더를 자동으로 찾음
- **이미지 정리 및 이름 변경**: 이미지 파일을 `image_001.png`, `image_002.png` 등의 형식으로 정리하여 순서를 유지
- **Tistory 호환 Markdown 변환**:
  - Notion 이미지 링크를 Tistory `[##_Image|...|_##]` 형식으로 변환
  - Markdown 헤더(`#` → `##`, `##` → `###`, `###` → `####`) 자동 조정
  - Notion에서 개행이 유지되지 않는 문제 해결
- **간편한 워크플로우**: Tistory에 이미지를 업로드하고 링크를 복사한 후, 변환 스크립트를 실행하면 끝!

## 🚀 사용 방법
1. **Notion 페이지를 내보내기** → **Markdown & CSV** 형식으로 다운로드
2. **내보낸 파일을 `notion_folder/` 에 복사** (`.md` 파일 및 이미지 폴더 포함)
3. **스크립트 실행**:
   ```bash
   python notion_to_tistory.py
   ```
4. **Tistory에 이미지 업로드** 후, 업로드된 이미지 URL을 `uploaded_images.md`에 복사
5. **Enter 키를 누르면** 변환이 완료된 Markdown 파일이 생성됨

## 🛠 개선 및 수정 사항
### 🔹 Notion 내보내기 문제 해결
1. **Markdown 내보내기 시 줄바꿈이 사라지는 문제** → 줄바꿈을 자동으로 처리
2. **목차 깊이가 3단계를 초과하면 깨지는 문제** → 자동으로 수정
3. **목차 내 이미지 또는 코드 블록이 있을 경우 깨지는 문제** → 올바르게 변환되도록 처리

## 📌 설치 및 필요 사항
### 사전 요구 사항
- Python 3.x 설치 필요

### 의존성 패키지 설치 (필요 시)
```bash
pip install -r requirements.txt
```

## 🏗️ 폴더 구조
```
Notion-To-Tistory-Markdown-Converter/
├── notion_folder/                # Notion에서 내보낸 .md 파일 및 이미지 폴더
├── uploaded_images.md            # Tistory에 업로드한 이미지 링크를 복사해서 넣는 파일
├── notion_to_tistory.py          # 메인 변환 Python 스크립트
├── converted_<파일명>.md         # 변환 완료된 Markdown 파일
└── README.md                     # 프로젝트 설명 문서
```# Notion-To-Tistory-MD
# Notion-To-Tistory-MD
