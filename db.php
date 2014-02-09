<?php
function connect() {
	/*
  $link = mysql_connect('mysql16.000webhost.com', 'a8068967_psymap', 'asdf123')
          or die('Could not connect: ' . mysql_error());
  mysql_select_db('a8068967_psymap') or die('Could not select database');
  */
	if (($_SERVER['SERVER_NAME']) == "localhost") {
		$link = mysql_connect('localhost', 'root', 'root')
		or die('Could not connect: ' . mysql_error());
		mysql_select_db('myeong_urban') or die('Could not select database');
	}
	else {
		$link = mysql_connect('localhost', 'myeong_drupal', 'drupal123')
		or die('Could not connect: ' . mysql_error());
		mysql_select_db('myeong_urban') or die('Could not select database');
	}	
  return $link;
}

function query($q) {
  $result = mysql_query($q) or die('Query failed: ' . mysql_error());
  return $result;
}
?>
