<?php 
  require_once('common.php');
    
  $lzw = new LZW();
  $link = connect();
  //$p = rand(0,1);
  $p = 1;
  if (empty($_SESSION['occured_id'])){
    $_SESSION['occured_id'] = -1;
  } 
      
  if($p == 0) {
    $result = query($link, 'SELECT id,lat,lon FROM points WHERE fake=1 ORDER BY RAND() LIMIT 1;');
    while ($line = mysqli_fetch_array($result, MYSQLI_ASSOC)) {
      echo base64_encode(gzencode($line['lat'].','.$line['lon'].','.$line['id'].',1'));      
    }
  }
  else {    
    $query = 'SELECT id,lat,lon,landmark_id,address_id FROM points WHERE fake IS NULL AND id NOT IN ('. $_SESSION['occured_id'] .') ORDER BY RAND() LIMIT 1;';
    $result = query($query);
    while ($line = mysqli_fetch_array($result, MYSQLI_ASSOC)) {
      echo base64_encode(gzencode($line['lat'].','.$line['lon'].','.$line['id'].',0,'.$line['landmark_id'].','.$line['address_id']));
      
      if ($_SESSION['occured_id'] == -1){
        $_SESSION['occured_id'] = $line['id'];
        $_SESSION['count'] = 0;
      } else {
        $_SESSION['occured_id'] .= "," . $line['id'];
        $_SESSION['count']++;
        if ($_SESSION['count']==$NUM_QUESTION) unset($_SESSION['occured_id']);
      }
      
    }    
    
  }
?>
