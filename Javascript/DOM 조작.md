JS 역사

- 회사가 많아서 파편화가 되었다.
- 이제 점점 표준화를 시키면서 안정되고 있다.



## DOM 조작

- 화면으로 표시된 HTML 을 JS 로 조작이 가능
- selector 를 이용해서 조작을 한다.
  - `querySelector` 를 이용해서 id, class, 태그를 선택해서 조작할 수 있다.
    - `getElementById` 는 수업시간에서는 사용하지 않을 예정
      - live 속성 때문에
- `dir` (선택된 엘리먼트를 가진 변수)
    - 사용할 수 있는 속성에 대한 정보를 볼 수 있다.
    - 더 자세한 내용을 알고 싶으면 mdn 문서를 이용
    - mdn + 찾고 싶은 속성
  
- 정리
  1. 선택한다.
  2. 변경한다.

----------------

## EventListener

- 이벤트

  - 브라우져에서 일어나는 일

  

- 이벤트 리스너

  - `~하면 ~한다.`

  - 특정한 이벤트가 발생하면, 할 일을 실행한다.

    `이벤트 타겟.addEventListener(이벤트 타입, 할 일)`



- preventDefault()

  - 기존에 행동하는 동작을 동작하지 않게 하는 함수

    예 ) submit

-----------------------------------

## 식별자 (identifier)

- 변수명은 식별자라고도 불림

- 규칙

  1. 반드시 **문자**, **달라($)** 또는 **밑줄(_)**로 시작해야 한다!! (숫자나, `-` 로 시작할 수 없다.)

     ```html
     const hi-hello
     ```

  2. 대소문자를 구분한다.

  3. 예약어는 사용할 수 없다. (const, function, class, .....)

- 스타일

  - 카멜케이스 (lowerCamelCase)
    - 객체, 변수, 함수
  - 파스칼케이스 (UpperCamelCase)
    - 클래스, 생성자
  - 대문자 스네이크 케이스 (UPPER_CASE)
    - 상수 : 변수나 변수의 속성이 변하지 않는 것

------------------

## Hoisting

- var 로 선언된 변수는 선언 이전에 참조할 수 있는 현상

  ```html
  console.log(name)
  var name = '홍길동'
  
  console.log(age)
  let age = 10
  ```

-------------------------

## String

- JS 에서 문자열을 표현하는 방법

  ```javascript
  const str1 = '홑 따옴표 사용'
  const str2 = "쌍 따옴표 사용"
  
  str1 + str2 // 2개의 문장을 한 문장으로 합침
  
  const str3 = "줄 바꿈
  은 허락되지 않는다."
  
  // escape squence
  const str4 = "줄 바꿈은 \n 이렇게 해야 합니다."
  
  // Template literal (ES6+) 백틱 (` : 물결표 shift 없이)
  const str5 = `안녕하세요.
  줄바꿈도 가능합니다.`
  const num = 100
  const str8 = `${num} - ${str1}`
  ```

  - 리터럴
    - 리터럴이라는 단어는 값을 프로그램 안에서 직접 지정한다 라는 의미
    - 리터럴은 값을 만드는 방법

-----------------------

## Switch

```javascript
const name = '홍길동'

switch(name) {
    case 'admin': {
        console.log('관리자 모드')
        break
    }
    case 'manager': {
        console.log('매니저 모드')
        break
    }
    default: {
        console.log(`${name}님 환영합니다.`)
    }
}
```

-------------------

## for 문

```javascript
for (let i = 0; i < 6; i++){
    console.log(i)
}

const numbers = [0, 1, 2, 3]
for (const number of numbers) {
    console.log(number)
}

const obj = {a: 'a', b: 'b'}
for (const o of obj){
    console.log(o)
} // 에러 발생 Uncaught TypeError : obj is not iterable

const obj = {a: 'apple', b: 'banana'}
for (const o in obj){
    console.log(o)
}
```

------------------------

## 화살표 함수

```javascript
const arrow = function (name) {
    return 'hello! ${name}!!'
}

// 1. function 키워드를 삭제하고 화살표를 추가한다.
const arrow = (name) => {
    return `hello! ${name}!!`
}

// 2. 매개변수가 하나일 때는 괄호를 생략할 수 있다.
const arrow = name => {
    return `hello! ${name}!!`
}

// 3. {} & return 생략 (body에 표현식이 1개인 경우)
const arrow = name => `hello! ${name}!!`


// 연습 코드
const exam = function () {
    return 'hello, world'
}

// 1
const exam = () => {
    return 'hello, world'
}

// 2 skip / 그래도 적용하고 싶다면 _ 를 사용
const exam = _ -> {
    return 'hello, world'
}

// 3
const exam = () => 'hello, world'
or
const exam = _ => 'hello,world'
```

-------------------------

## function 키워드 호이스팅

```javascript
// 선언식일 때는 동작
function add (a, b) {
    return a + b
}

// 표현식일 때는?
sub(7, 2)
const sub = function (num1, num2) {
    return num1 - num2
}

// const sub = (num1, num2) => num1 - num2
```

-------------

## 함수의 Object 축약형

```javascript
let obj = {
    name: 'ssafy',
    sayHi: function () {
        console.log('hello')
    }
};

obj.sayHi() // 'hello'

// ES6+
let obj2 = {
    name: 'ssafy',
    // 함수의 object 축약형
    sayHi () {
        console.lgo('hi!!!')
    }
}

obj2.sayHi()
```

--------------

## JSON (JavaScript Object Notation)

JavaScript Object 형태를 가지는 `문자열`

### object -> JSON (string)

```javascript
const objData = {
    coffee: 'Americano',
    icecream: 'Bravo corn'
}

const jsonData = JSON.stringify(objData)
console.log(typeof(jsonData))
```

### JSON -> object

```javascript
const objData2 = JSON.parse(jsonData)
console.log(typeof(objData2))
```

---------------------

### forEach

- exercise

  ```javascript
  // 배열 안에 있는 정보를 곱해서 그 넓이를 areas 배열에 저장
  const images = [
    { height: 10, width: 30 },
    { height: 20, width: 90 },
    { height: 54, width: 32 }
  ]
  
  const areas = []
  ```

  - 풀이 코드

    ```javascript
    images.forEach(function (img) {
        areas.push(img.height * img.width) // {height: 10, width: 30},
    })
    console.log(areas)
    ```



### map

- exercise

  ```javascript
  // 각 숫자들의 제곱근이 들어있는 새로운 배열을 만드세요.
  
  const newNumbers = [4, 9, 16]
  ```

  - 풀이 코드

    ```javascript
    const newArray = newNumbers.map(function (num) {
        return num ** 0.5
    })
    
    // const newArray2 = newNumbers.map(Math.sqrt)
    ```

    ```javascript
    const areas2 = images.map(function (img) {
        return img.height * img.width
    })
    console.log(areas2)
    ```



### filter

- example

  ```javascript
  const products = [
      { name: 'cucumber', type: 'vegetable'},
      { name: 'banana', type: 'fruit'},
      { name: 'carrot', type: 'vegetable'},
      { name: 'apple', type: 'fruit'}, 
  ]
  
  const fruits = products.filter(function (product) {
      return product.fype === 'fruit'
  })
  console.log(fruits)
  ```

  - exercise

    ```javascript
    // numbers 배열 중 50보다 큰 값들만 모은 배열 filteredNumbers 를 만드세요.
    const numbers = [15, 25, 35, 45, 55, 65, 75, 85, 95]
    
    const filteredNumbers1 = numbers.filter(function (num) {
        return num > 50
    })
    ```

--------------------

### some

```javascript
const products = [
    { name: 'cucumber', type: 'vegetable' },
    { name: 'banana', type: 'fruit' },
    { name: 'carrot', type: 'vegetable' },
    { name: 'apple', type: 'fruit' },
]

const someVegetable = products.some(function (product) {
	return product.type === 'vegetable'
})
console.log(somevegetable)

const someWater = products.some(function (product) {
	return product.type === 'water'
})
console.log(someWater)

const zeroList = []
const someZero = zeroList.some(function (zero) {
    return zero > 50
})
```

```javascript
// requests 배열에서 status가 pending인 요청이 있는지 확인하세요.
const request = [
    { url: '/photos', status: 'complete' },
    { url: '/albums', status: 'pending' },
    { url: '/users', status: 'failed' },
]
```

-------------------

### every

```javascript
// users 배열에서 모두가 submitted 인지 여부를 hasSubmitted 에 저장하세요.
const users = [
    { id: 21, submmited: true },
    { id: 33, submmited: false },
    { id: 712, submmited: true},
]

const hasSubmitted = users.every(function (user) {
    return user.submitted
})
console.log(hasSubmitted)
```

-------------------------------

### reduce

```javascript
// 주어진 baseUrl 문자열 뒤에 필수 요청 변수인 api 의 key - value 값을 key = value 의 형태로 더하여 요청 url 을 만드세요. URL 에서 요청 변수는 & 문자로 구분합니다.

const baseUrl = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?' key=API_KEY&targetDt=20200115

const api = {
  'key': 'API_KEY',
  'targetDt': '20200115'
}

const apiUrl = Object.entries(api).reduce(function (url, api) {
    return url + `${api[0]}=${api[1}&`
}, '')
console.log(apiUrl)
```

