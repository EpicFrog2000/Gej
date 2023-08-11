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
    <div class="Ban">
        <h1 style="text-align: center; margin: 0;">Dzisiejsze dane</h1>
        <a>Dane z <a style="color: rgb(200, 200, 200);" href ="https://it.pracuj.pl/" target="_blank">it.pracuj.pl</a>.
        <a style="text-align: center;"><?php count_all_data();?></a>
    </div>
    <div class="today_data_div">
        <div class="background"></div>
        <div class="bg"></div>
        <div class="stuff">
            <h2>Salary</h2>
            <?php percent_salary();?>
        </div>
        <div class="stuff">
            <h2>Etat</h2>
            <?php get_etat_data();?>
        </div>
        <div class="stuff">
            <h2>Kontrakt</h2>
            <?php get_kontrakt_data();?>
        </div>
        <div class="stuff">
            <h2>Level</h2>
            <?php get_management_level_data();?>
        </div>
        <div class="stuff">
            <h2>Work mode</h2>
            <?php get_work_type_data();?>
        </div>
        <div class="stuff">
            <h2>TOP 20 specializations</h2>
            <?php get_spec_data();?>
        </div>
        <div class="stuff">
            <h2>TOP 20 required technologies</h2>
            <?php get_wym_tech_data();?>
        </div>
        <div class="stuff">
            <h2>TOP 20 optional technologies</h2>
            <?php get_opt_tech_data();?>
        </div>
        <div class="stuff">
            <h2>TOP 20 locations</h2>
            <?php get_location_data();?>
        </div>

    </div>
    <div class="his">
        <h1 style="text-align: center;margin: 0;padding: 0;">Historic data</h1>
        wykresiki jakies tam gowno kurwaaaaa
    </div>

</body>
</html>
<?php
$conn->close();
?>