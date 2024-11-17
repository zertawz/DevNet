<?php
function initMysqlConnection(){
    $pdo = new PDO('mysql:host=127.0.0.1;dbname=devices', "root", "cpelyon123");
    return $pdo;
}

function getDevices($pdo){
    $query = $pdo->query("select * from devices");
    return $query;
}

$pdo = initMysqlConnection();
$devices = getDevices($pdo);

foreach ($devices as $row) {
    echo "-------------------------------------\n";
    echo "device name : ".$row['device_name']."<br/>\n";
    echo "device ip : ".$row['device_ip']."<br/>\n";
    echo "device vendor : ".$row['device_vendor']."<br/>\n";
}
?>
