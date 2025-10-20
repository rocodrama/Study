import os

### 디렉토리 관련 함수 ###

# 현재 작업 디렉토리 문자열로 반환
os.getcwd()

# 현재 작업 디렉토리를 지정된 경로로 변경
os.chdir('path')

# 지정된 경로 내의 모든 파일과 디렉토리 이름을 리스트로 반환
os.listdir('path')

# 지정된 경로에 새로운 디렉토리 생성
os.mkdir('path')

# 지정된 경로에 모든 중간 디렉토리를 포함하여 새로운 디렉토리 생성
os.makedirs('path')

# 지정된 경로의 빈 디렉토리를 삭제
os.rmdir('path')

# 지정된 경로의 빈 디렉토리를 재귀적으로 삭제(빈 상위 디렉토리까지 모두 삭제)
os.removedirs('path')

### 파일 및 경로 조작 ###

# 경로 결합(os에 맞는 구분자로 결합)
os.path.join('path1','path2')

# 파일 또는 디렉토리 확인
os.path.isfile('path')
os.path.isdir('path')

# 지정된 경로의 절대 경로 반환
os.path.abspath('path')

# 지정된 경로에서 파일명만 추출하여 반환
os.path.basename('path')

# 지정된 경로에서 디렉토리 경로만 추출하여 반환
os.path.dirname('path')

# 경로를 파일명과 확장자로 분리하여 튜플 형태로 반환
os.path.splitext('path')

### 파일 이름 변경 및 삭제 함수 ###

# 파일 또는 디렉토리의 이름을 변경하거나 이동
os.rename('src','dst')

# 파일 삭제
os.remove('path')
os.unlink('path')

### 시스템 제어 ###

# 디렉토리 트리를 순회하며 모든 하위 디렉토리의 정보를 반복적으로 반환
os.walk('path')

# 운영체제의 shell 명령을 실행
os.system('command')

# 환경 변수에 접근하는 딕셔너리 객체(환경 변수를 읽거나 설정)
os.environ

# 현재 운영 체제의 이름 반환
os.name

# 현재 실행 중인 프로세스의 PID 반환
os.getpid()