<?php
session_start();
include 'config.php';

if (!isset($_SESSION['username'])) {
    header("Location: login.php");
    exit();
}

if ($_SESSION['role'] != 'admin') {
    echo "You do not have permission";
    exit();
}

$id = $_GET['id'];

$conn->query("UPDATE users SET blocked=0, attempts=0 WHERE id=$id");

header("Location: admin_unblock.php");
exit();
?>
