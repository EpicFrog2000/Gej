<?php
$servername = "localhost";
$db_username = "root";
$db_password = "";
$db_name = "test_data_job_market";
$conn = new mysqli($servername, $db_username, $db_password, $db_name);

function count_all_data(){
    global $conn;

    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }
    $sql = "SELECT COUNT(id) AS count FROM data";

    $result = $conn->query($sql);
    
    while ($row = $result->fetch_assoc()) {
    $count = $row['count'];
    echo "Dane z ".$count." ofert." ;
    }
}

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
    $sql = "SELECT etat, COUNT(id) AS count FROM etat 
    WHERE etat IN ('pełny etat', 'część etatu', 'dodatkowa / tymczasowa')
    GROUP BY etat ORDER  BY count DESC";

    $result = $conn->query($sql);
    
    while ($row = $result->fetch_assoc()) {
    $contractType = $row['etat'];
    $count = $row['count'];
    echo $count . " - " . $contractType . "</br>";
    }
}

function get_kontrakt_data(){
    global $conn;

    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }
    $sql = "SELECT kontrakt, COUNT(id) AS count FROM kontrakt 
    WHERE kontrakt IN ('umowa o pracę', 'kontrakt B2B', 'umowa zlecenie', 'umowa o staż / praktyki', 'umowa o dzieło', 'umowa na zastępstwo')
    GROUP BY kontrakt ORDER  BY count DESC";

    $result = $conn->query($sql);

    while ($row = $result->fetch_assoc()) {
    $contractType = $row['kontrakt'];
    $count = $row['count'];
    echo $count . " - " . $contractType . "</br>";
    }
}

function get_management_level_data(){
    global $conn;

    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }
    $sql = "SELECT management_level, COUNT(id) AS count FROM management_level 
    WHERE management_level IN ('Mid', 'asystent', 'Junior', 'Senior', 'ekspert', 'team manager','menedżer', 'praktykant / stażysta','dyrektor')
    GROUP BY management_level ORDER  BY count DESC";

    $result = $conn->query($sql);

    while ($row = $result->fetch_assoc()) {
    $contractType = $row['management_level'];
    $count = $row['count'];
    echo $count . " - " . $contractType . "</br>";
    }
}

function get_work_type_data(){
    global $conn;

    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }
    $sql = "SELECT work_type, COUNT(id) AS count FROM work_type 
    WHERE work_type IN ('praca hybrydowa', 'praca zdalna', 'praca stacjonarna', 'praca mobilna')
    GROUP BY work_type ORDER  BY count DESC";

    $result = $conn->query($sql);

    while ($row = $result->fetch_assoc()) {
    $contractType = $row['work_type'];
    $count = $row['count'];
    echo $count . " - " . $contractType . "</br>";
    }
}

function get_spec_data(){
    global $conn;

    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }
    $sql = "SELECT specjalizacja, COUNT(specjalizacja) AS count
    FROM specjalizacje
    WHERE specjalizacja IS NOT NULL AND specjalizacja != ''
    GROUP BY specjalizacja
    ORDER BY count DESC
    LIMIT 20;";

    $result = $conn->query($sql);

    while ($row = $result->fetch_assoc()) {
    $contractType = $row['specjalizacja'];
    $count = $row['count'];
    echo $count . " - " . $contractType . "</br>";
    }
}

function get_wym_tech_data(){
    global $conn;

    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }
    $sql = "SELECT technologia, COUNT(technologia) AS count
    FROM technologie_wymagane
    GROUP BY technologia
    ORDER BY count DESC
    LIMIT 20;";

    $result = $conn->query($sql);

    while ($row = $result->fetch_assoc()) {
    $contractType = $row['technologia'];
    $count = $row['count'];
    echo $count . " - " . $contractType . "</br>";
    }
}

function get_opt_tech_data(){
    global $conn;

    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }
    $sql = "SELECT technologia, COUNT(technologia) AS count
    FROM technologie_mile_widziane
    GROUP BY technologia
    ORDER BY count DESC
    LIMIT 20;";

    $result = $conn->query($sql);

    while ($row = $result->fetch_assoc()) {
    $contractType = $row['technologia'];
    $count = $row['count'];
    echo $count . " - " . $contractType . "</br>";
    }
}


?>
