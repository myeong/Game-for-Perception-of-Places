<?php
require_once('common.php');
$link = connect();

$data = base64_encode(serialize($_POST));
//setcookie('userinfo', $data, time()+3600*24*30*12); //set cookie for 20 years
setcookie('userinfo', $data, time()+3600*24*30*12, false, NULL); //for local

$username = mysqli_real_escape_string($link, $_POST['username']);
$twitter = mysqli_real_escape_string($link, $_POST['twitter']);
$email = mysqli_real_escape_string($link, $_POST['email']);
$gender = mysqli_real_escape_string($link, $_POST['gender']);
$age= mysqli_real_escape_string($link, $_POST['age']);
$postcode = mysqli_real_escape_string($link, $_POST['postcode']);
$ethnic = mysqli_real_escape_string($link, $_POST['ethnic']);
$occupation = mysqli_real_escape_string($link, $_POST['occupation']);

$user = getIDCookie();
$id = $user['id'];

# Insert answer into DB
$q  = "UPDATE users SET username='$username',twitter='$twitter',email='$email',gender='$gender',age='$age',postcode='$postcode',ethnic='$ethnic',occupation='$occupation' WHERE id=$id";
query($link, $q);

?>
