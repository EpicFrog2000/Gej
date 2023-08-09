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
<p style="text-align: center;"><?php count_all_data();?></p>
    <div class="today_data_div">
        
        <div class="stuff">
            <h2>Salary stuff</h2>
            <?php percent_salary();?>
        </div>
        <div class="stuff">
            <h2>Etat stuff</h2>
            <?php get_etat_data();?>
        </div>
        <div class="stuff">
            <h2>Kontrakt stuff</h2>
            <?php get_kontrakt_data();?>
        </div>
        <div class="stuff">
            <h2>Kontrakt stuff</h2>
            <?php get_management_level_data();?>
        </div>
        <div class="stuff">
            <h2>tryb_pracy stuff</h2>
            <?php get_work_type_data();?>
        </div>
        <div class="stuff">
            <h2>top 20 specjalizacji</h2>
            <?php get_spec_data();?>
        </div>
        <div class="stuff">
            <h2>top 20 wymaganych technologii</h2>
            <?php get_wym_tech_data();?>
        </div>
        <div class="stuff">
            <h2>top 20 optional technologii</h2>
            <?php get_opt_tech_data();?>
        </div>

    </div>
    <h1 style="text-align: center;">Historic data<h1>
        wykresiki jakies tam gowno kurwaaaaa
</body>
</html>
<?php
$conn->close();
?>
<!--
    add the rest of todays data
-->

