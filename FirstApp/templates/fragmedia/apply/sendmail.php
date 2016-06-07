<?php
  $name = $_REQUEST['name'] ;
  $email = $_REQUEST['email'] ;
  $position = $_REQUEST['position'] ;
  $resume = $_REQUEST['resume'] ;
  $referred = $_REQUEST['referred'] ;


  mail( "jlmassey05@gmail.com", "Contact Form Results",
    "Name: $name
	Email: $email 
	Posistion: $position  
	Referal: $referred  
	Portfolio : $resume
	");
  header( "Location: http://xpcpro.frihost.org/fragmedia/apply/thanksforapply.php" );
?>

