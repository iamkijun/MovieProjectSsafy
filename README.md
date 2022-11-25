# MVTI PROJECT
- MVTI라는 명칭으로 MBTI 맞춤별 영화를 추천하는 프로젝트입니다.

# 프로젝트 기간
- 2022.11.16(수) - 2022.11.25(금)

# 팀원 및 역할

- 김호준 : 회원가입, 로그인, 영화 리스트, 영화 상세 정보, 영화 랜덤 추천, 리뷰 및 댓글 작성

- 이기준 : 전반 CSS, 검색 기능, MVTI 페이지

# 기술 스택
- Front-end
    - Vue
- Back-end
    - Django Rest Famework

# 핵심 기능
- 회원가입, 로그인

- 영화 정보
    - 400개 이상의 영화 데이터
    - 로그인 된 사용자만 서비스 이용 가능

- 추천 알고리즘
    - 랜덤 알고리즘
    - 회원 MBTI에 맞춘 추천 시스템

- 커뮤니티
    - 영화별 코멘트 생성
    - 자유게시판 리뷰 작성
    - 리뷰 코멘트 생성

# Installation
- Back
```
python -m venv venv

source venv/Scripts/activate

pip install -r requirements.txt

python manage.py makemigrations

python manage.py migrate

python manage.py loaddata movies.josn

python manage.py runserver
```

- Front
```
npm install

npm run serve
```

# 기획 단계

![Figma](https://user-images.githubusercontent.com/104968672/203873438-8c70e417-c890-450b-965f-93c8513f2be5.PNG)

![ERD](https://user-images.githubusercontent.com/104968672/203873448-95d3db71-531c-45dd-a318-658ba196c73a.png)

    - ※ (프로젝트 진행하며 수정됨)

# Vue 프로젝트 구조
- accounts
    - 회원가입, 로그인

- articles
    - 리뷰 생성, 댓글 작성
- movies
    - 영화 리스트
    - 영화 상세 정보
    - 추천 영화 서비스

# 로그인 필수

![gurard_service](https://user-images.githubusercontent.com/104968672/203872729-c1d59ac4-e02c-4362-bfa7-054169b6c31c.png)

# 회원가입

![Signup](https://user-images.githubusercontent.com/104968672/203872550-6bb916de-66dd-45e2-82c5-89789b12af45.png)

# 로그인

![Login](https://user-images.githubusercontent.com/104968672/203872605-fb7f64af-b363-45f6-978e-bf8731e6824f.png)

# Index

![index](https://user-images.githubusercontent.com/104968672/203872626-41e9e66d-2ce1-4e59-a153-6ec91161e5a1.png)

# 영화 정보 & 댓글

![Detail](https://user-images.githubusercontent.com/104968672/203872645-60d7240d-6be1-4d19-a98b-027a41619a09.png)

![Movie_Comment](https://user-images.githubusercontent.com/104968672/203872686-f2062564-b678-45fc-8946-13623024ef56.png)

# 영화 추천

![Recommend_Movies](https://user-images.githubusercontent.com/104968672/203872755-6d8c2c82-0690-47cb-8d61-f451cc77dd58.png)

![Recommend_Movies2](https://user-images.githubusercontent.com/104968672/203872761-97dec19e-5855-45ea-9d5c-0ecfd56ca6b4.png)

# 리뷰 작성 & 댓글

![articles](https://user-images.githubusercontent.com/104968672/203872844-2ae2d85f-0bb3-4dbb-9f2a-572a6e31b11d.png)

![article_check](https://user-images.githubusercontent.com/104968672/203872852-7b165543-1e2a-46cf-a1dc-6eaa3dbf5cb3.png)

![Review_Detail](https://user-images.githubusercontent.com/104968672/203872864-a05a6904-ee24-4d2d-bcc9-b3f8c0b20417.png)

# MVTI 서비스

![MVTI](https://user-images.githubusercontent.com/104968672/203873151-310a48b5-ec56-4854-bd25-53d6fee688dc.png)

### 16개의 지문
![지문](https://user-images.githubusercontent.com/104968672/203873171-3bd9b889-9d0a-4a1f-a6e7-449e8ababd66.png)

![지문](https://user-images.githubusercontent.com/104968672/203873182-1f7e4598-2230-4cdc-b45f-bd538ffd4b6e.png)

### 맞춤 영화 추천

![마지막](https://user-images.githubusercontent.com/104968672/203873237-a4689fb0-599f-461b-a15b-4c6bbc9256c5.png)

### 카카오톡 공유하기

![공유하기](https://user-images.githubusercontent.com/104968672/203873259-e3635402-31ed-4b26-8024-0cb23180117b.png)

### 배포

![사진](https://user-images.githubusercontent.com/104968672/203874302-e7eaf9d6-228b-4604-8f73-0a1efd9999ca.png)