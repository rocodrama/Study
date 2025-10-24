# import pathlib
from pathlib import Path

### 경로 생성 및 확인 ###

# 경로 객체 생성
path = Path("경로")

# 홈 디렉토리
path = Path.home()
print(path)

# 현재 작업 디렉토리
# print(pathlib.Path.cwd())
path = Path.cwd()
print(path)

# 경로 결합
path = path / "file/sample.txt"
print(path)

# 파일 또는 디렉토리 존재 확인
print(path.exists())

# 경로가 디렉토리인지 확인
print(path.is_dir())

# 경로가 파일인지 확인
print(path.is_file())

# 파일 또는 디렉토리 상세 정보 확인
print(path.stat())

### 경로 구성 요소 접근 및 변경 ###

# 파일 이름 또는 디렉토리 이름
print(path.name)

# 파일 이름(확장자 제외)
print(path.stem)

# 확장자(.포함)
print(path.suffix)

# 모든 확장자 리스트
print(path.suffixes)

# 상위 디렉토리 경로 객체 반환
print(path.parent)

# 경로의 앵커(최상위 디렉토리)
print(path.anchor)

# 파일 또는 디렉토리 이름 변경(확장자 포함)
path.with_name("rename.py")
path.with_name("sample.py")

# 이름만 변경
path.with_stem("rename")
path.with_stem("sample")

# 확장자만 변경
path.with_suffix(".txt")

### 파일 또는 디렉토리 조작 ###

# 경로 결합(오버로딩)
p = Path.cwd() / "file" / "test"

# 디렉토리 생성
p.mkdir(
    parents=False, exist_ok=True
)  # parents: 상위 폴더 없으면 함께 생성, exist_ok: 이미지 존재해도 에러 무시

# 빈 디렉토리 삭제
# p.rmdir()

# 파일 또는 디렉토리 이름 변경 또는 이동(폴더 생성x, 이름만 변경)
p.rename(p.cwd() / "file/new_path/new_name")

# 파일 또는 디렉토리 이동(대상 경로 있으면 덮어쓰기)
p.replace()

# 파일 삭제
p.unlink()

### 경로 탐색 및 검색 ###

# 현재 디렉토리의 모든 파일 또는 폴더를 반복자로 변환
p.iterdir()

# 현재 디렉토리 및 하위 1단계에서 패턴 일치 파일 또는 폴더를 반복자로 변환
p.glob("pattern")

# 현재 디렉토리 및 모든 하위 디렉토리에서 패턴 일치 파일 또는 폴더를 반복자로 변환
p.rglob("pattern")

# 절대 경로를 반환하고, 심볼릭 링크를 따라가 실제 경로를 확정
p.resolve()

### 파일 내용 입출력 ###

# 파일의 모든 텍스트 내용을 읽어 문자열로 반환
p.read_text(encoding="utf-8")

# 문자열 데이터를 파일에 저장(덮어쓰기)
p.write_text("New contents", encoding="utf-8")

# 파일의 바이너리 내요을 읽어 bytes 객체로 반환
p.read_bytes()

# 바이너리 데이터를 파일에 저장(덮어쓰기)
p.write_bytes("New contents")
