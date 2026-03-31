<?php
$conn = new mysqli("localhost", "root", "", "clinic_system");

if ($conn->connect_error) {
    die("Failed to connect to the database");
}
?>
