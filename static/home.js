function likePost(postId) {
  console.log(postId);
  h = document.getElementById(postId);
  console.log(h);
  s = h.src;
  console.log(s);
  if (s.endsWith("heart.png")) {
    h.src = "/static/images/like.png";
  } else {
    h.src = "/static/images/heart.png";
  }
}
