<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Main Site</title>
    <?php include 'db_operations.php';?>
    <link rel="stylesheet" type="text/css" href="styles.css">
</head>
<body>
    <h1 style="text-align: center;">Todays data<h1>
    <div class="today_data_div">
        
        <div class="salary_stuff">
            <h2>Salary stuff</h2>
            <?php 
                percent_salary();
                
            ?>
        </div>
        <div class="etat_stuff">
            <h2>Etat stuff</h2>
            <?php 
                get_etat_data();
                
            ?>
        </div>
    </div>
    <h1 style="text-align: center;">Historic data<h1>
        wykresiki jakies tam gowno kurwaaaaa
</body>
</html>
<?php
$conn->close();
?>

