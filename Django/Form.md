# Form

- Form 의 주요 역할

  - 입력 값 검증
  - 입력된 값이 검증에 통과하면 검증된 값을 Dictionary 형식으로 제공 (cleaned_data)

  

- Form 을 선언하는 방법

  - Model 선언하는 방법과 굉장히 유사
  - Form 정의
  - views.py 에서 정의한 Form 인스턴스를 만들어서 context 로 전달



- ModelForm





# Static

- img, js, css : **static file**
- 따로 폴더에 넣어서 보여줘야 합니다.
- like html ....



static 파일을 서브 할려면

1. 각 앱의 static 이라는 폴더 아래에 static file 이 위치해 있어야 한다.

   - 앱 폴더 외부에 있는 static 파일이라면 STATICFILES_DIRS 를 settings.py에 등록

2. static tag 를 이용해서 불러와야 함

   ```
   {% load static %} 상단에 있어야 함. extends tag 보다는 밑에 있어야 함.
   <img src="{% static '스태틱 파일 같은 경로' %}" 
   ```

   



### STATIC_URL

- 웹 페이지에서 사용하는 static file의 최상위 URL 경로
- 실제 파일이나 디렉토리 경로는 아님
- url 로만 존재하는 단위
- 반드시 `/` 로 끝나야 함
- STATIC_ROOT 설정에 있는 static file 을 참조할 때 사용하는 URL



### STATIC_ROOT (배포용)

- 배포할 때 사용하는 static file 경로
- `python manage.py collectstatic`
  - 프로젝트 배포 시 흩어져 있는 static file 을 모아서 특정 디렉토리로 옮기는 작업
  - 앱 폴더 내부의 static 폴더와 STATICFILES_DIRS 에 등록된 디렉토리의 static file 을 모아 줌.
- DEBUG = True 인 경우에는 파일경로로 인식되지 않음.
  - 실 서비스 환경에서만 동작
- DEBUG = False 인 경우 우리는 더 이상 장고에서 static 파일을 서비스 할 수 없음.
  - 웹 서버에서 static 파일을 전송해줘야 함.



### STATICFILES_DIRS (only 개발용)

- 외부에 있는 static file 을 찾아 오기 위해 등록

- like ... base.html 경로 등록

  ```
  STATICFILES_DIRS = [
      BASE_DIR / 'assets',
  ]
  ```

  



# Media

- 사용자가 업로드한 사진을 서비스 하는 방법
- 파일 자체는 static 이지만, **언제, 어떤 파일을 제공하는지 예측할 수 없는 파일**
- 모델 정의
  - ㅇ
- form 의 encryte 속성을 설정
  - application/x-www : 기본값, 모든 문자 인코딩
  - multipart/form-data : 파일/이미지 업로드시 반드시 사용해야 함
  - text/plain : 인코딩을 하지 않은 문자 그대로 전송



### MEDIA_ROOT

- 업로드가 끝난 파일을 위치할 최상위 경로를 지정하는 설정



### MEDIA_URL

- like **STATIC_URL**



_______________________________

이미지 사이즈 조절





______________________________

blank vs null

- null : DB 와 관련
- blank : 데이터의 유효성
- CharField, TextField 문자열을 기반으로 저장하는 필드들!!!!
  - `blank = True`
  - ""

