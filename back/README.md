# create-api-server

## Python 버전

- python 3.11.4 version

### 프로젝트 의존성 설치
### install project dependency

```
# cd back/ 
pip install -r requirements.txt
pip install "passlib[bcrypt]"
```

### DB 세팅
```
# cd back/
# config.json 파일에 DB 정보 작성

pip install alembic
alembic init migrations

# 생성된 alembic.ini 파일을 열어 sqlalchemy.url을 찾아 아래처럼 작성 -실제 데이터 입력 필요-
# sqlalchemy.url = postgresql://<DB_USER>:<DB_PWD>@<<DB_HOST>:<DB_PORT>/<DB_NAME>
# /migrations/env.py 파일을 열어 파일 상단에 import models 추가 
# target_metadata를 찾아 아래처럼 작성
# target_metadata = models.Base.metadata



alembic revision --autogenerate
alembic upgrade head

```

### 실행

```bash
uvicorn main:app --reload
```


>> http://127.0.0.1:8000/docs 경로에서 api 문서 확인 가능