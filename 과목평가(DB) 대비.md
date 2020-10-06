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
  - 칼럼 : 고유한 데이터 형식이 지정되는 열
  - 레코드 : 단일 구조 데이터 항목을 가리키는 행
  - 기본키 : 각 행의 고유 값
  - 테이블 : 열과 행의 모델을 사용해 조직된 데이터 요소들의 집합
  - 스키마 : RDB 에서 구조와 제약조건을 전반적으로 기술한 명세서
- 장점
  - 만들기도 쉽고, 확장이 용이하다.



### Sqlite

- `rowid` : PRIMARY KEY 속성을 가지는 컬럼을 작성하지 않으면 자동으로 생성되는 필드이다.
  - INTERGER 속성
  - 64비트가 최대 값 2^64
  - 사용자가 직접 수정 불가
  - autoincrease 설정을 적용하지 않음
    - 적용하려면 따로 컬럼을 정의해줘야 함
- `.table`, `.schema`, ..... (dot command) SQL X (시험에 나올법 함)

### SQL

- `;` 까지 하나의 문장으로 판단한다.

- 소문자로 작성해도 동작이 된다.

  - 소문자로 작성하게 되면 가독성이 떨어진다.

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

  - ALTER (수정)

    ```SQL
    ALTER TABLE 테이블명
    ADD 컬럼명 데이터타입 [제약조건];
    ```

  - DROP (삭제)

    ```SQL
    DROP TABLE 테이블명;
    ```

  - TRUNCATE (테이블 초기화) : SQLite 에서는 존재하지 않음

- DML

  - DB에 저장된 레코드를 생성하거나 저장된 레코드를 조회, 수정, 삭제

  - SELECT (데이터 조회)

    - DISTICT : 중복된 값을 없앰

      - `SELECT DISTICT director FROM movie;`

    - 산술 연산 검색

      - `SELECT money * 100 FROM movie;`

    - 조건 검색

      - 기본 비교 연산자 사용 가능 (>, <, !=, ...)

      - `IN`, `BETWEEN`

        - `SELECT age IN (18, 19, 20) FROM people`
        - `SELECT * FROM people WHERE age BETWEEN 20 AND 30;`

      - AND, OR

      - LIKE

        - 와일드 카드
        - `%` : 0 이상
        - `_` : 1개

      - ORDER BY : 정렬 (ASC / DESC)

      - GROUP BY

        - 특정 속성의 튜플을 모아 그룹을 지을 수 있다.
        - AS 로 컬럼명을 지을 수 있음
        - `HAVING` 특정 조건을 추가할 수 있다.

      - **JOIN**

        - 두 개 이상의 테이블을 연결해서 하나의 테이블처럼 만드는 것

        - 분산된 데이터를 하나로 묶어서 쿼리할 수 있다.

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

      - 서브쿼리 (시험에 안나올 것 같지만, 데이터 분석 쪽에 관심있으면 해야 함.)

        - SELECT 안에 SELECT 를 내포하고 있는 형태

        - 상위 SELECT 보다 먼저 수행

          ```SQL
          -- SELECT 에 사용 (스칼라 서브쿼리) 결과는 하나만 출력되어야 함.
                  SELECT CD_PLANT,NM_PLANT,(SELECT AVG(UM) FROM TABLE_ITEM) AS UM
                  FROM TABLE_PLANT;
                  
          -- FROM 에 사용 (인라인 뷰) 서브쿼리에서 조회된 값을 테이블 처럼 활용 가능.
                  SELECT title, author, reg_date
                  FROM (
                      SELECT * FROM board WHERE CREATE_AT <= '2020-10-30'
                  )
                  ORDER BY reg_date DESC;
                  
          
          
          
          -- WHERE에 사용
                  Select CD_PLANT
                  FROM TABLE_PLANT
                  WHERE CD_PLANT IN (SELECT CD_PLANT FROM  TABLE_PLANT WHERE PLANT ='1000' AND COMPANY = '0327');
          ```

  - INSERT (데이터 생성)

    ```SQL
    INSERT INTO 테이블 [(속성 리스트)]
    VALUES (속성 값들..) [,(속성 값들 2), (3), ...];
    ```

    - 속성 리스트를 생략 가능하며, 생략한 경우는 테이블을 정의할 때 속성의 순서대로 VALUES 절의 속성 값을 적어줘야 함
    - rowid 일 때는 속성리스트를 생략해도 id 를 입력하지 않아도 되는데
      - 따로 id 를 정의했을 때는 id 를 넣어줘야 한다.

  - UPDATE (데이터 수정)

    ```SQL
    UPDATE 테이블명
    SET 컬럼명=수정값, 컬럼명2=수정값2
    [WHERE 조건]
    ```

    - WHERE 이 없으면 모든 레코드를 수정

  - DELETE (데이터 삭제)

    ```sql
    DELETE FROM 테이블명
    [WHERE 조건]
    ```

    - WHERE 이 없으면 모든 레코드를 삭제

- DCL

  - DB 사용자에게 특정 권한을 수여 / 회수
  - GRANT (권한 수여)
  - REVOKE (권한 회수)

- (TCL)

  - COMMIT (트랜젝션 작업이 완료되었음을 알려줌)
  - SAVEPOINT
  - ROLLBACK (트랜젝션 작업 중 이상이 생겼을 때 원래 상태로 복구)

----------------------

### ORM

- 모든 레코드 조회

  `Board.objects.all()`

- 레코드 생성

  - 3가지 방법

    ```python
    board = Board() # 인스턴스 생성
    board.title = '제목'
    board.content = '내용'
    board.save()
    ```

    ```python
    board = Board(title='제목', content='내용')
    board.save()
    ```

    ```python
    board = Board.objects.create(title='제목', content='내용')
    ```

- 레코드 조회

  - `.get(조건)` : 찾는 값이 1개만 있을 때
  - `.filter(조건)` : 값이 있던 없던 QuerySet 으로 리턴

- 레코드 삭제

  - `delete()`



- 특정 조건에 따른 ORM 작성

  - 전체 인원 수 `.count()`

  - 컬럼에 조건을 주는 `.filter`

    - queryset field lookup (MDN 꼭 체크 해보기!!!!)

  - Q object

    - 조건을 캡슐화

    - And 표현은 ,  로 되는데 OR 표현은 Q object

      ```python
      Board.objects.filter(Q(age__lte=20) | ~Q(last_name='PARK'))
      ```

      - `~` NOT 을 표현

  - 특정 컬럼만 보고 싶을 때

    - `.values(보고싶은 컬럼명, ...)`

- 정렬

  - `order_by`
    - 컬럼명 앞 `-` 부호로 오름/내림 차순(`-`)
    - `'?'` : 랜덤하게 정렬 (매우 느림)

- LIMIT, OFFSET

  - LIMIT : 갯수 제한(슬라이싱으로 표현) [:10]
  - OFFSET : 특정 인덱스 (인덱싱, 슬라이싱으로도 표현) [2:12]



- aggregation (집계)
  - 집계 함수 : Avg, Sum, Min, Max, Count, .....
  - aggregate : 계산 후 딕셔너리로 그 값을 반환
  - annotate : 계산 후 컬럼을 추가해서 그 값을 나타냄