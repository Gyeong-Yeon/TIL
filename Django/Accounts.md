# Account 간단 요약

- 앱을 새롭게 생성
- **Article** 이 이미 존재하지만 **게시글**을 관리하는 역할을 하는 앱
- **회원관리** 역할을 하는 기능이 필요한데 **Account**



## 회원 가입 기능 추가

- 회원가입 == DB 유저 정보를 새롭게 추가 행위 (Create)
- **UserCreationForm** : django 에서 기본적으로 제공해주는 폼
  - 유저 정보를 DB 에 저장을 해야 함 => ModelForm
  - `from django.contrib.auth.forms import UserCreationForm`
  - 나머지 로직은 이전 CRUD 의 CREATE 동일
- 회원 가입을 하면 따로 로그인을 해야한다!!
  - 근데 우리는 이미 로그인하는 방법을 알고 있다.
  - 회원 가입을 한다라는 것은 우리 사이트의 회원임이 인증된 것이다.



### 로그인

- 쿠키
  - 브라우져에 저장
  - 키-벨류 작은 데이터 파일
  - 만료일자
  - 쿠키 종류
    - 세션 쿠키
      - 사용자가 사이트를 탐색할 때, 설정과 선호 사항을 저장하는 임시 쿠키
      - 브라우져를 닫으면 삭제
    - 지속 쿠키
      - 사용자가 주기적으로 방문하는 사이트에 대한 설정 정보나 로그인 이름을 유지하기 위해 주로 사용
      - 브라우저를 닫거나 컴퓨터를 재시작해도 남아 있음
- 세션
  - 서버 DB 혹은 메모리
  - 정말 중요한 정보를 저장
  - 사용자가 많아지면 서버가 느려질 수 있음
- 로그인 == 세션을 새롭게 생성 (Create)
- **AuthenticationForm** : Django 에서 기본적으로 제공해주는 Form
  - 로그인을 위해서 입력창을 제공
  - 로그인 유효성 검사
  - DB 유저 정보와 비교해서 접속 인증 해주는 친구
  - DB 를 직접 수정하는 폼이 아니기 때문에 Form
    - 첫번째 인자로 request 정보를 보내야 함
- **login 함수** : Django 에서 기본적으로 제공해 주는 함수
  - 세션에 인증 정보를 생성해주는 함수





## 로그아웃

- 로그아웃 == 세션을 삭제(Delete)
- logout 함수 : Django 에서 기본적으로 제공해 주는 함수
  - 현재 request 에서 session 에 관한 data 를 삭제



## 접근제한

- `is_authenticated`
  - User 클래스와 AnonymousUser 의 속성 값
    - User 해당 값이 항상 True, AnonymousUser 는 항상 False
  - 유저가 인증된 유저인지 아닌지를 확인
- `is_anonymous` : 유저가 인증되지 않은 사용자인지 확인
- `is_superuser` : 유저가 최고 관리자인지 확인
- `is_staff` : 유저가 관리자 계정에 접근 가능한지 확인



- login_required 데코레이터
  - 로그인 된 유저만 해당 함수를 실행가능하게 하는 데코레이터
  - 만약 로그인이 되지 않은 유저라면
    - `/accouts/login/` 으로 redirect 해줌
    - next 라는 쿼리 문자열에 이전에 접근하려 했던 주소를 keep 해줌
      - 킵된 주소를 사용하려면 request.GET.get('next')해서 redirect
    - `@login_required(login_url='/accounts/test/')`
    - settings.py 에 LOGIN_URL 을 설정을 해주면 해당 주소로 갈 수 있음.
      - LOGIN_URL 기본 값이 '/accounts/login'



- login_required 와 require_POST 를 같이 사용할 수 없는 이유

  ```python
  @require_POST
  @login_required
  def logout(request):
      # if request.user.is_authenticated:
      auth_logout(request)
      return redirect('accounts:index')
  ```

  - 비로그인 상태로 POST 로 글쓰기를 시도 했을 때
    1. login_required 에서 로그인 페이로 리다이렉트 (POST 데이터 손실)
       - 리다이렉트는 GET
    2. 로그인을 완료 후 next 를 이용해서 다시 logout 으로 접근
       - 리다이렉트로 logout 을 접근하게 됨
    3. 결국 403 http method 에러 발생



## 회원 탈퇴

- 회원 탈퇴 == DB 에서 유저 정보를 삭제

- 이전에 데이터 베이스로 정보를 삭제하는 방법

  ```python
  def delete(request, id):
      data = Article.objects.get(pk=id) # article 정보를 가져와서
      data.delete() # article 정보에서 delete 를 실행
      ...
  ```

  

- 유저 정보는 request.user 에 담겨져 있다!!

  - request.user.delete() 를 하면 유저 정보가 삭제
  - DB 정보를 삭제하는 것이기 때문에 POST 요청





## 회원 정보 수정

- 회원 정보를 Update
- `UserChangeForm` : Django 에서 기본적으로 제공해주는 폼
  - DB 를 수정해야 하는 폼
  - ModelForm
  - 문제점
    - 일반 유저가 권한 설정을 할 수 있게 됨
    - 그대로 사용하면 절대 안됨
- `CustomUserChangeForm` : `UserChangeForm`을 상속받아서 커스텀한 폼
  - 원하는 필드만 수정할 수 있게 해야함
  - 유저의 정보를 채워서 입력 창을 보여줘야 하므로 `instance` 설정을 해줘야 함.



- 디버깅 순서 (TIP)
  - 개발순서(요청 -> url -> view -> template -> 응답)
  - 개발 순서의 역순으로 생각하면서 오류를 트래킹
    - 응답 -> template -> view -> url -> 요청(주소줄 확인 or 장고 log 에 찍힌 요청을 확인)



## 비밀번호 변경

- DB를 수정을 하는데 그런데.....말입니다......
  - 비밀번호는 텍스트 그대로 저장
  - Django 는 비밀번호를 그냥 저장하지 않고 암호화
- **PasswordChangeForm**
  - Form 을 상속받아서 정의되어 있음
  - 첫번째 인자로 `request.user` 가 반드시 필요하다
- 비밀번호 변경을 성공하게 된다면 로그인이 풀려버린다!!
  - 로그인 되면 유저 정보를 세션에 저장을 하는데
  - 비밀번호가 변경이 되면 유저 정보가 업데이트 되어서 세션에 저장된 유저정보와 데이터가 일치하지 않음
  - `update_session_auth_hash` 함수를 이용해서 세션의 유저 정보를 업데이트 시켜줘야함.



------------------------



## URL Resolver

- resolver 는 웹 브라우져에서 요청을 서버로 전달하고 서버에서 주소를 받아 브라우져에 제공하는 기능을 수행
- Django 에서  url resolver `urls.py` 에서 정의한 `path`
- reverse() 함수가 존재하는데 이 함수는 url resolvers 모듈안에 있는 메서드
  - redirect("articles:Index", articles.pk) 로 사용하는 redirect 도 reverse 함수를 사용
  - app_name 과 path 의 name 에 일치하는 실제 주소창에 입력되는 /article/1/ 을 찾아줌
  - 찾지 못하면 NoReverseMatch 오류가 발생
- 결과적으로 resolver 라는건 실제 주소창에 입력되는 주소와 장고 내부에서 사용하는 url 을 서로 번역해주는 역할을 함





## Password 암호화

- 보안 시스템이 강한 지 약한 지 확인하는 방법은 가장 약한 부분이 얼만큼 강한 지에 따라서 결정
- PBKDF2
  - NIST (미국표준기술연구소) 에 의해서 인증된 암호화 방식
  - 미국 정부 시스템에서도 패스워드 관리할 때 사용



- 패스워드를 저장하는 방식
  - 있는 그대로 저장
  - 암호화를 시킨다
    - 단방향 해쉬함수를 이용해서 암호화를 시킴
      - 단방향 이란??
        - 메시지를 암호화하기는 쉽지만 그 반대는 불가능한 것
      - 암호화된 해쉬 데이터를 (다이제스트) 를 DB 에 저장
  - 단방향 해쉬 함수의 문제점
    - 동일한 메세지는 동일한 hash 값을 가지게 됨
    - 속도가 빨라서 문제
      - MD5 라는 알고리즘. 1초 56억번 대입연산할 수 있음.
      - 해커는 개이득, 서버측에서는 난감.
  - 단방향 해쉬함수 보완
    - Salt + 메세지 암호화
      - Salt 는 랜덤한 문자열
      - 동일한 hash 값이 아닌 다른 hash 값을 가지게 됨
    - 속도가 빠른 문제를 해결하기 위해서 iteration
      - 반복 hash 데이터를 생성
      - 반복 숫자만 가지고 있으면 암호화 할 수 있음
      - 연산이 많아져서 속도를 늦출 수 있음



- 장고에서는 어떻게 비밀번호를 비교??
  - 기존 비밀번호는 이미 솔트와 반복횟수로 암호화 되어 있음
  - DB 에 암호화된 다이제스트와, 해당 유저의 솔트값과 횟수를 저장
  - 입력되는 password 를 해당 값들로 암호화해서 다이제스트를 만든 뒤
  - 그 다이제스트 끼리 비교를 함

