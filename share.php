<?php 
require_once('common.php');
if(isset($_COOKIE['userinfo'])) {
  $userinfo = unserialize(base64_decode($_COOKIE["userinfo"]));
}
?>
<form id="user-form">
<div class="modal-body">
<?php
$score = $_GET['s'];
echo "<p>Congratulations! You scored $score points</p>";
?>
<a href="
https://twitter.com/intent/tweet?text=<?php echo urlencode("My score at #UrbanOpticonCP was $score! Test your knowledge of #CollegePark at $BASE_URL");?>"
class="btn"
>
<img src="images/tweet.png" class="icon"/>
Tweet it!
</a>
<a href="
https://www.facebook.com/dialog/feed?app_id=629627080407136&
link=<?php echo $BASE_URL;?>&
picture=http://urban.myeonglee.com/images/generic.jpg&
name=<?php echo urlencode("My score is $score at UrbanOpticonCP");?>&
caption=<?php echo urlencode("How well do you know College Park?");?>&
description=<?php echo urlencode("My score at DoUKnowCollegePark was $score! Think you can beat me?");?>&
redirect_uri=http://urban.myeonglee.com/
"
target="_blank"
class="btn">
<img src="images/facebook.png" class="icon"/>
Share on Facebook</a>

  <?php   
    $us = getIDCookie();
    $users_id = $us['id']; 
    session_destroy();
   ?>
<p>Would you participate in a short survey? It will take less than 10 minutes, and you will contribute to improve people’s understanding of importance 
of cultural background in designing information systems and online communities. Also, you will be better aware of your cultural behaviors through this survey.
 Thank you so much! </p>

<div class="clearfix">
  <div class="input">
    <a href="https://umdsurvey.umd.edu/SE/?SID=SV_3az5pycIzKvEUjb&userid=<?php echo $users_id;?>" target="_blank" class="btn btn-success">Take a Survey!</a>
  </div>
</div>

<!-- 
<div class="modal-footer">
<input type="submit" id="submit-user" class="btn primary" value="Ok" />
</div>
-->
</form>
