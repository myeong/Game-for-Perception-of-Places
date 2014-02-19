<?php
require_once('common.php');
connect();
    
$ans = mysql_real_escape_string(urldecode($_GET['q']));
$t = $_GET['t'];

if($t != 'familiarity') die('0');

if (is_numeric($ans)){
  $q = "SELECT * FROM address WHERE id='$ans'";
} else {
  $q = "SELECT * FROM landmarks WHERE name='$ans'";
}

$result = query($q);
while ($line = mysql_fetch_array($result, MYSQL_ASSOC)) {
  $answer = 'ok';
}

if($answer == '') {
  echo '0';
}
else {
  echo '1';
}

?>
