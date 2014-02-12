<?php
require_once('common.php');
connect();

$points_id = mysql_real_escape_string($_GET['point_id']);
$answer = $_GET['answer'];

# Insert answer into DB
$userinfo = getIDCookie();
$users_id = $userinfo['id'];
$q  = "INSERT INTO answers (points_id, users_id, correctness, familiarity_answer) VALUES ($points_id, $users_id, 0, $answer)";
$result = mysql_query($q);
if (!$result) {
  die('Query Failed: ' . mysql_error());
}

?>
