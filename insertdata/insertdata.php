<?php
require_once('../common.php');
$link = connect();

$lat = $_POST['latitude'];
$long = $_POST['longitude'];
$address = $_POST['addr_name'];
$addr_id = $_POST['addr_id'];
$landmark = $_POST['land_name'];
$land_id = $_POST['land_id'];
$fake = $_POST['fake'];

/* point id */
$point_query = "SELECT MAX(id) FROM points";
$result = query($link, $point_query);

while ($line = mysqli_fetch_row($link, $result)) {
  $point_id = $line[0];
}
$point_id++;


echo "Latitude: " . $lat . "  Longitude: ". $long ." <br>";
echo "Address: " . $address . "<br>";
echo "Landmark: " . $landmark . "<br>";
echo "This is " . $fake . "<br>";

if ($fake==0){
  $query1 = "INSERT INTO address (tfl_id, name, lat, lon) VALUES('$addr_id', '$address', '$lat', '$long')";
  query($link, $query1);
  
  $query2 = "INSERT INTO landmarks (ons_label, name, lat, lon) VALUES('$land_id', '$landmark', '$lat', '$long')";
  query($link, $query2);
}

$query3 = "INSERT INTO points (id, lat, lon, fake, landmark_id, address_id) VALUES('$point_id', '$lat', '$long', $fake, '$land_id', '$addr_id')";
query($link, $query3);

?>

<br>
<a href="index.php">Back to Insert Form</a>