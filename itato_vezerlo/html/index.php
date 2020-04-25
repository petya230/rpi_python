<!DOCTYPE html>
<head>
<meta charset="UTF-8">
<title>Itató szabályozás</title>
</head>
<html>
<body>
    <meta charset="UTF-8">
    <FORM name="funkcio" method="post" action="valaszt.php">
        <Input type='Radio' Name='funkcio' value='automatikus'> Automatikus <br>
        <Input type='Radio' Name='funkcio' value='leallit'> Leállít<br>
        <Input type='Radio' Name='funkcio' value='megy'> Folyamatos mukodes<br>
        <P>
            <Input type="Submit" Name="Submit1" VALUE="Küld">
    </FORM>
    <div>Jelenlegi mód:
        <?php
$line = fgets(fopen("valasz.txt", 'r'));
echo $line;
?>
    </div>
    
    <div> <br> 
    <?php
$sor = utf8_encode(fgets(fopen("vissza.txt", 'r')));
$visszajel = explode(";", $sor);

echo "1. itató állapota: ", $visszajel[0];
echo "<br>2. itató állapota: ", $visszajel[1];
echo "<br>3. itató állapota: ", $visszajel[2];
header("Refresh:5");
?>
</div>
</body>
</html>
