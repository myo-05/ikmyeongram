// detail_post.html

// 삭제 버튼 클릭시 확인 문구 출력 -> 원하시면 다른 버튼들에도 활용할 수 있습니다.
function confirmDeletePost(id) {
    if (confirm("진짜 지울꺼에오!?")) {
      window.location.href = "/api/sns/post/" + id + "/delete/";
    }
  }

  function confirmDeleteComment(id,comment_id) {
    if (confirm("진짜 지울꺼에오!?")) {
      window.location.href = "/api/sns/post/" + id + "/comment/" + comment_id + "/delete/";
    }
  }

  function validation(){
    let comment = document.getElementById("comment").value;

    if (comment === ""){
      alert ("빈칸발견! 강냉이가 날아가고 싶으신가요?");
      return false;
    }
  }

// new_post.html, signup.html

/* 썸네일 미리보기 함수 */
function setThumbnail(event) {
    var reader = new FileReader();

    reader.onload = function (event) {
      var img = document.createElement("img");
      img.setAttribute("src", event.target.result);

      // 썸네일 크기 조절
      img.style.width = "200px"; // 너비 200px로 설정
      img.style.height = "auto"; // 높이 자동 설정
      document
        .querySelector("div#image_container")
        .appendChild(img);
    };

    reader.readAsDataURL(event.target.files[0]);
  }

  function validation(){
    let post_title = document.getElementById("post_title").value;
    let post_content = document.getElementById("post_content").value;

    if (post_title === "" || post_content === ""){
      alert ("빈칸발견! 강냉이가 날아가고 싶으신가요?");
      return false;
    }
  }

