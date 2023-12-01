# Chatweb
    
### 1. 목표
   * DRF 습득
   * DRF(Django REST Framework)를 이용한 서버 구현
   * 회원가입, 로그인 구현

<br>

### 2. 개발 환경 및 기술
   * Visual Studio Code
   * Python
   * Django


<br>

### 3. 플로우 차트 및 DRF


<br>

<img width="769" alt="image" src="https://github.com/bardnia/Chatweb/assets/69304793/2da5dc4d-4f62-4763-bce2-258458fec453">


<br>
<br>

<img width="769" alt="image" src="https://github.com/bardnia/Chatweb/assets/69304793/135c91d8-4565-4965-9a74-3d9725afad94">


### 4. URL 구조

<br>

- accounts

| App       | Method        | URL                               | Views Class        | Note           |
|-----------|---------------|-----------------------------------|------------------- |----------------|
| accounts  | POST   | '/accounts/'                         |   -                 |회원가입  |

<br>

- blog

| App       | Method        | URL                               | Views Class        | Note           |
|-----------|---------------|-----------------------------------|------------------- |----------------|
| blog  | GET   | '/blog/'                         |   PostViewSet                 |게시글 목록 |
| blog  | POST   | '/blog/posts/'                       |   PostViewSet                 |게시글 생성  |
| blog  | GET   | '/blog/{post_id}/'                |    PostViewSet       |게시글 상세보기 |



<br>
<br>

### 5. 디렉토리 구조
```
 ┣ 📂accounts
 ┃ ┣ 📜admin.py
 ┃ ┣ 📜apps.py
 ┃ ┣ 📜models.py
 ┃ ┣ 📜permissions.py
 ┃ ┣ 📜serializers.py
 ┃ ┣ 📜tests.py
 ┃ ┣ 📜urls.py
 ┃ ┣ 📜views.py
 ┃ ┗ 📜__init__.py
 ┣ 📂blog
 ┃ ┣ 📜admin.py
 ┃ ┣ 📜apps.py
 ┃ ┣ 📜models.py
 ┃ ┣ 📜permissions.py
 ┃ ┣ 📜serializers.py
 ┃ ┣ 📜tests.py
 ┃ ┣ 📜urls.py
 ┃ ┣ 📜views.py
 ┃ ┗ 📜__init__.py
 ┣ 📂project
 ┃ ┣ 📜asgi.py
 ┃ ┣ 📜settings.py
 ┃ ┣ 📜urls.py
 ┃ ┣ 📜wsgi.py
 ┃ ┗ 📜__init__.py
```



<br>


### 6. 느낀점

- 자신의 능력에 대한 재평가
- DRF를 다룰 수 있게 된 것에 만족한다

