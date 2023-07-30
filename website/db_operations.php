<?php
$servername = "localhost";
$db_username = "root";
$db_password = "";
$db_name = "test_data_job_market";
$conn = new mysqli($servername, $db_username, $db_password, $db_name);

function percent_salary(){
    global $conn;

    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }
    $sql = "SELECT (SUM(CASE WHEN salary > 0 THEN 1 ELSE 0 END) / COUNT(salary)) * 100 AS percentage FROM data;";
    $result = $conn->query($sql);
    $row = $result->fetch_assoc();
    $percentage = round($row['percentage']);
    echo $percentage . "% ofert zawiera płace";
}

function get_etat_data(){
    global $conn;

    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }
    $sql = "
    SELECT SUM(count_total) AS total_num
    FROM (
        SELECT ID,
            COUNT(*) AS count_total,
            SUM(CASE WHEN etat = 'full-time' THEN 1 ELSE 0 END) AS count_full,
            SUM(CASE WHEN etat = 'pełny-etat' THEN 1 ELSE 0 END) AS count_part
        FROM etat
        GROUP BY ID WITH ROLLUP
    ) AS subquery;
    ";
    $result = $conn->query($sql);
    $row = $result->fetch_assoc();
    $res = round($row['total_num']);
    echo $res . " total_numss      cx";
    echo "</br>";

}
?>
