## Language_Coder

### 508:출력 - 자가진단8

```python
print("%10s%10s%10s" % ("item","count","price"))
print("%10s%10d%10d" % ("pen",20,100))
print("%10s%10d%10d" % ("note",5,95))
print("%10s%10d%10d" % ("eraser",110,97))

# 정렬과 공백
# >>> "%10s" % "hi" 
# '        hi' -> 전체 길이가 10개인 문자열 공간에서 오른쪽 정렬
# 반대쪽인 왼쪽 정렬은 %-10s
```

**문자열 포맷 코드**

| 코드 |           설명           |
| ---- | :----------------------: |
| %s   |      문자열(String)      |
| %c   |   문자 1개(character)    |
| %d   |      정수(Integer)       |
| %f   | 부동소수(floating-point) |
| %o   |          8진수           |
| %x   |          16진수          |
| %%   | Literal % (문자 % 자체)  |
