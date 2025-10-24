# 파일 읽기
with open("파일경로", "r", encoding="utf-8") as f:
    data = f.read()

# 파일 쓰기
with open("파일경로", "w", encoding="utf-8") as f:
    f.write("contents")

# 파일 추가작성
with open("파일경로", "a", encoding="utf-8") as f:
    f.write("\nNew contents")
