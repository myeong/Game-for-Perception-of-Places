<div id="helper">
<h3>How much are you familiar with this place? </h3>
<br>

<?php 
require_once('common.php');

connect();

?>
<form name='familiarity_options' method='post'>
	<div id='answer-input'>	
	  <div class="left familiarity">&larr;Unfamiliar at all</div>
	  <div class="right familiarity">Very familiar&rarr;</div>	
	  <br>
	  <table class="fopt">
	    <tr>
	      <td>1</td>
	      <td>2</td>
	      <td>3</td>
	      <td>4</td>
	      <td>5</td>
	      <td>6</td>
	      <td>7</td>
	    </tr>
	    <tr>
	      <td><input type="radio" name="familiar_q1" value="1"></td>
	      <td><input type="radio" name="familiar_q1" value="2"></td>
	      <td><input type="radio" name="familiar_q1" value="3"></td>
	      <td><input type="radio" name="familiar_q1" value="4"></td>
	      <td><input type="radio" name="familiar_q1" value="5"></td>
	      <td><input type="radio" name="familiar_q1" value="6"></td>
	      <td><input type="radio" name="familiar_q1" value="7"></td>
	    </tr>
	  </table>
      <!-- 
      <div class="fopt"><input type="radio" name="familiar_q1" value="2"></div>
      <div class="fopt"><input type="radio" name="familiar_q1" value="3"></div>
      <div class="fopt"><input type="radio" name="familiar_q1" value="4"></div>
      <div class="fopt"><input type="radio" name="familiar_q1" value="5"></div>
      <div class="fopt"><input type="radio" name="familiar_q1" value="6"></div>
      <div class="fopt"><input type="radio" name="familiar_q1" value="7"></div>
      		 -->		
	</div>
</form>
<br>
<input id="type" value="familiarity" type="hidden" />
<input id="geovalues" value="<?php echo $_GET["values"];?>" type="hidden" />
<input type="button" id="submit" class="btn primary" value="Submit" />


</div>
