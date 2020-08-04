# Pupple Application

## 개발 
### 1. 개발 환경 준비
#### a. [pipenv](https://github.com/pypa/pipenv) 설치
pipenv 는 파이썬 패키지 (개발하는데 필요한 라이브러리들) 을 관리해줌. 쉽게 설치하고 삭제할 수 있게, 그리고 서로 의존 버전이 꼬이지 않게 개발자의 수고를 덜어주는 프로그램. 
```shell script
$ brew install pipenv
```

#### b. python 가상환경 접속 
의존성이 개발자의 컴퓨터에 global 하게 설치되지 않고, 이 프로젝트 범위 내에서만 설치되도록 pipenv 가 가상의 울타리를 만들어놓음. 그 울타리 안으로 접속해서 django 를 실행해야함.
```shell script
$ pipenv shell
```

#### c. 의존성 설치 
울타리 안으로 들어와서, `Pipfile` 에 적힌대로 환경을 세팅함.
```shell script
$ pipenv install
```

### 2. 개발하기
#### a. 개발 서버 실행 
```shell script
python manage.py runserver
```

#### b. 새로운 패키지 설치
```shell script
pipenv shell
pipenv install ${패키지명} 
```

#### c. 새로운 주제 만들기 
```shell script
python manage.py startapp ${주제이름}
```
