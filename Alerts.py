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

$result = $conn->query("SELECT * FROM alerts ORDER BY id DESC");
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Security Alerts</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>

<div class="topbar">🔔 Security Alerts</div>

<div class="container">
    <div class="card">
        <h2 class="page-title">All Security Alerts</h2>

        <?php
        if ($result->num_rows > 0) {
            while ($row = $result->fetch_assoc()) {
                echo "<div class='card'>";
                echo "<p><strong>User:</strong> ".$row['username']."</p>";
                echo "<p><strong>Alert:</strong> ".$row['message']."</p>";
                echo "<p><strong>Time:</strong> ".$row['created_at']."</p>";
                echo "</div>";
            }
        } else {
            echo "<p>No alerts</p>";
        }
        ?>

        <a class="btn" href="dashboard.php">⬅ Back</a>
    </div>
</div>

</body>
</html>
