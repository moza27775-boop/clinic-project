<?php
session_start();
include 'config.php';

if (!isset($_SESSION['username'])) {
    header("Location: login.php");
    exit();
}

$key = "secretkey123";

function decryptData($data, $key) {
    return openssl_decrypt($data, "AES-128-ECB", $key);
}

$user_id = $_SESSION['user_id'];

$sql = "SELECT * FROM secrets WHERE user_id='$user_id' ORDER BY id DESC";
$result = $conn->query($sql);
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>View Encrypted Data</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>

<div class="topbar">Encrypted Data</div>

<div class="container">
    <div class="card">
        <h2>User Private Data</h2>

        <?php
        if ($result->num_rows > 0) {
            while ($row = $result->fetch_assoc()) {
                echo "<p><strong>Encrypted Text:</strong> " . $row['encrypted_data'] . "</p>";
                echo "<p><strong>Decrypted Text:</strong> " . decryptData($row['encrypted_data'], $key) . "</p>";
                echo "<hr>";
            }
        } else {
            echo "<p>No saved data</p>";
        }
        ?>

        <a class="btn" href="encrypt.php">Back to Encryption</a>
        <a class="btn" href="dashboard.php">Dashboard</a>
    </div>
</div>

</body>
</html>
