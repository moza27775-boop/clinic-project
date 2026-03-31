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
    <title>Decrypt Data</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>

<div class="topbar">🔓 Data Decryption</div>

<div class="container">
    <div class="card">
        <h2 class="page-title">Decrypted Data</h2>
        <p>All your encrypted records will appear below.</p>
    </div>

    <?php
    if ($result->num_rows > 0) {
        while ($row = $result->fetch_assoc()) {
            $decrypted = decryptData($row['encrypted_data'], $key);

            echo "<div class='card'>";
            echo "<p><strong>Encrypted Text:</strong><br>" . $row['encrypted_data'] . "</p>";
            echo "<p><strong>Decrypted Text:</strong><br>" . $decrypted . "</p>";
            echo "</div>";
        }
    } else {
        echo "<div class='card'><p>No encrypted data found.</p></div>";
    }
    ?>

    <div class="card">
        <a class="btn" href="encrypt.php">🔐 Encrypt Data</a>
        <a class="btn" href="dashboard.php">⬅ Back to Dashboard</a>
    </div>
</div>

</body>
</html>
