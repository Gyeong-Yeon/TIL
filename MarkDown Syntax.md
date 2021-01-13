## 마크다운(MarkDown)

일반 텍스트형식 구문을 사용하는 마크업언어의 일종이다.



# 1. Heading

> '#' 코드를 이용하여 간단하게 heading 입력 가능. 총 6가지의 heading 스타일 지원
>
> `#(1~6개) 문구`

# Heading 1

## Heading 2

### Heading 3

#### Heading 4

#### Heading 5

###### Heading 6



# 2. Line

> 언더스코어 세번(`___`) / 스코어 세번(`---`) 입력하면 라인 추가

___

---



# 3. Text attributes

1) 볼드체 `**` : **bold**

2) 이탈릭 `*` : *italic*

3) strikethrough `~~` : ~~strikethrough~~



# 4. Quote

> `>`



# 5. Bullet List

> '*' 코드나 '-' 코드를 문구 앞에 달아주면 목록으로 변환
>
> `*/- 문구`

* Apple

- Lemon



# 6. Numbered List

> 문구 앞에 숫자를 붙여서 숫자 목록으로 변환

1. first
2. second
3. third



# 7. Link

> []안에 원하는 문구를 작성하고, ()안에 원하는 링크를 작성하면 클릭 가능
>
> `[]()`

Click [here](https://github.com/Gyeong-Yeon)



# 8. Image

> ![]안에 이비지에 대한 설명을 작성하고, ()안에 이미지의 링크를 추가하면 이미지 출력
>
> `![]()`

- 절대경로 : C:\users\ 같은형식
- 상대경로 : 현재 위리치를 기준으로 접근하는 형태
- 로컬에 이미지파일을 저장한 경우 절대 경로가 아닌 상대 경로를 사용하여 이미지를 저장
  - 현재 보는 마크다운.md 파일이 c:\users\Edwin에 있다고 가정
  - 예시 : ./download => 절대경로 c:\users\Edwin\download
    - `.` : 현재폴더
    - `..` : 상위폴더 ../download =>절대경로 `c:/users/download`

- word처럼 이미지가 파일내부에 저장되는 형태가 아닌점을 주의

※ HTML img 태그를 이용하여 width를 지정해주면, 이미지 사이즈 일관성있게 조정 가능



# 9. Table

> `|` (파이프)사이에 컬럼을 작성하고 enter를 입력
>
> ex) '|'+Header+'|'+Description+'|'

| Header | Description |
| ------ | ----------- |
|        |             |



# 10. Code

1) 인라인 형태 : `(백틱) 키를 이용해서 해당하는 코드 감싸주면, 인라인 형태로 포맷

To print message in the console, use `console.log('your message')` and ...

2) 코드 블럭 : `(백틱) 키를 세 번 누르고 해당하는 언어 표현 후, 코드 작성

```javascript
console.log('your message')
```



# 11.  Task Lists

> `- [ ] task list item`

- [ ] this is a incomplete item : [ ]

- [x] this is a complete item : [x]



