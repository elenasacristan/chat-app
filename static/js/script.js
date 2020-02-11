$(document).ready(function() {
  $("#action_menu_btn").click(function() {
    $(".action_menu").toggle();
  });

  var objDiv = document.getElementById("msg_card_body");

  $("#submit").click(function() {
    objDiv.scrollTop = objDiv.scrollHeight;
  });
});
