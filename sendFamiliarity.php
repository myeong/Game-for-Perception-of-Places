<?php
require_once('common.php');
$link = connect();

$points_id = mysqli_real_escape_string($link, $_GET['point_id']);
$answer = $_GET['answer'];

# Insert answer into DB
$userinfo = getIDCookie();
$users_id = $userinfo['id'];
$q  = "INSERT INTO answers (points_id, users_id, correctness, familiarity_answer) VALUES ($points_id, $users_id, 0, $answer)";
$result = query($link, $q);
if (!$result) {
  die('Query Failed: ' . mysqli_connect_error());
}

?>
