### Data Base

- 체계화된 데이터의 모임.
- 자료를 구조화해서 기억시켜놓은 테이블의 집합체
- 장점
  - 데이터 중복 최소화
  - 데이터 무결성(정확한 정보 보장)
  - 데이터 일관성
  - 데이터 독립성
  - 데이터의 보안 유지 (Sqlite 제외...Oracle, mySql, postgresql, ...)

### RDBMS (Relational Data Base Manage System)

- 용어 정리
  - 칼럼 : 고유한 데이터 형식이 지정되는 **열**
  - 레코드 : 단일 구조 데이터 항목을 가리키는 **행**
  - 기본키(Primary Key) : 각 행의 고유 값
  - 테이블 : 열과 행의 모델을 사용해 조직된 데이터 요소들의 집합 (엑셀 테이블)
  - 스키마 : RDB 에서 구조와 제약조건을 전반적으로 기술한 명세서. 테이블이 어떻게 생겼고 어떤 구조를 가지고 제약조건은 어떤 것들이 있는지 적혀있는 설계도
- 장점
  - 만들기도 쉽고, 확장이 용이하다.



### Sqlite

- `rowid` : PRIMARY KEY 속성을 가지는 컬럼을 작성하지 않으면 자동으로 생성되는 필드이다.
  - INTERGER 속성
  - 64비트가 최대 값 2^64
  - 사용자가 직접 수정 불가
  - `autoincrease` 설정을 적용하지 않음
    - 적용하려면 따로 컬럼을 정의해줘야 함. 삭제를 하면 자동으로 숫자를 증가시켜서 이전 pk 값은 사용하지 않는 속성.
- `.table`, `.schema`, `.database`..... (dot command) 
  - SQL 문이 아니다.

### SQL

- `;` 까지 하나의 문장으로 판단한다.
  - 중간에 엔터를 치던, 공백을 엄청 크게 가져가던 세미콜론까지를 하나의 문장으로 봄
- 소문자로 작성해도 동작이 된다. (대문자 작성을 권장)

  - 소문자로 작성하게 되면 가독성이 떨어진다.
- 주석은 한줄 (`--`), 여러줄 (`/* 주석을 입력 */`)



- DDL

  - 데이터베이스(테이블) 구조를 정의하는 언어

  - **테이블**을 생성, 수정, 삭제할 때 주로 사용

  - CREATE (생성)

    ```SQL
    CREATE TABLE 테이블명 (
    	컬럼명1 데이터타입 [제약조건],
        컬럼명2 데이터타입,
        ...
    );
    ```

    - 기본으로 NULL 허용으로 되어 있음

    - 데이터 타입

      | Data Type                       | 내용                                   |
      | ------------------------------- | -------------------------------------- |
      | **INT** or **INTEGER**          | 정수                                   |
      | **CHAR(n)** or **CHARACTER(n)** | 길이가 n 인 문자열                     |
      | **VARCHAR(n)**                  | 최대 길이가 n인 문자열 (크기는 가변적) |
      | **FLOAT(n)**                    | 부동 소수점 실수                       |
      | **DATETIME**                    | 년월일                                 |
      | **BLOB**                        | 바이너리 값 그대로 저장                |
      | **SMALLINTEGER**                | INT 보다 작은 정수                     |
      | **NUMERIC** or **DECIMAL**      | 실수를 저장                            |
      | **TEXT**                        | 문자열                                 |

  - ALTER (수정)

    ```SQL
    ALTER TABLE 테이블명
    RENAME TO 변경할 테이블명;
    
    ALTER TABLE 테이블명
    ADD 컬럼명 데이터타입 [제약조건];
    ```

  - DROP (삭제)

    ```SQL
    DROP TABLE 테이블명;
    ```

  - TRUNCATE (테이블 초기화) : SQLite 에서는 존재하지 않음

  

- DML

  - DB에 저장된 레코드를 생성하거나 저장된 레코드를 조회, 생성, 수정, 삭제

  - SELECT (데이터 조회)

    - DISTICT : 중복된 값을 없애고 결과로 반환

      - `SELECT DISTICT director FROM movie;`

    - 산술 연산 검색

      - `SELECT money * 100 FROM movie;`

    - 조건 검색 (WHERE)

      - 기본 비교 연산자 사용 가능 (>, <, !=, ...)

      - `IN`, `BETWEEN`

        - `SELECT age IN (18, 19, 20) FROM people`
        - `SELECT * FROM people WHERE age BETWEEN 20 AND 30;`

      - AND, OR

      - LIKE

        - 와일드 카드
        - `%` : 0개 이상. 있던지 없던지 해당 패턴과 비슷한 값을
        - `_` : 1개. 무조건 해당 자리에 어떤 값이 하나가 존재해야 한다.

      - ORDER BY : 정렬 (ASC / DESC)

      - GROUP BY 컬럼명 (HAVING 조건)

        - 특정 속성의 데이터를 모아 그룹을 지을 수 있다.
        - AS 로 컬럼명을 지을 수 있음
        - `HAVING 조건` : 해당 조건을 만족하는 데이터를 그룹지어 준다. 특정 조건을 추가할 수 있다.

      - **JOIN**

        - 두 개 이상의 테이블을 연결해서 하나의 가상 테이블을 만드는 것

        - 분산된 데이터를 하나로 묶어서 쿼리를 할 수 있다.

        - 묶여진 결과는 하나의 큰 테이블처럼 생각할 수 있다. (가상 테이블)

        - 외래키를 조언 속성으로 이용

          ```SQL
          SELECT 결과컬럼, .. FROM 테이블1 [as 별명1]
          [INNER/LEFT/CROSS] JOIN 테이블2 [AS 별명2]
          ON 연결조건 / USING 일치컬럼
          [GROUP BY]
          [ORDER BY];
          ```

          - INNER

            - 가장 많이 쓰이는 JOIN
            - 교집합

          - LEFT

            - 테이블 순서에 따라 합침
            - 값이 없을 때는 NULL 을 채워서 연결

          - CROSS

            - ON 이나 USING 으로 한정하는 필드가 없으면, N x M 개의 행을 가진 모든 조합을 만들어 냄
            - FROM 에서 두 개의 테이블을 `,` 로 나열해도 같은 효과

      - 서브쿼리

        - SELECT 안에 SELECT 를 내포하고 있는 형태

        - 내포된 SELECT 가 상위 SELECT 보다 먼저 수행

          ```SQL
          -- 컬럼에 내포하고 있는 형태. SELECT 에 사용 (스칼라 서브쿼리) (결과는 하나만 출력되어야 함.)        
          SELECT movie_name, director, (SELECT AVG(balance) FROM theaters)
          FROM movies;
                  
          -- FROM 에 내포하고 있는 형태. (서브쿼리에서 조회된 값을 테이블 처럼 활용 가능.)
          SELECT title, author, reg_date
          FROM (SELECT * FROM books WHERE CREATE_AT <= '2020-01-01')
          ORDER BY reg_date DESC;
                  
          -- WHERE에 내포하고 있는 형태
          SELECT cd_plant FROM table_plant
          WHERE cd_plant IN (SELECT cd_plant FROM table2_plant);
          ```
    
  - INSERT (데이터 생성)

    ```SQL
    INSERT INTO 테이블 [(컬럼명1, 컬럼명2, ...)] (<-컬럼리스트라고 하겠습니다.)
    VALUES (컬럼1에들어갈데이터, 컬럼2에들어갈데이터, ....) [,(속성 값들 2), (3), ...];
    ```

    - 컬럼리스트는 생략 가능하며, 생략한 경우는 테이블을 정의할 때 컬럼의 순서대로 VALUES 절의 속성 값을 적어줘야 함
    - rowid 를 사용하면 컬럼 리스트를 생략해도 id 값을 따로 입력하지 않아도 되는데
      - 따로 id 를 정의했을 때는 id 값을 넣어줘야 한다.

  - UPDATE (데이터 수정)

    ```SQL
    UPDATE 테이블명
    SET 컬럼명=수정값 [, 컬럼명2=수정값2]
    [WHERE 조건];
    ```

    - WHERE 이 없으면 모든 레코드를 수정

  - DELETE (데이터 삭제)

    ```sql
    DELETE FROM 테이블명
    [WHERE 조건]
    ```

    - WHERE 이 없으면 모든 레코드를 삭제
    
    

- DCL : 데이터 베이스와 관련된 명령어 (접근권한)

  - DB 사용자에게 특정 권한을 수여 / 회수
  - GRANT (권한 수여)
  - REVOKE (권한 회수)

  (TCL)

  - COMMIT (트랜젝션 작업이 완료되었음을 알려줌)
  - ROLLBACK (트랜젝션 작업 중 이상이 생겼을 때 원래 상태로 복구)
  - SAVEPOINT

----------------------

### ORM

- 모든 레코드 조회

  ```python
  Article.objects.all()
  ```

  - data object 가 QuerySet 으로 전달되어 짐

    ```sql
    SELECT * FROM articles;
    ```

  - Table 정보가 전달 되어짐

- 테이블 생성

  ```python
  Class 테이블명(models.Model):
      컬럼명1 = models.데이터타입필드
      컬럼명2 = models.데이터타입필드([제약조건, 속성, ...])
      ....
  ```

  - migration 이 필요
  - `python manage.py makemigrations` : migrations 파일 생성 (설계도 생성)
  - `python manage.py migrate` : 설계도를 기반으로 DB에 테이블 생성

  

- 데이터(레코드) 생성

  - 3가지 방법

    ```python
    board = Board() # 인스턴스 생성
    board.title = '제목'
    board.content = '내용'
    board.save() # DB에 정보 저장
    ```

    ```python
    board = Board(title='제목', content='내용')
    board.save() # DB에 정보 저장
    ```

    ```python
    board = Board.objects.create(title='제목', content='내용') # DB에 정보 저장
    board # 저장된 데이터와 object 가지고 있음
    ```

- 데이터(레코드) 조회

  - `.get(조건)` : 찾는 값이 1개만 있을 때 (1개 이상이 나오게 되거나 값이 없으면 오류)

  - `.filter(조건)` : 값이 있던 없던 데이터를 QuerySet 으로 리턴

  - 특정 조건에 따른 ORM 작성

    - 전체 길이, 인원 수, 갯수 : 갯수를 세려는 QuerySet 에 `.count()` 호출
    - 조건을 검색할 때 Queryset queryset field lookup 사용.(MDN 꼭 체크 해보기!!!!)
      - 크거나 같을 때 (`__gte`)
      - 특정 글자로 시작하는 조건 (`__startswith`)

  - **Q object**

    - 조건을 캡슐화 사용 가능

    - AND 표현은 `, ` 로 되는데 OR 표현은 `|` 로만 표현할 수 없다.

      ```python
      Person.objects.filter(Q(age__lte=20) | ~Q(last_name='PARK'))
      ```

      - `~` 로 NOT 을 표현할 수 있다.

  - 특정 컬럼만 보고 싶을 때 `.values(보고싶은 컬럼명, ...)`

    ```python
    Person.objects.filter(age=20).values('name')
    [{'name': 'ed', 'age':20}]
    ```

  - 정렬

    - `order_by`
      - 컬럼명 앞 `-` 부호로 오름/내림 차순(`-`)
      - `'?'` : 랜덤하게 정렬 (매우 느림)

  - LIMIT, OFFSET

    - LIMIT : 갯수 제한(슬라이싱으로 표현) [:10]
    - OFFSET : 특정 인덱스 정보 (인덱싱/슬라이싱으로 ORM에서 표현. 예)2번째 정보를 보고 싶을 땐[1])
      - SQL 도 첫 번째 자료는 0으로 접근

  - aggregation (집계)

    - 집계 함수
    - Avg, Sum, Min, Max, Count, ..... (특징 : 첫 문자가 대문자)
    - aggregate : 계산 후 딕셔너리로 그 값을 반환
    - annotate : 계산 후 결과에 컬럼을 새롭게 추가해서 그 값을 보여줌

- 데이터(레코드) 삭제

  - 삭제하려는 object 에 `delete()` 호출해주면 삭제됨

--------------------------

### 1:N

- ForeignKey
  - 필수인자 2개 필요
    - 참조하는 객체
    - `on_delete` : 참조하는 객체가 삭제되었을 때 참조하고 있는 데이터의 처리를 설정하는 속성
      - CASACDE : 참조하는 개체가 삭제되면 해당 객체를 참조하는 데이터도 삭제
      - PROTECT : 참조하고 있는 데이터가 있다면 참조 당하는 객체는 삭제할 수 없다.
      - SET_NULL : 참조하는 객체가 삭제가 되면 그 값을 NULL 로 변경. 데이터는 유지
      - SET_DEFAULT : 삭제가 되면 default 값으로 그 내용을 채워 줌. 데이터는 유지. default 설정이 필요
  - `필드 이름_id` 필드명이 생성 되어짐.
  - 역참조
    - 부모가 어떤 자식을 가지고 있는지 참조하는 형태
    
    - `자식테이블_set` 접근 가능
    
    - 자식테이블에 바로 접근이 불가능 (여러명의 자식을 가지고 있을 수 있기 때문)
    
      `parent.child_set.name (X)`
    
      - 접근을 하려면 for 문을 사용하거나 filter 로 조건을 준 후 indexing 으로 접근

![image-20201007190344910](과목평가(DB) 대비.assets/image-20201007190344910.png)

### N:M

- ManyToManyField

  - 필드가 생성되는 것이 아니라 테이블이 생성된다.

    `앱이름_모델이름_필드이름`

    - 필드 이름 생성 규칙

      - 서로 다른 테이블간의 N:M

        > `참조하는 모델 _id`
        >
        > `참조당하는 모델 _id`

      - 같은 테이블 간에 N:M

        > `from _ 모델 _ id`
        >
        > `to _ 모델 _ id`

  - 필수 인자 : 참조하는 객체

  - related_name : 역참조 이름을 설정하는 속성

    - 역참조 이름을 설정하게 되면 더이상 `_set` 으로 접근할 수 없음
    - 여러개의 참조를 하고 있는 경우 `related_name` 설정이 필수적일 때가 있다.
      - 두 테이블에서 두 개 이상의 관계 설정이 되어있을 때 related_name 필수 설정
        - User 와 Article 간에 1:N 관계와 Like로 N:M 관계로 두 개 이상의 관계 설정이 된 경우 User 에서는 Article 에 접근하기 위해 사용하는 역참조 이름 `article_set` 이 중복으로 사용되어 지기 때문에 `related_name` 을 필수적으로 지정해야 함 

  - Through : 중계 테이블을 정의해서 사용할 때 중계 테이블 등록 속성

  - symmetrical : 대칭적으로 간주해서 동시에 참조하는 속성 (니가 내 친구이면 나도 니 친구이다.)

  - 값을 추가할 때는 add / 삭제할 때는 remove



[TOC]

# 06_django_many_to_one

> 2020.09.21

<br>

## Django Relationship fields

> https://docs.djangoproject.com/ko/3.1/ref/models/fields/#module-django.db.models.fields.related

<br>

## ForeignKey (1:N Relation)

>  A many-to-one relationship

**개념**

- 외래 키는 참조하는 테이블에서 1개의 키(속성 또는 속성의 집합)에 해당하고, 참조하는 측의 관계 변수는 참조되는 측의 테이블의 키를 가리킨다.
- 하나(또는 복수) 다른 테이블의 기본 키 필드를 가리키는 데이터의 참조 무결성(Referential Integrity) 즉, 허용된 데이터 값만 데이터베이스에 저장되는 것이다.

**특징**

- 외래 키를 사용하여 **부모 테이블의 유일한 값을 참조**한다. (예를 들어, 부모 테이블의 기본 키를 참조 )
- 외래 키의 값이 부모 테이블의 기본 키 일 필요는 없지만 **유일**해야 한다.

<br>

**comment 모델 정의**

```python
# articles/models.py

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content
```

- 한 테이블에 있는 두 개 이상의 레코드가 다른 테이블에 있는 하나의 레코드를 참조할 때, 두 모델 간의 관계를 일대다 관계라고 한다.
- 이때 참조하는 대상이 되는 테이블의 필드는 유일한 값 이어야 한다. (ex. PK)
- Article : Comment = 1 : N → 하나의 게시글에는 여러 개의 댓글이 달릴 수 있다.

<br>

`on_delete`

- ForeignKey의 필수 인자이며, ForeignKey가 참조하고 있는 부모(Article) 객체가 사라졌을 때 달려 있는 댓글들을 어떻게 처리할 지 정의
- Database Integrity(데이터 무결성)을 위해서 매우 중요한 설정이다.
  - **개체 무결성**: 식별자는 NULL 혹은 중복일 수 없다. (PK / NOT NULL)
  - 참조 무결성: 릴레이션과 관련된 설정(모든 외래 키 값은 두 가지 상태 가운데 하나에만 속함)
  - 범위 / 도메인 무결성 : 컬럼은 지정된 형식을 만족해야한다. (Integer Datetime 등 / Not Null / Default / Check)

<br>

**possible values for `on_delete`**

- `CASCADE` : **부모 객체(참조 된 객체)가 삭제 됐을 때 이를 참조하는 객체도 삭제**한다.
- `PROTECT` : 참조가 되어 있는 경우 오류 발생.
- `SET_NULL` : 부모객체가 삭제 됐을 때 모든 값을 NULL로 치환. (NOT NULL 조건시 불가능)
- `SET_DEFAULT` : 모든 값이 DEFAULT 값으로 치환 (DEFAULT 설정 있어야함. DB에서는 보통 default 없으면 null로 잡기도 함. 장고는 아님.)
- `SET()` : 특정 함수 호출.
- `DO_NOTHING` : 아무것도 하지 않음. 다만, 데이터베이스 필드에 대한 SQL `ON DELETE` 제한 조건을 설정해야 한다.
- `RESTRICT`(new in 3.1) : RestrictedError를 발생시켜 참조 된 객체의 삭제를 방지

<br>

**데이터베이스 표현**

- Django는 필드 이름에 `_id`를 추가하여 데이터베이스 열 이름을 만듦

<br>

**Table 직접 확인하기**

- `article_id` 라는 컬럼이 생성되었다. 우리가 댓글을 작성하면 댓글이 해당하는 글이 **몇 번째 게시 글의 댓글인지 알아야 하기 때문**
- 만약 ForeignKey 를 article 이라고 하지 않고 `abcd = models.ForeignKey(..)` 형태로 생성 했다면 `abcd_id` 로 만들어진다. 이렇게되면 모델 관계를 파악하는 것이 어렵기 때문에 **부모 클래스명의 소문자(단수형)로 작성하는 것이 바람직하다.**

<br>

**1 : N 관계 manager**

- **Article(1)** : **Comment(N)** : `comment_set`
  - `article.comment` 형태로는 가져올 수 없다. 
  - 게시글에 몇 개의 댓글이 있는지 Django ORM이 보장할 수 없기 때문 (본질적으로는 애초에 Article 클래스에 Comment 와의 어떠한 관계도 연결하지 않음)
  - article 는 comment 가 있을 수도 있고, 없을 수도 있기 때문.
- **Comment(N)** : **Article(1)** : `article`
  - 그에 반해 댓글의 경우 `comment.article` 식의 접근이 가능한 이유는 어떠한 댓글이든 반드시 자신이 참조하고 있는 게시글이 있으므로 이와 같이 접근할 수 있다.

<br>

**`related_name`**

> https://docs.djangoproject.com/en/3.1/ref/models/fields/#django.db.models.ForeignKey.related_name

- 위에서 확인한 것처럼 부모 테이블에서 역으로 참조할 때(the relation from the related object back to this one.) `모델이름_set` 이라는 형식으로 참조한다. (**역참조**)

- related_name 값은 django 가 기본적으로 만들어 주는 `_set` 명령어를 임의로 변경할 수 있다.

  ```python
  # articles/models.py
  
  class Comment(models.Model):
      article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    ...
  ```

- 위와 같이 변경하면 `article.comment_set` 은 더이상 사용할 수 없고 `article.comments` 로 대체된다.

- 1:N 관계에서는 거의 사용하지 않지만 M:N 관계에서는 반드시 사용해야 할 경우가 발생한다.

<br>

------

<br>

## Comment

### CREATE

- CommentForm 작성

  ```python
  # forms.py
  
  from .models import Article, Comment
  
  class CommentForm(forms.ModelForm):
  
      class Meta:
          model = Comment
          fields = '__all__'
  ```

- detail 에서 commentform 보여주기

  ```python
  from .forms import ArticleForm, CommentForm
  
  def detail(request, pk):
      article = Article.objects.get(pk=pk)
      comment_form = CommentForm()
      context = {
          'article': article,
          'comment_form': comment_form,
      }
      return render(request, 'articles/detail.html', context)
  ```

- **detail page 에 댓글 작성 form 추가**

  ```html
  <!-- articles/detail.html -->
  
  {% extends 'base.html' %}
  
  {% block content %}
    ...
    <a href="{% url 'articles:index' %}">back</a>
    <hr>
    <form action="" method="POST">
      {% csrf_token %}
      {{ comment_form }}
      <input type="submit">
    </form>
  {% endblock %}
  ```

- 그런데 외래키를 직접 입력한다. Comment

  ```python
  class CommentForm(forms.ModelForm):
  
      class Meta:
          model = Comment
          exclude = ['article',]
  ```

```python
# articles/urls.py

path('<int:pk>/comments/', views.comments_create, name='comments_create'),

```

<br>

**save method**

>  https://docs.djangoproject.com/en/3.0/topics/forms/modelforms/#the-save-method

- 우리가 `models.py` 에서 `Comment` 클래스를 정의 했을 때 필드(컬럼)을 `article`과`content` 2개를 설정했다. 데이터 무결성의 원칙에 따라 해당 필드는 레코드가 없는 NULL 일 상태 일 수 없기 때문에 값을 넣어 주어야 한다.

  ```python
  # articles/views.py
  
  @require_POST
  def comments_create(request, pk):
      article = Article.objects.get(pk=pk)
      comment_form = CommentForm(request.POST)
      if comment_form.is_valid():
          comment = comment_form.save(commit=False)
          comment.article = article
          comment.save()
          return redirect('articles:detail', article.pk)
      context = {
          'comment_form': comment_form,
          'article': article,
      }
      return render(request, 'articles/detail.html', context)
  ```

  ```html
  <form action="{% url 'articles:comments_create' article.pk %}" method="POST">
    {% csrf_token %}
    {{ comment_form }}
    <input type="submit">
  </form>
  ```

  - 댓글을 작성한 후 admin 페이지 혹은 sqlite 확장에서 확인

<br>

### READ

- 특정 article에 있는 모든 댓글을 가져온 후 template 으로 전달한다.

  ```python
  # articles/views.py
  
  from .models import Article, Comment
  
  def detail(request, pk):
      article = Article.objects.get(pk=pk)
      comment_form = CommentForm()
      comments = article.comment_set.all()
      context = {
          'article': article,
          'comment_form': comment_form,
          'comments': comments,
      }
      return render(request, 'articles/detail.html', context)
  ```

  ```html
  <!-- articles/detail.html -->
  
  {% extends 'base.html' %}
  
  {% block content %}
    ...
    <a href="{% url 'articles:index' %}">back</a>
    <hr>
    <h4>댓글 목록</h4>
    {% for comment in comments %}
      <li>{{ comment.content }}</li>
    {% endfor %}
    <hr>
    ...
  {% endblock %}
  ```

<br>

### DELETE

```python
# articles/urls.py

path('<int:article_pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete'),
```

```python
# articles/views.py

@require_POST
def comments_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('articles:detail', article_pk)
```

```django
<!-- articles/detail.html -->

{% extends 'base.html' %}

{% block content %}
  ...
  <h4>댓글 목록</h4>
  {% for comment in comments %}
    <li>
      {{ comment.content }}
      <form action="{% url 'articles:comments_delete' article.pk comment.pk %}" method="POST" class="d-inline">
        {% csrf_token %}
        <input type="submit" value="DELETE">
      </form>
    </li>
  {% endfor %}
  <hr>
	...
{% endblock %}
```

- comment update 페이지의 경우 JS를 사용하지 않으면 흐름이 부자연스럽다.

<br>

------

<br>

## Comment 관련 추가 사항

### 댓글 개수 출력

```python
# 1. {{ comments|length }}

# 2. {{ article.comment_set.all|length }}

# 3. {{ comments.count }} 는 count 메서드가 호출되면서 comment 모델 쿼리를 한번 더 보내기 때문에 매우 작은 속도차이지만 더 느려진다. (단, 상황에 따라 달라질 수 있다.)
```

```django
<!-- articles/detail.html -->

<h4>댓글 목록</h4>
{% if comments|length %}
  <p><b>{{ comments|length }}개의 댓글이 있습니다.</b></p>
{% endif %}
```

<br>

### 댓글이 없는 경우 다른 문장 출력

- `for empty` 활용

  ```html
  <!-- articles/detail.html -->
  
  {% for comment in comments %}
    <li>
      {{ comment.content }}
      <form action="{% url 'articles:comments_delete' article.pk comment.pk %}" method="POST" class="d-inline">
        {% csrf_token %}
        <button>댓글삭제</button>
      </form>
    </li>
  {% empty %}
    <p><b>댓글이 없어요..</b></p>
  {% endfor %}
  ```

<br>

---

<br>

## get_object_or_404

> 주어진 모델 관리자에서 get()을 호출하지만 모델의 DoesNotExist 예외 대신 Http404를 발생시킴
>
> https://docs.djangoproject.com/en/3.1/topics/http/shortcuts/#get-object-or-404

- 시작하기 전에 pk 값이 없는 detail 페이지로 요청을 보내 보자. (예를 들면, url 에 `articles/100/` 이라고 입력 해보자. 존재하지 않는 pk로!) 에러 메시지가 500(Internal Server Error)으로 나온다.

- 500 에러는 내부 서버의 오류로 '서버에 오류가 발생하여 요청을 수행할 수 없다'는 의미다.  이 경우 사용자의 요청이 잘못된 경우이기 때문에 404 에러인 '서버에 존재하지 않는 페이지에 대한 요청이 있을 경우' 에 해당하는 에러로 바꿔서 처리해주는 것이 더 바람직하다.

- `get_object_or_404` 는 해당 객체가 있다면 `objects.get(pk=article_pk)` 을 실행하고 없으면 **ObjectDoesNotExist 예외**가 아닌 **Http404(HttpResponseNotFound)** 를 raise 한다.

  ```python
  from django.shortcuts import get_object_or_404
  
  article = get_object_or_404(Article, pk=pk)
  comment = get_object_or_404(Comment, pk=comment_pk)
  ```

- 모두 변경해보자

  ```python
  def detail(request, pk):
      article = get_object_or_404(Article, pk=pk)
  
  @require_http_methods(['GET', 'POST'])
  def update(request, pk):
      article = get_object_or_404(Article, pk=pk)
  
  @require_POST
  def delete(request, pk):
      article = get_object_or_404(Article, pk=pk)
  
  @require_POST
  def comments_create(request, pk):
      article = get_object_or_404(Article, pk=pk)
  
  @require_POST
  def comments_delete(request, article_pk, comment_pk):
      comment = get_object_or_404(Comment, pk=comment_pk)
  ```

- 변경 후에 다시 `articles/100` 으로 요청을 보내보면 이제는 Page not found 라는 404 에러가 발생한다.

- 응용

  ```python
  get_object_or_404(Article, title__startswith='A', pk=1)
  ```

------

[TOC]

# 07_django_many_to_one

> 2020.09.23

<br>

## User - Article

### User model 대체

> https://docs.djangoproject.com/en/3.1/topics/auth/customizing/#auth-custom-user

- 일부 프로젝트에서는 Django의 내장 유저 모델이 제공하는 인증 요구사항이 적절하지 않을 수 있다.
- 사용자 지정 모델을 참조하는 AUTH_USER_MODEL 설정 값을 변경해 기본 유저 모델을 재정의(override) 할 수 있다.
- Django는 새 프로젝트를 시작하는 경우 기본 사용자 모델이 충분하더라도 커스텀 유저 모델을 설정하는 것을 강력하게 권장한다.
- 커스텀 유저 모델은 기본 사용자 모델과 동일하게 작동하지만 필요한 경우 나중에 맞춤 설정할 수 있기 때문이다.
- **단, 프로젝트의 첫 migrate를 실행하기 전에 완료해야 한다.**

<br>

**AUTH_USER_MODEL**

> https://docs.djangoproject.com/en/3.1/ref/settings/#auth-user-model

- User를 나타내는데 사용하는 모델
- 기본 값은 ‘auth.User’
- 주의 사항
  - 프로젝트를 진행하는 동안 (즉, 프로젝트에 의존하는 모델을 만들고 마이그레이션 한 후) 설정은 변경할 수 없다. (변경하려면 큰 노력이 필요)
  - 프로젝트 시작 시 설정하기 위한 것이고 커스텀 User로 대체하기를 참고해서 설정한다.

<br>

**`AbstractUser` vs `AbstractBaseUser`**

> [https://github.com/django/django/blob/415e899dc46c2f8d667ff11d3e54eff759eaded4/django/contrib/auth/base_user.py#L47](https://github.com/django/django/blob/415e899dc46c2f8d667ff11d3e54eff759eaded4/django/contrib/auth/base_user.py)
> [https://github.com/django/django/blob/415e899dc46c2f8d667ff11d3e54eff759eaded4/django/contrib/auth/models.py#L290](https://github.com/django/django/blob/415e899dc46c2f8d667ff11d3e54eff759eaded4/django/contrib/auth/models.py)

<img width="250" alt="Picture1" src="https://user-images.githubusercontent.com/18046097/93996761-98afc300-fdcd-11ea-9ae7-3d8f90f102a8.png">

- `AbstractBaseUser`
  - password 와 last_login 만 기본적으로 제공
  - 자유도가 높지만 다르 필요한 필드는 모두 작성해야 함
- `AbstractUser`
  - 관리자 권한과 함께 완전한 기능을 갖춘 사용자 모델을 구현하는 기본 클래스

```python
# accounts/models.py

from django.conf import settings
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass
```

```python
# settings.py

AUTH_USER_MODEL = 'accounts.User'
```

- Django는 맞춤 모델을 참조하는 `AUTH_USER_MODEL` 설정 값을 제공함으로써 기본 사용자 모델을 오버라이드하도록 할 수 있다.

```python
# accounts/admin.py

from django.contrib.auth.admin import UserAdmin
from .models import User

admin.site.register(User, UserAdmin)
```

<br>

**데이터베이스 초기화 후 마이그레이션**

1. migrations 파일 삭제
2. db.sqlite3 삭제
3. migrations

<br>

### Custom user and built-in auth forms

> https://docs.djangoproject.com/ko/3.1/topics/auth/customizing/#custom-users-and-the-built-in-auth-forms

- 유저모델 대체 후 회원가입 시 에러 발생

- AbstractBaseUser의 모든 subclass와 호환되는 forms

  - AuthenticationForm, SetPasswordForm, PasswordChangeForm, AdminPasswordChangeForm

- User와 연결되어 있어서 커스텀 유저 모델을 사용하려면 다시 작성하거나 확장해야 하는 forms (ModelForm)

- UserCreationForm, UserChangeForm

- `UserCreateForm()` 을 재정의 해보자.

  ```python
  # accounts/forms.py
  
  from django.contrib.auth.forms import UserChangeForm, UserCreationForm
  
  
  class CustomUserCreationForm(UserCreationForm):
  
      class Meta(UserCreationForm.Meta):
          model = get_user_model()
          fields = UserCreationForm.Meta.fields + ('email',)
  ```

  ```python
  # accounts/views.py
  
  from .forms import CustomUserChangeForm, CustomUserCreationForm
  
  
  def signup(request):
      if request.user.is_authenticated:
          return redirect('articles:index')
  
      if request.method == 'POST':
          form = CustomUserCreationForm(request.POST)
          if form.is_valid():
              user = form.save()
              auth_login(request, user)
              return redirect('articles:index')
      else:
          form = CustomUserCreationForm()
      context = {
          'form': form,
      }
      return render(request, 'accounts/signup.html', context)
  ```

<br>

### User model 참조

`get_user_model()`

- User를 직접 참조하는 대신 django.contrib.auth.get_user_model()을 사용하여 사용자 모델을 참조해야 함
- 이 메서드는 현재 활성 사용자 모델 (지정된 경우 사용자 지정 사용자 모델, 그렇지 않은 경우 User)을 반환합니다.

<br>

`settings.AUTH_USER_MODEL`

- 유저 모델에 대한 외래 키 또는 다 대다 관계를 정의 할 때 사용

- 즉, models.py 에서 유저 모델을 참조할 때 사용

- Article 모델에 외래키 설정 후 마이그레이션 작업 진행

  ```python
  # articles/models.py
  
  from django.conf import settings
  
  class Article(models.Model):
  	  ...
      user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  ```

  ```bash
  $ python manage.py makemigrations
  
  # 첫번째 상황(null 값이 허용되지 않는 user_id 가 아무 값도 없이 article 에 추가되려 하기 때문)
  $ python manage.py makemigrations
  You are trying to add a non-nullable field 'user' to article without a default; we can't do that (the database needs something to populate existing rows).
  Please select a fix:
   1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
   2) Quit, and let me add a default in models.py
  Select an option: # 1 입력하고 enter
  
  # 두번째 상황(그럼 기존 article 의 user_id 로 어떤 데이터를 넣을건지 물어봄, 현재 admin 의 pk 값인 1을 넣자)
  Please enter the default value now, as valid Python
  The datetime and django.utils.timezone modules are available, so you can do e.g. timezone.now
  Type 'exit' to exit this prompt
  >>> # 1 입력하고 enter (그럼 현재 작성된 모든 글은 admin 이 작성한 것으로 됨)
  ```

  ```bash
  $ python manage.py migrate
  ```

<br>

- 게시글을 작성하려 하면 user 를 선택 해야하는 불필요한 field 가 노출된다. 제목과 내용만 입력하도록 필드를 설정해야한다.

  ```python
  # articles/forms.py
  
  class ArticleForm(forms.ModelForm):
      ...
      class Meta:
          model = Article
          fields = ['title', 'content',]
  ```

  - 글을 작성해보면 create 시에 유저 정보가 저장되지 않기 때문에 다음과 같은 에러가 발생한다.
    - `NOT NULL constraint failed: articles_article.user_id`

<br>

### CREATE 로직 수정

- 그리고 `request.user` 라는 현재 요청의 유저 객체를 `article.user` 에 할당한다.

  ```python
  # articles/views.py
  
  @login_required
  @require_http_methods(['GET', 'POST'])
  def create(request):
      if request.method == 'POST':
          form = ArticleForm(request.POST)
          if form.is_valid():
              article = form.save(commit=False)
              article.user = request.user
              article.save()
              return redirect('articles:detail', article.pk)
  ```

- 게시글을 작성한 user가 누구인지 보기 위해 `index.html` 수정

  ```django
  <!-- articles/index.html -->
  
  {% extends 'base.html' %}
  
  {% block content %}
    ...
    {% for article in articles %}
      <p><b>작성자 : {{ article.user }}</b></p>
      <p>글 번호 : {{ article.pk }}</p>
      <p>글 제목 : {{ article.title }}</p>
      <p>글 내용 : {{ article.content }}</p>
      <a href="{% url 'articles:detail' article.pk %}">DETAIL</a>
      <hr>
    {% endfor %}
  {% endblock %}
  ```

<br>

### UPDATE, DELETE 로직 수정

- 사용자가 자신의 글만 **수정/삭제** 할 수 있도록 내부(update/delete) 로직 수정

  ```python
  # articles/views.py
  
  from django.contrib.auth.decorators import login_required
  
  @login_required
  @require_http_methods(['GET', 'POST'])
  def update(request, pk):
      article = get_object_or_404(Article, pk=pk)
      if request.user == article.user:
          if request.method == 'POST':
              form = ArticleForm(request.POST, instance=article)
              if form.is_valid():
                  form.save()
                  return redirect('articles:detail', article.pk)
          else:
              form = ArticleForm(instance=article)
      else:
          return redirect('articles:index')
      context = {
          'form': form,
      }
      return render(request, 'articles/update.html', context)
  ```

  ```python
  # articles/views.py
  
  @require_POST
  def delete(request, pk):
      if request.user.is_authenticated:
          article = get_object_or_404(Article, pk=pk)
          if request.user == article.user:
              article.delete()
              return redirect('articles:index')
      return redirect('articles:detail', article.pk)
  ```

- 해당 게시글의 게시자가 아니라면, 삭제/수정 버튼을 보이지 않게하자.

  ```django
  <!-- articles/detail.html -->
  
  {% extends 'articles/base.html' %}
  {% block content %}
    ...
    {% if request.user == article.user %}
      <a href="{% url 'articles:update' article.pk %}">UPDATE</a><br>
      <form action="{% url 'articles:delete' article.pk %}" method="POST">
        {% csrf_token %}
        <input type="submit" value="DELETE">
      </form>
    {% endif %}
  ...
  ```

<br>

---

<br>

## User - Comment

```python
# articles/models.py

class Comment(models.Model):
		article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
		...
```

```bash
$ python manage.py makemigrations

# 첫번째 상황(null 값이 허용되지 않는 user_id 가 아무 값도 없이 comment 에 추가되려 하기 때문)
You are trying to add a non-nullable field 'user' to comment without a default; we can't do that (the database needs something to populate existing rows).
Please select a fix:
 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
 2) Quit, and let me add a default in models.py
Select an option: # 1 입력하고 enter

# 두번째 상황(그럼 기존 comment 의 user_id 로 뭘 넣을건지 물어봄, 현재 admin 인 1을 넣자)
Please enter the default value now, as valid Python
The datetime and django.utils.timezone modules are available, so you can do e.g. timezone.now
Type 'exit' to exit this prompt
>>> # 1 입력하고 enter (모든 댓글의 작성자를 admin 으로 하게 됨)

Migrations for 'articles':
  articles/migrations/0005_comment_user.py
    - Add field user to comment
```

```bash
$ python manage.py migrate
```

<br>

### CREATE & READ

- 해당 view 함수를 요청한 유저의 정보를 넣고나서 저장한다. (로그인 사용자만 작성하도록)

  ```python
  # articles/views.py
  
  @require_POST
  def comments_create(request, pk):
      if request.user.is_authenticated:
          article = get_object_or_404(Article, pk=pk)
          comment_form = CommentForm(request.POST)
          if comment_form.is_valid():
              comment = comment_form.save(commit=False)
              comment.article = article
              comment.user = request.user
              comment.save()
              return redirect('articles:detail', article.pk)
      return redirect('accounts:login')
  ```

- 비로그인 유저는 댓글 작성 form 을 볼 수 없도록 한다.

  ```django
  <!-- articles/detail.html -->
  
  {% extends 'articles/base.html' %}
  {% block content %}
    ...
  <hr>
    {% if request.user.is_authenticated %}
      <form action="{% url 'articles:comments_create' article.pk %}" method="POST">
        {% csrf_token %}
        {{ comment_form }}
        <input type="submit">
      </form>
    {% else %}
      <a href="{% url 'accounts:login' %}">[댓글을 작성하려면 로그인하세요.]</a>
    {% endif %}
    <a href="{% url 'articles:index' %}">[back]</a>
  {% endblock %}
  ```

  ```python
  # articles/forms.py
  
  class CommentForm(forms.ModelForm):
  
      class Meta:
          model = Comment
          exclude = ['article', 'user',]
  ```

- 댓글 작성자 출력

  ```django
  <!-- articles/detail.html -->
  
  {{ comment.user }} - {{ comment.content }}
  ```

<br>

### DELETE

- 본인이 작성한 댓글만 삭제할 수 있어야 한다.

  ```python
  # articles/views.py
  
  @require_POST
  def comments_delete(request, article_pk, comment_pk):
      if request.user.is_authenticated:
          comment = get_object_or_404(Comment, pk=comment_pk)
          if request.user == comment.user:
              comment.delete()
      return redirect('articles:detail', article_pk)
  ```

  ```django
  <!-- articles/detail.html -->
  
  {% extends 'articles/base.html' %}
  {% block content %}
    ...
    <h4>댓글 목록</h4>
    {% if comments|length %}
      <p><b>{{ comments|length }}개의 댓글이 있습니다.</b></p>
    {% endif %}
    {% for comment in comments %}
      <div>
        {{ comment.user }} - {{ comment.content }}
        {% if request.user == comment.user %}
          <form action="{% url 'articles:comments_delete' article.pk comment.pk %}" method="POST" class="d-inline">
            {% csrf_token %}
            <input type="submit" value="DELETE">
          </form>
        {% endif %}
      </div>
    {% empty %}
      <p><b>댓글이 없어요..</b></p>
    {% endfor %}
    <hr>
    ...
  {% endblock %}
  ```




[TOC]

# 08_django_many_to_many

> 2020.09.28

<br>

## Many-to-many relationship

> https://docs.djangoproject.com/en/3.1/ref/models/fields/#manytomanyfield

<br>

------

<br>

## ManyToManyField

> https://docs.djangoproject.com/en/3.1/ref/models/fields/#manytomanyfield

<br>

**개념**

- M:N(이하 다대다) 관계를 나타내기 위해 사용하는 필드

- 하나의 필수 위치인자(다대다 관계로 설정할 모델 클래스)가 필요하다.

<br>

**데이터베이스에서의 표현**

- django는 다대다 관계를 나타내는 중개 조인 테이블(intermediary join table)을 만든다.
- 테이블 이름은 ManyToManyField의 이름과 이를 포함하는 모델의 이름을 조합하여 생성한다.
- `db_table` 옵션을 사용하여 조인 테이블의 이름을 변경할 수도 있다.

![image-20201004025914535](과목평가(DB) 대비.assets/image-20201004025914535-1602460063180.png)

<br>

**Arguments**

- `related_name`

  - ForeignKey의 related_name과 동일

  ![image-20201004025402544](과목평가(DB) 대비.assets/image-20201004025402544-1602460063181.png)

- `through`

  - django는 다대다 관계를 관리하는 중개 테이블을 자동으로 생성한다.
  - 하지만, 중간 테이블을 직접 지정하려면 through 옵션을 사용하여 중개 테이블을 나타내는 Django 모델을 지정할 수 있다.
  - 일반적으로 추가 데이터를 다대다 관계와 연결하려는 경우에 사용한다.

  ![image-20201004025015431](과목평가(DB) 대비.assets/image-20201004025015431-1602460063181.png)

- `symmetrical`

  - ManyToManyField가 동일한 모델을 가리키는 정의에서만 사용

  ```python
  from django.db import models
  
  class Person(models.Model):
      friends = models.ManyToManyField('self')
  ```

  - 예시처럼 동일한 모델을 가리키는 정의의 경우 django는 Person 클래스에 person_set 매니저를 추가 하지 않는다.
  - 대신 대칭적(`symmetrical`)이라고 간주하며, source 인스턴스가 target 인스턴스를 참조하면 target 인스턴스도 source 인스턴스를 참조하게 된다.
  - 즉, 내가 당신의 친구라면 당신도 내 친구가 된다.
  - self와의 관계에서 대칭을 원하지 않는 경우 `symmetrical=False`로 설정한다.

- related_query_name

- limit_choices_to

- through_fields

- db_table



<br>

**중개 테이블 필드 생성 규칙**

1. 소스(source model) 및 대상(target model) 모델이 다른 경우
   - id
   - `<containing_model>_id`
   - `<other_model>_id`
2. ManyToManyField가 동일한 모델을 가리키는 경우
   - id
   - `from_<model>_id`
   - `to_<model>_id`

<br>

------

<br>

## LIKE

> `user` 는 여러 `article` 에 **좋아요를 누를 수 있고**
>
> `article` 은 여러 `user` 로부터 **좋아요를 받을 수 있다.**

<br>

**model 설정**

```python
# articles/models.py

class Article(models.Model):
    ...
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
```

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

<br>

- **현 상황에서는 `related_name` 작성이 필수**
  - M:N 관계 설정 시에 `related_name` 이 없다면 자동으로 `.article_set` 매니저를 사용할 수 있도록 하는 데 이 매니저는 이미 이전 1:N(User:Article) 관계에서 사용 중인 매니저이다.
  - user가 작성한 글들(`user.article_set`)과 user가 좋아요를 누른 글(`user.article_set`)을 django는 구분할 수 없게 된다.
    - `user.article_set.all()` : 유저가 작성한 게시글 전부
    - `user.like_articles.all()` : 유저가 좋아요를 누른 게시글 전부

<br>

- 여기서 `articles_article_like_users` 는 두 테이블 간의 M:N 관계를 나타내주는 중개 모델(Intermediary join table)이 된다.

  ```sql
  $ sqlite3 db.sqlite3
  
  sqlite> .tables
  articles_article             auth_user_groups
  articles_article_like_users  auth_user_user_permissions
  articles_comment             django_admin_log
  auth_group                   django_content_type
  auth_group_permissions       django_migrations
  auth_permission              django_session
  auth_user
  ```

<br>

- **이제 사용 가능한 ORM 명령어는 다음과 같다.**
  - `article.user` : 게시글을 작성한 유저 - 1:N
  - `article.like_users` : 게시글을 좋아요한 유저 - M:N
  - `user.article_set`: 유저가 작성한 게시글들 → 역참조 - 1:N
  - `user.like_articles`: 유저가 좋아요한 게시글들 → 역참조 - M:N

<br>

**view & urls**

> https://docs.djangoproject.com/en/3.1/ref/models/querysets/#filter
>
> https://docs.djangoproject.com/en/3.1/ref/models/querysets/#django.db.models.query.QuerySet.exists

- `filter()` 
  - 조건에 맞는 여러 행을 출력한다. (조건에만 맞는다면 전부 가져온다.)
- `exists()`
  - 최소한 하나의 레코드가 존재하는지 여부를 확인하여 알려 준다. 

- `.get` 이 아닌 `.filter` 를 사용하는 이유 → 데이터가 없는 경우의 오류 여부
  - `.get()` 은 유일한 값을 꺼낼 때 사용한다.(ex. pk) 유일한 값을 꺼낸다는 것은 해당 데이터가 존재하지 않는 경우가 없다는 뜻이다. 값이 없으면 에러(DoesNoetExist error) 가 발생하기 때문에 무조건 존재하는 값에 접근할 때 사용한다.
  - `.filter()` 의 경우 조건에 맞는 여러 개의 데이터를 가져온다. 이때 데이터가 1개도 없어도 빈 쿼리셋을 반환한다. (몇 개인지 보장할 수 없을 때)

```python
# articles/urls.py

urlpatterns = [
		...
		path('<int:article_pk>/like/', views.like, name='like'),
]
```

```python
# articles/views.py

@require_POST
def like(request, article_pk):
    # 인증된 사용자만 가능
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=article_pk)
        user = request.user

        if article.like_users.filter(pk=user.pk).exists():
        # if user in article.like_users.all():
        	# 좋아요 취소
            article.like_users.remove(user)
        else:
            # 좋아요
            article.like_users.add(user)
        return redirect('articles:index')
    return redirect('accounts:login')
```

<br>

- **font awesome 을 활용한 like 버튼 만들기**

> https://fontawesome.com/

```html
<!-- articles/base.html -->

<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <script src="<https://kit.fontawesome.com/dacaadcd9c.js>" crossorigin="anonymous"></script>
...
```

```django
<!-- articles/index.html -->

{% extends 'base.html' %}

{% block content %}
  <h1 class="text-center">Articles</h1>
  ...
    <p>글 내용: {{ article.content }}</p>
    <form action="{% url 'articles:like' article.pk %}" method="POST" class="d-inline">
      {% csrf_token %}
      {% if user in article.like_users.all %}
        <button class="btn btn-link">
          <i class="fas fa-heart fa-lg" style="color:crimson;"></i>
        </button>
      {% else %}
        <button class="btn btn-link">
          <i class="fas fa-heart fa-lg" style="color:black;"></i>
        </button>
      {% endif %}
    </form>
    {{ article.like_users.all|length }} 명이 이 글을 좋아합니다.<br>
    <a href="{% url 'articles:detail' article.pk %}">[detail]</a>
    <hr>
  {% endfor %}
{% endblock %}
```

<br>

## Profile

```python
# accounts/urls.py

path('<username>/', views.profile, name='profile'),
```

```python
# accounts/views.py

def profile(request, username):
    person = get_object_or_404(get_user_model(), username=username)
    context = {
        'person': person,
    }
    return render(request, 'accounts/profile.html', context)
```

```django
<!-- accounts/profile.html -->

{% extends 'base.html' %}

{% block content %}
<h1 class="text-center">{{ person.username }}님의 프로필</h1>

<!-- bootstrap 점보트론 들어갈 곳 -->

<hr>

<h2>{{ person.username }}가 쓴 글</h2>
{% for article in person.article_set.all %}
  <div>{{ article.title }}</div>
{% endfor %}

<hr>

<h2>{{ person.username }}가 쓴 댓글</h2>
{% for comment in person.comment_set.all %}
  <div>{{ comment.content }}</div>
{% endfor %}

<hr>

<h2>{{ person.username }}가 좋아요한 글</h2> 
{% for article in person.like_articles.all %}
  <div>{{ article.title }}</div>
{% endfor %}

<hr>

<a href="{% url 'articles:index' %}">back</a>
{% endblock  %}
```

```django
<!-- base.html -->

<a href="{% url 'accounts:profile' request.user.username %}">내프로필</a>
```

```django
<!-- articles/index.html -->

<p><b>작성자 : <a href="{% url 'accounts:profile' article.user.username %}">{{ article.user }}</a></b></p>
```



<br>

## FOLLOW

**models**

```python
# accounts/models.py

from django.conf import settings

class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
```

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

<br>

**Follow 구현**

> 자기자신은 follow 하면 안된다.

```python
# accounts/urls.py

urlpatterns = [
    ...,
    path('follow/<int:user_pk>/', views.follow, name='follow'),
]
```

```python
# accounts/views.py

@require_POST
def follow(request, user_pk):
    you = get_object_or_404(get_user_model(), pk=user_pk)
    me = request.user

    if me != you:
        # if user in person.followers.all():
        if you.followers.filter(pk=me.pk).exists():
            you.followers.remove(me)
        else:
            you.followers.add(me)
    return redirect('accounts:profile', you.username)

```

<br>

**templates**

- 템플릿 분할

```django
<!-- accounts/_follow.html -->

<!-- 팔로워 수 / 팔로잉 수 -->
<div class="jumbotron">
  <p class="lead">
    팔로워 수 : {{ person.followers.all|length }} / 팔로잉 수 : {{ person.followings.all|length }} 
  </p>
  <!-- 팔로우 버튼 / 언팔로우 버튼 -->
  {% if request.user != person %}
    <form action="{% url 'accounts:follow' person.pk %}" method="POST">
      {% csrf_token %}
      {% if request.user in person.followers.all %}
      <button class="btn btn-secondary">Unfollow</button>
      {% else %}
      <button class="btn btn-primary">Follow</button>
      {% endif %}
    </form>
  {% endif %}
</div>
```

```django
<!-- articles/detail.html -->

{% extends 'base.html' %}

{% block content %}
<h1 class="text-center">{{ person.username }}님의 프로필</h1>

{% include 'accounts/_follow.html' %} # 템플릿 분할

<hr>
```

<br>

**`with` template tag**

>  https://docs.djangoproject.com/en/3.1/ref/templates/builtins/#with

- 더 간단한 이름으로 복잡한 변수를 저장한다.
- 주로 데이터베이스에 중복으로 여러번 엑세스 할 때 유용하게 사용한다.
- 변수는 `{% with %}` and `{% endwith %}` 사이에서만 사용 가능하다.

```django
<!-- accounts/_follow.html -->

<!-- 팔로워 수 / 팔로잉 수 -->
<div class="jumbotron">
  {% with followers=person.followers.all followings=person.followings.all %}
    <p class="lead">
      팔로워 수 : {{ followers|length }} / 팔로잉 수 : {{ followings|length }} 
    </p>
    <!-- 팔로우 버튼 / 언팔로우 버튼 -->
    {% if request.user != person %}
      <form action="{% url 'accounts:follow' person.pk %}" method="POST">
        {% csrf_token %}
        {% if request.user in followers %}
          <button class="btn btn-secondary">Unfollow</button>
        {% else %}
          <button class="btn btn-primary">Follow</button>
        {% endif %}
      </form>
    {% endif %}
  {% endwith %}
</div>
```

------

 

