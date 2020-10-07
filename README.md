# 💻DJango

- 파이썬으로 작성된 오픈 소스 웹 프레임워크
- 모델-뷰-컨트롤러 패턴을 따르고 있다.
- URL 설계
- ORM

<br>

## 💾구동방식

<img src="https://media.vlpt.us/post-images/rosewwross/74f7df80-44c1-11ea-abd8-615fe26b63cd/image.png" style="zoom:50%;" />

👉URL Dispatcher를 통해 요청을 분석하고 적합한 view로 전달하며, view는 사용자가 요구한 데이터베이스 정보를 model에게 알려준다. 

model은 데이터베이스에 연결되어 데이터를 가져온다. 

model은 다시 view에 데이터를 전송하고, view는 template에 전달하여 최종적으로 사용자에게 전달될 수 있도록 데이터를 만든다.

<br>

---

### 📟장점

- 비교적 쉬운 언어인 python을 기반으로 두기 때문에 익히기 쉽다.
- 개발 비용을 크게 절감시킬 수 있다.

<br>

### 📟단점

- python이 객체지향프로그램이기 때문에, 객체지향프로그램에 대한 이해가 필요하다.
- 성능이 다른 웹 어플리케이션 프레임워크(Node.js 등) 보다 좋지 못하다.

<br>

---

## 💾Project & Application

#### 💽Project

 👉웹사이트를 뜻하며, 하나의 프로젝트는 하나의 웹사이트를 의미한다.

<br>

#### 💽Application

 👉의미있는 하나의 기능

<br>

---

<img src="https://mkjjo.github.io/img/posting/2019-01-05-001-djangoflow.PNG" style="zoom:33%;" />

💽**URLs**

👉분리된 뷰 함수를 작성하는 것이 각각의 리소스를 유지보수하기 훨씬 쉽다. URL mapper는 요청 URL을 기준으로 HTTP요청을 적절한 view로 보내주기 위해 사용된다.

<br>

💽**View** **(views.py)**

👉HTTP 요청을 수신하고 HTTP 응답을 반환하는 요청 처리 함수이다.

View는 Model을 통해 요청을 충족시키는데 필요한 데이터에 접근하여 template에게 응답의 서식 설정을 맡긴다.

<br>

💽**Models**

👉application의 데이터 구조를 정의하고 데이터베이스의 기록을 관리하고 query하는 방법을 제공하는 파이썬 객체이다.

<br>

💽**Templates**

👉파일의 구조나 레이아웃을 정의하고 실제 내용을 보여주는데 사용되는 플레이스홀더를 가진 텍스트 파일이다.

view는 HTML 템플릿을 이용하여 동적으로 HTML페이지(.js, .html)를 만들고 model에서 가져온 데이터로 채운다.

<br>