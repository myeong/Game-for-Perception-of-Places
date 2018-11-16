<?php
require_once('common.php');
$link = connect();

$id = mysqli_real_escape_string($link, $_POST['point_id']);

# Insert answer into DB
$q  = "UPDATE points SET reported=reported+1 WHERE id=$id";
query($link, $q);
?>
