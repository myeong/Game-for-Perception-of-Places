<div id="helper">
<h3>Choose the best option describing this photo: </h3>
<br>

<?php 
require_once('common.php');

$options = array();  /* for final options */
$values = explode(',', $_GET["values"]); /* 0: latitude, 1: longitude, 2: point_id, 3: fake, 4: landmark_id, 5: address_id */

connect();

/* landmark correct answer */
$qr = 'SELECT ons_label, name FROM landmarks WHERE ons_label="' . $values[4] . '";';
$result = query($qr);
$row = mysql_fetch_array($result);
$options[0] = '<div class="opt"><input type="radio" name="q1" value="'. $row[0] .'"> ' . $row[1] . '</div>';

/* address correct answer */
$qr = 'SELECT tfl_id, name FROM address WHERE tfl_id=' . $values[5] . ';';
$result = query($qr);
$row = mysql_fetch_array($result);
$options[1] = '<div class="opt"><input type="radio" name="q1" value="'. $row[0] .'"> ' . $row[1] . '</div>';

/* landmark wrong answers */
$qr = 'SELECT ons_label, name FROM landmarks WHERE ons_label!="' . $values[4] . '" ORDER BY RAND() LIMIT 2;';
$result = query($qr);
$i = 2;
while ($row = mysql_fetch_array($result, MYSQL_NUM)) {
	 $options[$i] = '<div class="opt"><input type="radio" name="q1" value="'. $row[0] .'"> ' . $row[1] . '</div>';
	 $i++;
}

/* address wrong answers */
$qr = 'SELECT tfl_id, name FROM address WHERE tfl_id!=' . $values[5] . ' ORDER BY RAND() LIMIT 2;';
$result = query($qr);
$i = 4;
while ($row = mysql_fetch_array($result, MYSQL_NUM)) {
	$options[$i] = '<div class="opt"><input type="radio" name="q1" value="'. $row[0] .'"> ' . $row[1] . '</div>';
	$i++;
}

if (!shuffle($options)) {
	echo ("Shuffle failed!");
}	

?>
<form name='options' method='post'>
	<div id='answer-input'>		
				<?php
				$k=0; 
				while(isset($options[$k])){
					print($options[$k]);
					$k++;
				}
				
				?>
				<!--  <div class='opt'><input type="radio" name="q1" value="dn"> Don't know </div> -->
	</div>
</form>
<br>
<input id="type" value="familiarity" type="hidden" />
<input type="button" id="submit" class="btn primary" value="Submit" />


</div>