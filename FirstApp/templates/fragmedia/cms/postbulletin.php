<?php

require'config/db_config.php';
$query = @mysql_query('SELECT id, heading, author, date, email, bulletin FROM predections ORDER BY id asc');

if(!$query) {
	exit ( '<p>Error Performing Request: ' . mysql_error() . '</p>');
}
?>


<?php

 while ($row = mysql_fetch_array($query))
{

	$newsheading = $row['heading'];
	$newsemail = $row['email'];
	$newsauthor = $row['author'];
	$newsbulletin = $row['bulletin'];
	$date = $row['date'];

?>
  <tr>
	<td>
	  <?php echo '' . $date . '';?>
	</td>
	  <td>
		<b><?php echo '' . $newsheading . '';?></b>
	  </td>
	  <td>
	  <a href="mailto:<?php echo '' . $newsemail . ''; ?>" ><i><?php echo'' . $newsauthor . ''; ?></a>  </i>
	  </td>
	  <td>
	 <i> <?php echo '' . $newsbulletin . ''; ?>  </i>
	  </td>
				</tr>
<?php
	}
?>
	</tr>
	</table>