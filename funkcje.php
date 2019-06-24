<!DOCTYPE html>
<html>
<head>
   <title>
     run
   </title>
  </head>
 <body>
 

   <form method="post">

    <input type="submit" value="GO" name="GO">
   </form>
 </body>
</html>

<?php
	if(isset($_POST['GO']))
	{
		shell_exec("python mkdir.py");
		echo"success";
	}
?>