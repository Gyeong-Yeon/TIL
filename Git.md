# Git, (분산)버전 관리 시스템

> 코드의 History를 관리하는 도구. 개발된 과정과 역사를 볼 수 있으며, 프로젝트의 이전 버전을 복원하고 변경 사항을 비교, 분석 및 병합도 가능



## git, DVCS(Distributed Version Control System)

차이(diff)가 무엇이고 수정 이유를 log로 남길 수 있다. 

현재 파일들을 안전한 상태로 과거 모습 그대로 복원 가능. 

.`git` : Repository 주소 정보. `.git`폴더가 위치하는 곳만 관리(상위 폴더 X). 

​			`.git`을 지우면 local DB가 날라가지만, Repository에는 남아 있음(2원 관리).



### git 공간

- working dir
  - 실제 작업공간
- staging area
  - add 명령어를 입력했을떄 임시로 저장이 되는 공간
- local repo (.git)
  - commit 명령어를 입력했을 떄 버전이 기록되는 공간



### git 작업 흐름

> Working directory(작업한 파일) - INDEX/Staging area(커밋할 목록) - HEAD(쌓인 커밋들) - GitHub

1. add : 커밋할 목록에 추가 -> local DB
2. commit : 커밋(create a snapshot) 만들기 -> local DB
3. push : 현재까지의 역사(commits)가 기록되어 있는 곳에 새로 생성한 커밋들 반영하기 -> Repository



### git 기본

1. $ git add helloworld.py : add는 git의 sub-command 중 하나
2. $ git commit -m : -m로 시작하면 보통 short name 옵션
3. $git config --global user.name "Gyeong-Yeon" : global은 전체 설정(git commit을 한 사람의 이름을 컴퓨터에 설정) - Git 설치 후 최초 1번



### git lab

1. Private
2. 수업자료(.py, .html) & EX_HW_WS(.md)



### git hub

1. 오픈소스 프로젝트 - Tensorflow

2. 개발자의 이력서 & 연습장 - TIL(.md) 매일 작성하는 버릇 들이기!!!! "잔디 심는다."

   (주의!!!!! Github는 public설정이어서 누구나 소스코드를 열람 가능. 그러므로 싸피 교육자료는 업로드 금지!!!!!!!!!!!!!! 삼성전용 gitlab에는 업로드해도 됨.)

3. Repository

   | Repository 삭제 | ![image-20200817023157412](Intro.assets/image-20200817023157412.png)![image-20200817023325837](Intro.assets/image-20200817023325837.png) |
   | --------------- | ------------------------------------------------------------ |
   | Repository 생성 | ![image-20200817023832231](Intro.assets/image-20200817023832231.png)![image-20200817024215246](Intro.assets/image-20200817024215246.png) |

4.  Profile 꾸미기

   > `Gyeong-Yeon` Repository에서 README 수정 (html tag 적용 가능)

   | stats 화면 (https://github.com/anuraghazra/github-readme-stats) | ![image-20200817154128328](Intro.assets/image-20200817154128328.png)![image-20200817154621930](Intro.assets/image-20200817154621930.png)![image-20200817155057328](Intro.assets/image-20200817155057328.png)![image-20200817155712088](Intro.assets/image-20200817155712088.png)![image-20200817161534467](Intro.assets/image-20200817161534467.png)![image-20200817161710284](Intro.assets/image-20200817161710284.png) |
   | ------------------------------------------------------------ | ------------------------------------------------------------ |
   | icon (https://github.com/MikeCodesDotNET/ColoredBadges)      | ![image-20200817225835472](Intro.assets/image-20200817225835472.png)![image-20200817231546415](Intro.assets/image-20200817231546415.png)![image-20200817231556530](Intro.assets/image-20200817231556530.png) |

   참고(https://github.com/abhisheknaiidu/awesome-github-profile-readme)

5. Blog 꾸미기



Pull Add Commit Push - PACP



### git 명령어

- `git init`
  - `.git`폴더를 만들어 주는 명령어
  - `최초 한번`만 실행한다.
- `git add`
  - 뒤에 staging area로 올리고 싶은 파일을 적어준다.
  - `. `을 입력하면 전체 파일이 추가된다.
- `git commit`
  - 버전을 생성
  - `-m` 옵션을 일반적으로 추가해준다.
- `git remote add`
  - 원격 저장소의 주소를 등록
  - origin이라는 이름을 기본값으로 사용
  - `최초 한번`만 실행한다.
- `git push`
  - 등록된 원격 저장소로 커밋 기록을 업로드









