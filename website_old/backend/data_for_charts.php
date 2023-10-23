<?php
$servername = "localhost";
$db_username = "root";
$db_password = "";
$db_name = "test_data_job_market";
$conn = new mysqli($servername, $db_username, $db_password, $db_name);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}else{
    $query = "SELECT `date`, `pełny etat`, `część etatu`, `dodatkowa / tymczasowa` FROM historic_etat";
    $result = $conn->query($query);
    $etat_data = array();
    while ($row = $result->fetch_assoc()) {
        $etat_data[] = $row;
    }
    
    $query = "SELECT `date`, `praca hybrydowa`,`praca zdalna`,`praca stacjonarna`,`praca mobilna` FROM historic_work_type";
    $result = $conn->query($query);
    $work_type_data = array();
    while ($row = $result->fetch_assoc()) {
        $work_type_data[] = $row;
    }
    
    $query = "SELECT `date`, `count` FROM historic_count";
    $result = $conn->query($query);
    $count_data = array();
    while ($row = $result->fetch_assoc()) {
        $count_data[] = $row;
    }
    
    $query = "SELECT `date`, `umowa o pracę`,`kontrakt B2B`,`umowa zlecenie`,`umowa o staż / praktyki`,`umowa o dzieło`,`umowa na zastępstwo` FROM historic_kontrakt";
    $result = $conn->query($query);
    $kontrakt_data = array();
    while ($row = $result->fetch_assoc()) {
        $kontrakt_data[] = $row;
    }
    
    $query = "SELECT `date`, `Mid`,`asystent`,`Junior`,`Senior`,`ekspert`,`team manager`,`menedżer`,`praktykant / stażysta`, `dyrektor` FROM historic_management_level";
    $result = $conn->query($query);
    $management_level_data = array();
    while ($row = $result->fetch_assoc()) {
        $management_level_data[] = $row;
    }

    $query = "SELECT `date`, `technologia`, `count` FROM ( SELECT `date`, `technologia`, `count`, ROW_NUMBER() OVER (PARTITION BY `date` ORDER BY `count` DESC) AS row_num FROM historic_technologie_wymagane ) AS ranked WHERE row_num <= 20;";
    $result = $conn->query($query);
    $historic_technologie_wymagane = array();
    while ($row = $result->fetch_assoc()) {
        $historic_technologie_wymagane[] = $row;
    }

    $query = "SELECT `date`, `technologia`, `count` FROM ( SELECT `date`, `technologia`, `count`, ROW_NUMBER() OVER (PARTITION BY `date` ORDER BY `count` DESC) AS row_num FROM historic_technologie_mile_widziane ) AS ranked WHERE row_num <= 20;";
    $result = $conn->query($query);
    $historic_technologie_mile_widziane = array();
    while ($row = $result->fetch_assoc()) {
        $historic_technologie_mile_widziane[] = $row;
    }
    
    // Set the Content-Type header
    header('Content-Type: application/json');
    
    // Combine data into an associative array
    $data = [
        'historic_etat' => $etat_data,
        'historic_work_type' => $work_type_data,
        'historic_count' => $count_data,
        'historic_kontrakt' => $kontrakt_data,
        'historic_management_level' => $management_level_data,
        'historic_technologie_wymagane' => $historic_technologie_wymagane,
        'historic_technologie_mile_widziane' => $historic_technologie_mile_widziane,
    ];

    $conn->close();

    // Return the combined data as JSON
    echo json_encode($data);


/* 
    $query_dates = "SELECT DISTINCT `date` FROM historic_technologie_mile_widziane ORDER BY `date` DESC LIMIT 5";
    $result_dates = $conn->query($query_dates);
    $last_5_dates = array();
    
    while ($date_row = $result_dates->fetch_assoc()) {
        $last_5_dates[] = $date_row['date'];
    }
    
    // Use the last 5 dates in the main query
    $last_5_dates_str = implode("', '", $last_5_dates);
    $query = "SELECT `date`, `technologia`, `count` FROM historic_technologie_mile_widziane
        WHERE `date` IN ('$last_5_dates_str')
        AND (
            SELECT COUNT(*) FROM historic_technologie_mile_widziane AS sub
            WHERE sub.`date` = historic_technologie_mile_widziane.`date`
            AND sub.`count` >= historic_technologie_mile_widziane.`count`
        ) <= 20";
*/



}
?>
