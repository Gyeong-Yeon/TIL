## Vue Directive

```javascript
<div id="app"></div>

<!-- vue CDN 추가 -->
<script>
    const app = new Vue({
        el: '#app', // 어떤 엘리먼트와 연결할 지 정함
        data: {
            // vue 에서 사용되는 변수들
            // 다양한 정보의 타입이 저장될 수 있다.
        },
        methods: {
            // vue 에서 사용할 함수들을 정의하는 곳
            // 메소드를 정의할 때는 화살표 함수를 사용하지 않는다. (this)
        }
    })
</script>
```

- v-html

  - innerHTML 로 할당
  - HTML 을 그대로 읽기 때문에 XSS 공격에 취약

- v-text

  - innerText 로 할당
  - {{ 머스타치 }}: 보간법 (interpolation) 과 동일한 역할

- v-if, v-if-else, v-else

  - 조건문에 따라서 해당 Tag 의 렌더링 여부를 결정
  - 아예 코드 자체가 렌더링되지 않는다.
  - v-if, v-else 를 사용할 때 사이에 어떠한 Tag 가 있으면 제대로 동작하지 않는다.

- v-show

  - v-show 의 값에 따라 css display 속성을 조절해서 화면 노출을 결정

- v-for

  - 반복문

- v-bind

  - HTML 표준 속성에 Vue 의 데이터를 연결

  - `:` (shortcut)

  - Object 형태(키-밸류)로 사용하면 value 가 true 인 경우만 바인딩된 값으로 할당 가능

    `:class = "{ 클래스 이름:false }"`

- v-model

  - 양방향 바인딩
  - 입력되어지는 태그 (Input, TextArea, Select) 사용

- v-on

  - 이벤트
  - `@` (shortcut)



- this 정리

  - obj.functionCall() => this === obj : 메소드 호출되었을 때

  - 그 외 => this === window

    ```javascript
    const myObjg = {
        myFunc: function () {
            console.log(this) // myObj
            axios.get(URL)
              .then(function () {
                console.log(this) // myObj
            }.bind(myObj))
            
            // 2. 콜백 함수에서 this를 obj로 만드는 방법
            axios.get(URL)
              .then(() => {
                console.log(this) // myObj
            })
        }
    }
    ```

    

