<?php
	if(isset($_GET['getmail'])) { // when you clicked on 'get mail' check if there is new mail and display the attachment
		shell_exec("sudo /home/pi/python_files/mails/getmail.py > /dev/null &"); // run the 'get mail' script and redirect output to /dev/null so the page loads directly and doesn't wait until the execution of the python script is finished
		$success = "<div class='alert alert-success' role='alert'><strong>E-Mails werden abgerufen...</strong><hr>This can take a little while. When there's a new image, it will be displayed.</div>";
	}
?>

<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1"> 

    <!-- Bootstrap CSS -->
    <link href="bootstrap.min.css" rel="stylesheet">

    <title>Picture frame</title>
	<style>
		.card:hover {
			    background-color: #f8f9fa!important;
		}
	</style>
  </head>
  <body>
    <div class="container" style="padding:20px;">
	    <h1>Picture frame</h1>
		<?php if(isset($success)){echo $success;} ?>
		<div class="card-group" style="max-width:25rem;">
		<div class="card table-hover">
		  <img src="pictures.png" class="card-img-top mx-auto" style="max-width:100px; margin:5px;">
		  <div class="card-body">
		      <h5 class="card-title"><a href="selectimage.php" class="stretched-link" style="text-decoration:none; color:black;">Show picture</a></h5>
		    <p class="card-text">Select and display already saved images.</p>
		  </div>
		</div>
		
		<div class="card table-hover">
		  <img src="mailpicture.png" class="card-img-top mx-auto" style="max-width:100px; margin:5px;">
		  <div class="card-body">
		      <h5 class="card-title"><a href="?getmail" class="stretched-link" style="text-decoration:none; color:black;">Get mail</a></h5>
		    <p class="card-text">Get mail and display the new picture.</p>
		  </div>
		</div>
	</div>
		
		<!-- this part is not on github yet -->
	<hr> 
	<p><a onclick="document.getElementById('wifilinkarea').style.display='block'"><span style="text-decoration:underline; cursor: pointer;">show further configuration</span> ⬇️</a>
		<div id="wifilinkarea" style="display:none;">
			
	<div class="card-group" style="max-width:25rem;">
		<div class="card table-hover">
		  <img src="wifi.png" class="card-img-top mx-auto" style="max-width:100px; margin:5px;">
		  <div class="card-body">
		      <h5 class="card-title"><a href="network.php" class="stretched-link" style="text-decoration:none; color:black;">Internet connection</a></h5>
		    <p class="card-text">Connect to WIFI network.</p>
		  </div>
		</div>
	</div>
			
		</div>
	</div>

  </body>
</html>
