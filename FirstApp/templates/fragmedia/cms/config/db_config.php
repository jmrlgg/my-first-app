<?php

$db_host = 'localhost';
$db_user = 'fragmedia';
$db_password = 'fragmedia';
$db_name = 'fragmedia';

$conn = mysql_connect($db_host, $db_user) or die(mysql_error());


if (!$conn) {
	exit('<p>Unable to connect to server at this time!</p>') or die(mysql_error());
}
if (!mysql_select_db($db_name)) {
	exit('<p>Unable to connect to Database at this time!</p>') or die(mysql_error());
}

?>
