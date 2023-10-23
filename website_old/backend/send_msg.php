<?php
require "vendor/autoload.php";
use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;

$developmentMode = false;
$mailer = new PHPMailer($developmentMode);

if ($_SERVER["REQUEST_METHOD"] === "POST") {
    // Retrieve the message from the form
    $msg = $_POST["message"];
    echo $msg;
    try {
        // Set debugging mode (0 for production)
        $mailer->SMTPDebug = $developmentMode ? 2 : 0;
        $mailer->isSMTP();
        
        if ($developmentMode) {
            $mailer->SMTPOptions = [
                'ssl'=> [
                    'verify_peer' => false,
                    'verify_peer_name' => false,
                    'allow_self_signed' => true
                ]
            ];
        }
        
        // Set SMTP server and authentication
        $mailer->Host = 'smtp.wp.pl'; // SMTP server address
        $mailer->SMTPAuth = true;
        $mailer->Username = 'strona_internetowa@wp.pl'; // Your WP.pl email address
        $mailer->Password = '###'; // Your WP.pl email password
        $mailer->SMTPSecure = 'tls';
        $mailer->Port = 587;
        
        // Set sender and recipient
        $mailer->setFrom('strona_internetowa@wp.pl', 'Name of sender');
        $mailer->addAddress('strona_internetowa@wp.pl', 'Name of recipient');
        
        $mailer->isHTML(true);
        $mailer->Subject = 'PHPMailer Test';
        $mailer->Body = $msg;
        
        $mailer->send();
        $mailer->ClearAllRecipients();

    } catch (Exception $e) {
        echo "EMAIL SENDING FAILED. INFO: " . $mailer->ErrorInfo;
    }
}
?>