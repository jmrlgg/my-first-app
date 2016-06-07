<?php

require'config/db_config.php';
$query = @mysql_query('SELECT id, heading, author, date, email, bulletin FROM predections ORDER BY date desc');


?>

<table>
  <tr>

<?php

 while ($row = mysql_fetch_array($query))
{

	$newsheading = $row['heading'];
	$newsemail = $row['email'];
	$newsauthor = $row['author'];
	$newsbulletin = $row['bulletin'];
	$date = $row['date'];

?>
    <tr colspan="2"><b><?php echo '' . $newsheading . '';?></b></tr>
  </tr>
  <tr>
    <td rowspan="2">pic</td>
    <td><?php echo '' . $date . '';?> <b>||</b> <i><?php echo '' . $newsauthor . ''; ?></a></i> <b>||</b> <?php echo '' . $tags . '';?></td>
  </tr>
  <tr>
    <td><?php echo '' . $newsbulletin . ''; ?></td>
  </tr>
  <tr>
    <td colspan="2"><hr></td>
<?php
	}
?>
</tr>
</table>