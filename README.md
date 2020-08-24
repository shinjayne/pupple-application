# Pupple Application

## 개발 

### 1. 개발 환경 준비
#### a. git clone 코드 내려받기 
코드를 내려받습니다.  이후 프로젝트 폴더를 IDE 나 Code Editor 로 엽니다.
```shell script
$ git clone https://github.com/shinjayne/pupple-application.git
```

#### b. [pipenv](https://github.com/pypa/pipenv) 설치
pipenv 는 파이썬 패키지 (개발하는데 필요한 라이브러리들) 을 관리해줌. 쉽게 설치하고 삭제할 수 있게, 그리고 서로 의존 버전이 꼬이지 않게 개발자의 수고를 덜어주는 프로그램. 
```shell script
$ brew install pipenv
```

#### c. python 가상환경 접속 
의존성이 개발자의 컴퓨터에 global 하게 설치되지 않고, 이 프로젝트 범위 내에서만 설치되도록 pipenv 가 가상의 울타리를 만들어놓음. 그 울타리 안으로 접속해서 django 를 실행해야함.
```shell script
$ pipenv shell
```

#### d. 의존성 설치 
울타리 안으로 들어와서, `Pipfile` 에 적힌대로 환경을 세팅함.
```shell script
$ pipenv install
```

> #####  🔴 Why Pipenv?
>  
>  `pipenv` 의 패키지 매니징 기능은 `pip install` 과 `requirements.txt` 를 대체합니다. Python 가상환경 관리와 패키지 관리를 동시에 해주기 때문에, 개개인의 로컬 환경과 배포 환경 등 다양한 python 환경을 통일되게 관리할 때 큰 비용적인 이점이 있습니다.
>  
> 즉, Pipenv 는 복잡한 문제를 추상화해줍니다.
> 1. 패키지 의존성간의 버전 문제를 `Pipfile.lock` 으로 알아서 관리해줍니다. 특히 여러 개발자가 동일한 소스베이스를 바라보고 동시 수정하는 경우 더욱 장점이 있습니다. 
> 2. `Pipfile` 로 python 가상환경과 의존성을 한번에 관리해줍니다.
> 3. `pipenv shell` 로 가상환경에 접속하고, `pipenv install` 로 가상환경 내 의존 패키지를 최신화합니다.  더 설치된 게 있으면 삭제해주고, 덜 설치된 것이 있으면 설치해주고, 버전이 맞지 않으면 업그레이드해줍니다. 단순한 조작으로 모든 것을 알아서 해줍니다.
>
> 다른 많은 언어들도 `pipenv` 와 같이, 환경과 의존성을 한번에 관리하는 것이 큰 흐름으로 가고 있고, 실제로 생산성 향상에 기여하고 있습니다. 

### 2. 개발하기
#### a. 개발 서버 실행 
```shell script
python manage.py runserver
```

#### b. 새로운 패키지 설치
```shell script
pipenv shell
pipenv install ${패키지명}

# examples
pipenv install django-model-utils
pipenv install pillow
```

#### c. 새로운 주제 만들기 
```shell script
python manage.py startapp ${주제이름}
```

### 3. 해볼만한 개발 과제들
 
1. 이미지 여러개 가로로 스크롤할 수 있는 컴포넌트 만들어보기 
2. 유튜브 임베드 웹페이지 만들어보기 
3. 퍼플 기획안에 맞게 DB 모델링해보기  
