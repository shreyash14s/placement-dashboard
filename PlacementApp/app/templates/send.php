<?php
require_once 'swift/lib/swift_required.php';

$transport = Swift_SmtpTransport::newInstance('smtp.gmail.com', 465, "ssl")
  ->setUsername('pesplacementhub@gmail.com')
  ->setPassword('aabbccdd123');

$emails = ['pesplacementhub1@gmail.com','pesplacementhub2@gmail.com'];

$da_mess = file_get_contents('/Users/sarnayak/Desktop/Sem7/SE_Project/placement-dashboard/PlacementApp/file.txt');

foreach ($emails as $email) {
    $mailer = Swift_Mailer::newInstance($transport);

	$message = Swift_Message::newInstance('PES Placement Hub - ')
	  ->setFrom(array('pesplacementhub@gmail.com' => 'PES Placement Portal'))
	  ->setTo(array($email))
	  ->setBody('Welcome to PES Placement Portal'.PHP_EOL.'Dear student,'.PHP_EOL."New companies have been added to the portal recently. Login at http://localhost:8080 to register!".PHP_EOL.$da_mess.PHP_EOL.PHP_EOL."Regards,".PHP_EOL."Team Placement Hub");

	$result = $mailer->send($message);
} 

?>
