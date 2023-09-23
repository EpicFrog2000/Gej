<?php
$servername = "localhost";
$db_username = "root";
$db_password = "";
$db_name = "test_data_job_market";
$conn = new mysqli($servername, $db_username, $db_password, $db_name);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

function count_all_data($conn){
    $sql = "SELECT COUNT(id) AS count FROM data";

    $result = $conn->query($sql);

    if ($result === false) {
        die("Query error: " . $conn->error);
    }

    while ($row = $result->fetch_assoc()) {
        $count = $row['count'];
        echo "Na dzień dzisiejszy: ".$count." ofert" ;
    }
}

function percent_salary($conn){
    $sql = "SELECT (SUM(CASE WHEN salary > 0 THEN 1 ELSE 0 END) / COUNT(salary)) * 100 AS percentage FROM data;";

    $result = $conn->query($sql);

    if ($result === false) {
        die("Query error: " . $conn->error);
    }

    $row = $result->fetch_assoc();

    $percentage = round($row['percentage']);
    echo $percentage . "% ofert zawiera płace";
}

function get_etat_data($conn){
    $sql = "SELECT etat, COUNT(id) AS count FROM etat 
    WHERE etat IN ('pełny etat', 'część etatu', 'dodatkowa / tymczasowa')
    GROUP BY etat ORDER  BY count DESC";

    $result = $conn->query($sql);

    if ($result === false) {
        die("Query error: " . $conn->error);
    }
    
    echo "<table style='text-align: left;'>";
    while ($row = $result->fetch_assoc()) {
        $etat = $row['etat'];
        $count = $row['count'];
        echo "<tr>";
        echo "<td>".$count ."</td><td>". $etat ."</td>";
        echo "</tr>";
    }
    echo "</table>";

}

function get_kontrakt_data($conn){
    $sql = "SELECT kontrakt, COUNT(id) AS count FROM kontrakt 
    WHERE kontrakt IN ('umowa o pracę', 'kontrakt B2B', 'umowa zlecenie', 'umowa o staż / praktyki', 'umowa o dzieło', 'umowa na zastępstwo')
    GROUP BY kontrakt ORDER  BY count DESC";

    $result = $conn->query($sql);

    if ($result === false) {
        die("Query error: " . $conn->error);
    }

    echo "<table style='text-align: left;'>";
    while ($row = $result->fetch_assoc()) {
        $contractType = $row['kontrakt'];
        $count = $row['count'];
        echo "<tr>";
        echo "<td>".$count ."</td><td>". $contractType ."</td>";
        echo "</tr>";
    }
    echo "</table>";
}

function get_management_level_data($conn){
    $sql = "SELECT management_level, COUNT(id) AS count FROM management_level 
    WHERE management_level IN ('Mid', 'asystent', 'Junior', 'Senior', 'ekspert', 'team manager','menedżer', 'praktykant / stażysta','dyrektor')
    GROUP BY management_level ORDER  BY count DESC";

    $result = $conn->query($sql);

    if ($result === false) {
        die("Query error: " . $conn->error);
    }

    echo "<table style='text-align: left;'>";
    while ($row = $result->fetch_assoc()) {
        $management_level = $row['management_level'];
        $count = $row['count'];
        echo "<tr>";
        echo "<td>".$count ."</td><td>". $management_level ."</td>";
        echo "</tr>";
    }
    echo "</table>";
}

function get_work_type_data($conn){
    $sql = "SELECT work_type, COUNT(id) AS count FROM work_type 
    WHERE work_type IN ('praca hybrydowa', 'praca zdalna', 'praca stacjonarna', 'praca mobilna')
    GROUP BY work_type ORDER  BY count DESC";

    $result = $conn->query($sql);

    if ($result === false) {
        die("Query error: " . $conn->error);
    }

    echo "<table style='text-align: left;'>";
    while ($row = $result->fetch_assoc()) {
        $work_type = $row['work_type'];
        $count = $row['count'];
        echo "<tr>";
        echo "<td>".$count ."</td><td>". $work_type ."</td>";
        echo "</tr>";
    }
    echo "</table>";
}

function get_spec_data($conn){
    $sql = "SELECT specjalizacja, COUNT(specjalizacja) AS count
    FROM specjalizacje
    WHERE specjalizacja IS NOT NULL AND specjalizacja != ''
    GROUP BY specjalizacja
    ORDER BY count DESC
    LIMIT 20;";

    $result = $conn->query($sql);

    if ($result === false) {
        die("Query error: " . $conn->error);
    }

    echo "<table style='text-align: left;'>";
    while ($row = $result->fetch_assoc()) {
        $specjalizacja = $row['specjalizacja'];
        $count = $row['count'];
        echo "<tr>";
        echo "<td>".$count ."</td><td>". $specjalizacja ."</td>";
        echo "</tr>";
    }
    echo "</table>";
}

function get_wym_tech_data($conn){
    $sql = "SELECT technologia, COUNT(technologia) AS count
    FROM technologie_wymagane
    GROUP BY technologia
    ORDER BY count DESC
    LIMIT 20;";

    $result = $conn->query($sql);

    if ($result === false) {
        die("Query error: " . $conn->error);
    }

    echo "<table style='text-align: left;'>";
    while ($row = $result->fetch_assoc()) {
        $technologia = $row['technologia'];
        $count = $row['count'];
        echo "<tr>";
        echo "<td>".$count ."</td><td>". $technologia ."</td>";
        echo "</tr>";
    }
    echo "</table>";
}

function get_opt_tech_data($conn){
    $sql = "SELECT technologia, COUNT(technologia) AS count
    FROM technologie_mile_widziane
    GROUP BY technologia
    ORDER BY count DESC
    LIMIT 20;";

    $result = $conn->query($sql);

    if ($result === false) {
        die("Query error: " . $conn->error);
    }

    echo "<table style='text-align: left;'>";
    while ($row = $result->fetch_assoc()) {
        $technologia = $row['technologia'];
        $count = $row['count'];
        echo "<tr>";
        echo "<td>".$count ."</td><td>". $technologia ."</td>";
        echo "</tr>";
    }
    echo "</table>";
}

function get_location_data($conn){
    $sql = "SELECT location, COUNT(*) AS location_count
    FROM `data`
    GROUP BY location
    ORDER BY location_count DESC
    LIMIT 20;";

    $result = $conn->query($sql);

    if ($result === false) {
        die("Query error: " . $conn->error);
    }
    echo "<table style='text-align: left;'>";
    while ($row = $result->fetch_assoc()) {
        $location = $row['location'];
        $count = $row['location_count'];
        echo "<tr>";
        echo "<td>".$count ."</td><td>". $location ."</td>";
        echo "</tr>";
    }
    echo "</table>";
}

function get_last_date($conn){

$sql = "SELECT date FROM `data` ORDER BY DESC LIMIT BY 1";

}



?>
