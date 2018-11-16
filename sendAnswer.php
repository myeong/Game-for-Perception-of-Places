<?php
require_once('common.php');
$link = connect();

function distance($lat1, $lon1, $lat2, $lon2) {
  if($lat1 == $lat2 && $lon1 == $lon2) return 0;

  $theta = $lon1 - $lon2;
  $dist = sin(deg2rad($lat1)) * sin(deg2rad($lat2)) +  cos(deg2rad($lat1)) * cos(deg2rad($lat2)) * cos(deg2rad($theta));
  $dist = acos($dist);
  $dist = rad2deg($dist);
  $miles = $dist * 60 * 1.1515;

  return ($miles * 1.609344); #Km
}

$points_id = mysqli_real_escape_string($link, $_POST['point_id']);
$answer = $_POST['answer_input'];
$tfl_answer = '';
$answer_lat = 0;
$answer_lon = 0;

# Get answer info between Landmark or Address
if (is_numeric($answer)){
	$q = "SELECT tfl_id,lat,lon FROM address WHERE tfl_id='$answer'";
	$result = query($link, $q);
	
	while ($line = mysqli_fetch_array($result, MYSQLI_ASSOC)) {
	  $tfl_answer = $line['tfl_id'];
	  $answer_lat = $line['lat'];
	  $answer_lon = $line['lon'];
	}
	
	# Insert answer into DB
	$userinfo = getIDCookie();
	$users_id = $userinfo['id'];
	$q  = "INSERT INTO answers (points_id, users_id, address_answer) VALUES ($points_id, $users_id, $tfl_answer)";
	query($link, $q);
	
	/* To get the correct answer */
	$q = "SELECT address.name,points.address_id,points.lat,points.lon FROM points JOIN address ON address.tfl_id=points.address_id WHERE id=$points_id";
} else {   
	$q = "SELECT ons_label,lat,lon FROM landmarks WHERE ons_label='$answer'";	
    $result = query($link, $q);

    while ($line = mysqli_fetch_array($result, MYSQLI_ASSOC)) {  
      $tfl_answer = $line['ons_label'];
      $answer_lat = $line['lat'];
      $answer_lon = $line['lon'];
    }
    
    # Insert answer into DB
    $userinfo = getIDCookie();
    $users_id = $userinfo['id'];
	$q  = "INSERT INTO answers (points_id, users_id, landmark_answer) VALUES ($points_id, $users_id, '$tfl_answer')";
	$result = mysqli_query($link, $q);	
	
	/* To get the correct answer */
	$q = "SELECT landmarks.name,points.landmark_id,points.lat,points.lon FROM points JOIN landmarks ON landmarks.ons_label=points.landmark_id WHERE id=$points_id";
}


# Get correct answer
$result = query($link, $q);
while ($line = mysqli_fetch_array($result, MYSQLI_ASSOC)) {
  $correct_answer = isset($line['address_id']) ? $line['address_id'] : $line['landmark_id'];
  $correct_name = $line['name'];
  $point_lat = $line['lat'];
  $point_lon = $line['lon'];
}

# Return result
if($tfl_answer==$correct_answer) {
  echo "100|success|<p><strong>100 points</strong> That's correct!</p>|$NUM_QUESTION";
} 
else {
  $d = distance($point_lat,$point_lon,$answer_lat,$answer_lon) * 200; #meters

  if($d <= 300) {
    $score = round(100/pow($d,0.05));
    $message = "<p><strong>$score points -</strong> It was in $correct_name: not quite right, but close.</p>";
  }
  else {
    if($d <= 1000)
      $score = round(75/pow($d-300,0.2));
    else $score = 0;
    $message = "<p><strong>$score points -</strong> It was in $correct_name.</p>";
  }

  echo "$score|error|$message|$NUM_QUESTION";
}
?>
