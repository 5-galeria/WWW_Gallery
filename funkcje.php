<!DOCTYPE html>
<html>
<head>
   <title>
     run
   </title>
  </head>
 <body>
 
	<script>
$(document).ready(function(){

  console.log("hello2");
   
 
});
</script>
   <form method="post">

    <input type="submit" value="GO" name="GO">
   </form>
 </body>
</html>

<?php

		shell_exec("python detectFaces.py");
		echo"success";
	
?>
