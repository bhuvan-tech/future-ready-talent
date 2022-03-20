<?php 
    session_start();
    $db_hostname="sql304.epizy.com";
    $db_username="epiz_30407137";
    $db_password="sGVedl0Ei1xuk";
    $db_name="epiz_30407137_hack";

    $email=$_POST['email'];
    $password=$_POST['password'];
    $conn=mysqli_connect($db_hostname,$db_username,$db_password,$db_name);
    if(!$conn){
        echo "Connection could not happen: ".mysqli_connect_error();
        exit;
    }
    echo $email;
    mysqli_close($conn);
?>