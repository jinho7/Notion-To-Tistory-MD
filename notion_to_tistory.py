import os
import re
import shutil
from urllib.parse import unquote

NOTION_FOLDER = "notion_folder"
UPLOADED_IMAGES_FILE = "uploaded_images.md"

def find_notion_export():
    """notion_folder에서 Markdown 파일과 이미지 폴더 찾기"""
    files = os.listdir(NOTION_FOLDER)
    
    # Markdown 파일 찾기
    md_files = [f for f in files if f.endswith('.md')]
    if not md_files:
        print("❌ MD 파일을 찾을 수 없습니다.")
        return None, None

    md_file = md_files[0]
    image_dir = os.path.splitext(md_file)[0]  # 동일한 이름의 이미지 폴더 찾기
    
    return os.path.join(NOTION_FOLDER, md_file), os.path.join(NOTION_FOLDER, image_dir)

def rename_images(image_dir):
    """이미지 파일을 image_001 형식으로 정리"""
    if not os.path.exists(image_dir):
        print("❌ 이미지 폴더가 존재하지 않습니다.")
        return []

    image_files = sorted(os.listdir(image_dir))  # 정렬하여 순서 유지
    new_filenames = []

    for idx, filename in enumerate(image_files, 1):
        _, ext = os.path.splitext(filename)
        new_filename = f"image_{str(idx).zfill(3)}{ext}"
        shutil.move(os.path.join(image_dir, filename), os.path.join(image_dir, new_filename))
        new_filenames.append(new_filename)

    print(f"✅ {len(new_filenames)}개의 이미지가 정리되었습니다.")
    return new_filenames

def load_uploaded_image_links():
    """업로드된 티스토리 이미지 링크 불러오기"""
    if not os.path.exists(UPLOADED_IMAGES_FILE):
        print("❌ uploaded_images.md 파일을 찾을 수 없습니다.")
        return []

    with open(UPLOADED_IMAGES_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    # 티스토리에서 생성된 이미지 링크만 추출
    links = re.findall(r'\[##_Image\|(.*?)\|', content)
    print(f"📸 {len(links)}개의 업로드된 이미지 링크를 확인했습니다.")
    return links

def replace_images_in_markdown(md_file, image_links):
    """MD 파일에서 이미지 링크를 티스토리 형식으로 변환하고 헤더 수정"""
    with open(md_file, "r", encoding="utf-8") as f:
        content = f.read()

    # 이미지 링크 변환
    def replace_image(match):
        return f"[##_Image|{image_links.pop(0)}|CDM|1.3|{{\"filename\":\"image.png\"}}|_##]" if image_links else match.group(0)

    content = re.sub(r"!\[.*?\]\(.*?\)", replace_image, content)

    # Markdown 헤더 변환: "# -> ##", "## -> ###", "### -> ####"
    content = re.sub(r"^(#{1,3})\s", lambda m: "#" + m.group(1) + " ", content, flags=re.MULTILINE)

    # 변환된 파일 저장
    output_file = "converted_" + os.path.basename(md_file)
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"✅ 변환 완료: {output_file}")

def main():
    print("🚀 Notion to Tistory 변환 시작")
    
    # 1️⃣ Markdown 및 이미지 폴더 찾기
    md_file, image_dir = find_notion_export()
    if not md_file or not image_dir:
        return
    
    print(f"\n📝 변환 대상: {md_file}")
    
    # 2️⃣ 이미지 정렬 및 이름 변경
    rename_images(image_dir)

    print("\n⏳ 다음 단계:")
    print("1. 티스토리 글쓰기 페이지에서 '모든 이미지'를 업로드")
    print("2. 기본 모드 > 마크다운으로 변경")
    print("3. 업로드된 이미지 링크 전체 복사 후 'uploaded_images.md'에 복사")
    input("\n모든 이미지 파일을 업로드하고 Enter를 눌러주세요...")

    # 3️⃣ 업로드된 이미지 링크 불러오기
    uploaded_image_links = load_uploaded_image_links()
    if not uploaded_image_links:
        print("❌ 업로드된 이미지 링크가 없습니다.")
        return
    
    # 4️⃣ MD 파일 내 이미지 링크 변환 & 헤더 변환
    replace_images_in_markdown(md_file, uploaded_image_links)

if __name__ == "__main__":
    main()
