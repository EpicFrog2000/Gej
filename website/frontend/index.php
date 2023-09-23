<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Data from it.pracuj.pl site</title>
    <link rel="stylesheet" type="text/css" href="styles.css">
    <?php include '../backend/db_operations.php';?>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
</head>
<body loading="lazy">

    <div class="top_menu">
        <ul class = top_menu_list>
            <li class="menu_list_option"> <a href="about.php" style="color: rgb(200, 200, 200);"> O mnie </a> </li>
            <li class="menu_list_option">
            <details>
              <summary>
              ⬇️Dane ze stronek
              </summary>
              <a href="project1.php" class="option"> Projekt 1 </a></br>
              <a href="project2.php" class="option"> Projekt 2 </a></br>
              <a href="project3.php" class="option"> Projekt 3 </a>

            </details>
                
                
            </li>
            <li class="menu_list_option"> <a href="otherP.php" style="color: rgb(200, 200, 200);"> inne projekty </a> </li>
            <li class="menu_list_option"> <a href="main.php" style="color: rgb(200, 200, 200);"> glowna </a> </li>
        </ul>
        <!--glowna-->
        <!--Lista danych ze stron-->
        <!--inne projekty-->
        <!--O mnie-->

    </div>

    <div class="main">

        <div class="Ban">
            <a>Dane z <a style="color: rgb(200, 200, 200);" href ="https://it.pracuj.pl/" target="_blank">it.pracuj.pl</a>.
            <a style="text-align: center;"><?php count_all_data($conn);?></a>
        </div>

        <div class="data">
        <?php echo "<h1>TE DANE ZEBRANO OSTATNIO Z ".date('Y-m-d') ."</h1>"?>

         <!--Zmień na ostanią dete z bazy danych (nie ma jej, trzeba dorobic te funkcje)-->

            <div class="bg"></div>

            <div class="left">
                <div class="stuff">
                    <h2>PŁACA</h2>
                    <?php percent_salary($conn); echo "</br>";?>
                </div>
                <div class="stuff">
                    <h2>POZIOM</h2>
                    <?php get_management_level_data($conn);?>
                </div>
                <div class="stuff">
                    <h2>TOP 20 WYMAGANYCH TECHNOLOGII</h2>
                    <?php get_wym_tech_data($conn);?>
                </div>
            </div>

            <div class="center">
                <div class="stuff">
                    <h2>ETAT</h2>
                    <?php get_etat_data($conn);?>
                </div>
                <div class="stuff">
                    <h2>TOP 20 SPECJALIZACJI</h2>
                    <?php get_spec_data($conn);?>
                </div>
                <div class="stuff">
                    <h2>TOP 20 MILE WIDZIANYCH TECHNOLOGII</h2>
                    <?php get_opt_tech_data($conn);?>
                </div>
            </div>

            <div class="right">
                <div class="stuff">
                    <h2>KONTRAKT</h2>
                    <?php get_kontrakt_data($conn);?>
                </div>
                <div class="stuff">
                    <h2>TRYB PRACY</h2>
                    <?php get_work_type_data($conn);?>
                </div>
                <div class="stuff">
                    <h2>TOP 20 LOKACJI</h2>
                    <?php get_location_data($conn);?>
                </div>
            </div>

        </div>

            <div class="data-charts">
            <div class="bg"></div>
                <h1 style="text-align: center; margin: 0;padding: 0;">HISTORYCZNE DANE</h1>
                
                <div class="wykresy">
                    <div class="wykres">
                        <h2 style="text-align: center;">HISTORIC ILOSC OFERT</h2>
                        <canvas id="count_chart"></canvas>
                    </div>
                    <hr>
                    <div class="wykres">
                        <h2 style="text-align: center;">HISTORIC ETAT</h2>
                        <canvas id="historic_etat_chart"></canvas>
                    </div>
                    <hr>
                    <div class="wykres">
                        <h2 style="text-align: center;">HISTORIC WORK TYPE</h2>
                        <canvas id="work_type_etat_chart"></canvas>
                    </div>
                    <hr>
                    <div class="wykres">
                        <h2 style="text-align: center;">HISTORIC KONTRAKT</h2>
                        <canvas id="kontrakt_chart"></canvas>
                    </div>
                    <hr>
                    <div class="wykres">
                        <h2 style="text-align: center;">HISTORIC MANAGEMENT LEVEL</h2>
                        <canvas id="management_level_chart"></canvas>
                    </div>
                    <hr>
                    
                    <div class="wykres">
                        <h2 style="text-align: center;">HISTORIC WYMAGANE TECHNOLOGIE</h2>
                        <canvas id="historic_technologie_wymagane"></canvas>
                    </div>
                    <hr>
                    <div class="wykres">
                        <h2 style="text-align: center;">HISTORIC MILE WIDZIANE TECHNOLOGIE</h2>
                        <canvas id="historic_technologie_mile_widziane"></canvas>
                    </div>
                    <hr>

                    <script src="../backend/charts.js"></script>
                </div>
            </div>

        <div class="footer">

            <div class="kontakt">
                <h2 style="text-align: center;">Dane kontaktowe</h2>
                <p>Tel: +48 690 868 601</p>
                <p>Mail: tasarz_norbert@wp.pl</p>
            </div>

            <div class="wiadomosc">
                <h2 style="text-align: center;">Wyslij wiadomosc prosto do mnie</h2>
                <form id="messageForm" action="../backend/send_msg.php" method="post">
                    <textarea name="message" id="message" cols="40" rows="5" required></textarea>
                    <button type="submit" value="Wyslij" id="clk" onclick="submitForm();">Wyślij</button>
                </form>
                <iframe name="messageFrame" style="display: none;"></iframe>
            </div>
        </div>
    </div>

</body>
</html>
<?php
$conn->close();
?>