<?php
session_start();
include 'config.php';

if (!isset($_SESSION['username'])) {
    header("Location: login.php");
    exit();
}

$key = "secretkey123";

function encryptData($data, $key) {
    return openssl_encrypt($data, "AES-128-ECB", $key);
}

if (isset($_POST['data'])) {
    $data = $_POST['data'];
    $encrypted = encryptData($data, $key);
    $user_id = $_SESSION['user_id'];

    $sql = "INSERT INTO secrets (user_id, encrypted_data) VALUES ('$user_id', '$encrypted')";
    $conn->query($sql);

    $msg = "Data has been successfully saved after encryption";
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Encrypt Data</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>

<div class="topbar">Encrypt Data</div>

<div class="container">
    <div class="card">
        <h2>Enter Data to Encrypt</h2>

        <form method="POST">
            <label>Enter Data</label>
            <input type="text" name="data" required>
            <button type="submit">Encrypt and Save</button>
        </form>

        <?php
        if (isset($msg)) {
            echo "<p class='success'>$msg</p>";
        }
        ?>

        <br>
        <a class="btn" href="view_secrets.php">View Encrypted Data</a>
        <a class="btn" href="dashboard.php">Back</a>
    </div>
</div>

</body>
</html>
