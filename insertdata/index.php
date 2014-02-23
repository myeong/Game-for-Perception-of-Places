<html>
<head>
<title>Insert GeoData</title>
</head>
<?php
require_once('../common.php');
connect();

/* address id */
$addr_query = "SELECT MAX(tfl_id) FROM address";
$result = query($addr_query);

while ($line = mysql_fetch_row($result)) {
  $address_id = $line[0];  
}
$address_id++;

/* landmark id */
$land_query = "SELECT MAX(ons_label) FROM landmarks";
$result = query($land_query);
while ($line = mysql_fetch_row($result)) {
  $land_id = $line[0];
}
$land_id++;


?>

<body>
<h1>Insert geo-data to be used in the quiz game</h1>
<br><br>
<form name='insertform' method='post' action='insertdata.php'>
	<div id='geo-input'>		
	  Latitude: <input id="latitude" name="latitude" type="text" /> 
	  Longitude: <input id="longitude" name="longitude" type="text" />		 
	</div>	
	<div id='landmark-info'>
	  <input id="land_id" name="land_id" type="hidden" value="<?php echo $land_id?>"/><br>
	  Landmark name: <input id="land_name" name="land_name" type="text" size="50" /><br>
	</div>
	<div id='address-info'>
	  <input id="addr_id" name="addr_id" type="hidden" value="<?php echo $address_id?>" /><br>
	  Address name: <input id="addr_name" name="addr_name" type="text" size="50" /><br>
	</div>
	<br>
	Fake <input name="fake" type="radio" value="1">
	Not Fake <input name="fake" type="radio" value="NULL" checked="true">
	  
	</div>
	
	<br><br>

    <button type="submit" id="submitdata" class="btn primary" value="Submit">Submit</button>
</form>




</body>
</html>