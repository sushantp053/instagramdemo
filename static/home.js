function likePost(postId) {
  console.log(postId);
  h = document.getElementById(postId);
  console.log(h);
  
  h.src = "/static/images/heart.png";
}
