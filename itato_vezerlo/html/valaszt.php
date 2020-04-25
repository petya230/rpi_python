<?php
$_funkcio = $_POST["funkcio"];

if($_funkcio == "automatikus")
{
    $myfile = fopen("valasz.txt", "w");
    $txt = "automatikus";
    fwrite($myfile, $txt);
    fclose($myfile);
    echo("Az itató automatikus feltöltése, addig amíg el nem éri a kívánt vízszintet!");
}
else if ($_funkcio == "leallit")
{
    $myfile = fopen("valasz.txt", "w");
    $txt = "leallitva";
    fwrite($myfile, $txt);
    fclose($myfile);
    echo("Az itató telítése leállítva!");
}
else if ($_funkcio == "megy")
{
    $myfile = fopen("valasz.txt", "w");
    $txt = "folyamatos";
    fwrite($myfile, $txt);
    fclose($myfile);
    echo("Az itató folyamatos telítése!");
}
header( "refresh:1;url=index.php" );
?>
