<?php
require('common.php');

$link = connect();

// Removes % and escapes the input
$q = $_GET['q'];
$q = str_replace('%', '', $q);
$q = mysqli_real_escape_string($link, $q);
$t = $_GET['t'];

if($t != 'tubes' and $t !='boroughs') die('Heh. I see what you did there.');

if (strlen($q) > 0)
{
?>
<ul>
<?php
$max_results = 3;
$result = query($link, "SELECT name FROM $t WHERE name LIKE '$q%' LIMIT $max_results");
while ($line = mysqli_fetch_array($result, MYSQLI_ASSOC)) {
  echo '<li ';
  echo 'onclick="choice(\''.$line['name'].'\')">';
  echo $line['name'];
  echo '</li>';
}
if($t=='tubes') 
  echo '<li><a href="stations.php" target="_blank">View all stations</a></li>';
?>
</ul>
<?php
}
?>
