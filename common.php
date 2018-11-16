<?php
session_start();
require('db.php');
require('ip2locationlite.class.php');
require('lzwc.php');

$BASE_URL = 'https://myeonglee.com/urban/';
//$BASE_URL = 'http://127.0.0.1/';
$NUM_QUESTION = 15;

function getID(){
  $location = getLocationCookie();
  $ip = $location['ipAddress'];
  $city = $location['cityName'];
  $country = $location['countryCode'];
  $lat = $location['latitude'];
  $lon = $location['longitude'];
  $date = new DateTime();  
  $date->setTimezone(new DateTimeZone('America/New_York'));
  $datestr = $date->format('Y-m-d H:i:s');

  $link = connect();
  $q = "INSERT INTO users (ip,ip_city,ip_country,ip_lat,ip_lon, timestamp) VALUE('$ip','$city','$country',$lat,$lon,'$datestr')";
  query($link, $q);
  $user['id'] = mysqli_insert_id($link);
  $data = base64_encode(serialize($user));
  setcookie('user', $data, time()+3600*24*30*12); //set cookie for 20 years))
  return $user;
}

function getIDCookie() {
  if(!isset($_COOKIE['user'])){
    $user = getID();
  }
  else {
    $user = unserialize(base64_decode($_COOKIE["user"]));
  }
  return $user;
}

function getIP(){
  if (!empty($_SERVER['HTTP_CLIENT_IP']))  //check ip from share internet
    $ip=$_SERVER['HTTP_CLIENT_IP'];
  elseif (!empty($_SERVER['HTTP_X_FORWARDED_FOR']))   //to check ip is pass from proxy
    $ip=$_SERVER['HTTP_X_FORWARDED_FOR'];
  else
    $ip=$_SERVER['REMOTE_ADDR'];
  
  if ($ip == '127.0.0.1' or $ip == '::1')
    return '0.0.0.0';
  else
  return $ip;
}

function getLocation(){
  $ip = getIP();
  $ipLite = new ip2location_lite;
  $ipLite->setKey('1053c5269a22275f139b3fdbd99df3e8a700fa520f2d08018d1f0cfbd2fff943');
  
  $visitorGeolocation = $ipLite->getCity($ip);
  return $visitorGeolocation;
}

function getLocationCookie(){	
  $ip = getIP();
  //Set geolocation cookie
  if(!isset($_COOKIE['geolocation'])){
    $visitorGeolocation = getLocation();
    if ($visitorGeolocation['statusCode'] == 'OK') {
      $data = base64_encode(serialize($visitorGeolocation));
      //setcookie('geolocation', $data, time()+3600*24); //set cookie for 1 day
      setcookie('geolocation', $data, time()+3600*24, false, NULL); // for local machine 
    }    
  }else{
    $visitorGeolocation = unserialize(base64_decode($_COOKIE["geolocation"]));
    if($visitorGeolocation['ipAddress'] != $ip){
      $visitorGeolocation = getLocation();
      if ($visitorGeolocation['statusCode'] == 'OK') {
        $data = base64_encode(serialize($visitorGeolocation));
        setcookie('geolocation', $data, time()+3600*24); //set cookie for 1 day
      }
    }
  }
  return $visitorGeolocation;
}

?>
