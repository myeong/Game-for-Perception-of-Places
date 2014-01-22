<div id="helper">
<h3>Choose the best option describing the photo: </h3>
<br>

<?php 
require_once('common.php');

$values = explode(',', $_GET["values"]); /* 0: latitude, 1: longitude, 2: point_id, 3: fake, 4: landmark_id, 5: address_id */
$qr = 'SELECT id, name FROM landmarks WHERE id=' . $values[4] . ';';
connect();

$result = query($qr);
echo mysql_fetch_array($result)[0]; 
	

?>
<form name='options' method='post'>
	<div id='answer-input'>		
				<input type="radio" name="q1" value="1">  <br> 
				<input type="radio" name="q1" value="2"> <br>
				<input type="radio" name="q1" value="3"> <br>
				<input type="radio" name="q1" value="4"> <br>
				<input type="radio" name="q1" value="5">  <br>
	</div>
</form>
<br>
<br>
<input id="type" value="tubes" type="hidden" />
<input type="button" id="submit" class="btn primary" value="Submit" />


</div>