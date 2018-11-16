<?php
require_once('common.php');
$link = connect();
    
$ans = mysqli_real_escape_string($link, urldecode($_GET['q']));
$t = $_GET['t'];

if($t != 'familiarity') die('0');

if (is_numeric($ans)){
  $q = "SELECT * FROM address WHERE tfl_id='$ans'";
} else {
  $q = "SELECT * FROM landmarks WHERE ons_label='$ans'";
}

$result = query($link, $q);
while ($line = mysqli_fetch_array($result, MYSQLI_ASSOC)) {
  $answer = 'ok';
}

if($answer == '') {
  echo '0';
}
else {
  echo '1';
}

?>
