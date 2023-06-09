익명이그램
======
![image](https://user-images.githubusercontent.com/120750451/232473884-19e9a2d1-c350-46c2-8a37-83600dc5a52f.png)

배포
------
> 배포 완료되면 주소를 추가합니다.
  
Stacks
------
<img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white">  <img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white"> <img src="https://img.shields.io/badge/html5-E34F26?style=for-the-badge&logo=html5&logoColor=white">  <img src="https://img.shields.io/badge/css-1572B6?style=for-the-badge&logo=css3&logoColor=white"> <img src="https://img.shields.io/badge/javascript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black"> 

***

익명이그램 : B-1조 뉴스피드 프로젝트
------
> 2023.04.10 ~ 2023.04.17  
  
익명이들의 수다 공감 공간!  
게시글을 작성하고, 댓글을 달며 익명력을 길러보아요! (그래요, 떠드는 겁니다! 히히)  


기능
------
### 핵심기능

1. 로그인, 회원 가입
    - 회원가입 기능
    - 로그인 기능
    - 로그아웃 기능
    
2. 게시글 CREATE - 게시글 작성 페이지 
    - 로그인한 사용자만 가능 : 프론트 - 버튼 숨기기 / 백 - 접근 제한
    - 사진 업로드 가능 : 사진이 없을 경우 Default 사진 표시

3. 게시글 READ 
    - 피드 페이지
        - 게시글 목록 썸네일, 제목, 내용(100자) : 최신 등록 순, 로그인 없이도 볼 수 있게
    - 게시글 상세 페이지
        - 게시글의 제목, 내용, 작성자(닉네임), 등록시각, 수정시각
    - 프로필 페이지
        - 내가 쓴 게시글 모아보기

4. 게시글 UPDATE
    - 로그인한 사용자이면서 글 작성자일 때만 가능 : 프론트 - 버튼 숨기기 / 백 - 접근 제한

5. 게시글 DELETE
    - 로그인한 사용자이면서 글 작성자일 때만 가능 : 프론트 - 버튼 숨기기 / 백 - 접근 제한

### 추가기능

1. 팔로우,팔로워 기능  
    - 팔로우 여부에 따라 팔로우/언팔로우 버튼
    - 프로필 페이지
        - 팔로우 목록, 팔로잉 목록 : 목록에도 사용자마다 팔로우/언팔로우 버튼 구현 
        
3. 프로필에 사진 업로드 기능  
    - 500KB 크기제한
    - 프로필 사진이 없을 경우 Default 사진 표시
    
5. 좋아요 기능
    - 게시글 상세 페이지 : 글 하단 하트 버튼 누르면 좋아요, 한 번 더 누르면 좋아요 취소
    - 프로필 페이지
        - 내가 좋아요 누른 게시글 모아보기 (내 프로필일 때만) : 북마크 역할
        
6. 댓글 기능  
    - 게시글 상세 페이지에서 로그인한 사용자만 댓글 작성 가능
    - 댓글 수정/삭제
        - 작성자일 때만 가능 : 프론트 - 버튼 숨기기 / 백 - 접근 제한

***

ERD
------
![익명이그램 (1)](https://user-images.githubusercontent.com/120750451/232480440-a81ac5be-f167-4b75-a607-c36a1ff42b13.png)

API 명세
------
[익명이그램](https://www.notion.so/9546d4e308d54daab957549a25c18af7)
