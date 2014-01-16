<?php
function connect() {
	/*
  $link = mysql_connect('mysql16.000webhost.com', 'a8068967_psymap', 'asdf123')
          or die('Could not connect: ' . mysql_error());
  mysql_select_db('a8068967_psymap') or die('Could not select database');
  */
	$link = mysql_connect('localhost', 'root', 'root')
	or die('Could not connect: ' . mysql_error());
	mysql_select_db('a8068967_psymap') or die('Could not select database');
  return $link;
}

function query($q) {
  $result = mysql_query($q) or die('Query failed: ' . mysql_error());
  return $result;
}
?>
