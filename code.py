<?php
session_start();
include 'config.php';

if (!isset($_SESSION['username'])) {
    header("Location: login.php");
    exit();
}S

if ($_SESSION['role'] != 'admin') {
    echo "You do not have Role to access this page.";
    exit();
}

$result = $conn->query("SELECT * FROM users WHERE blocked = 1");
?>
<!DOCTYPE html>
<html lang="ar">
<head>
    <meta charset="UTF-8">
    <title>Unblocking management</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>

<div class="topbar">✅ Unblocking management</div>

<div class="container">
    <div class="card">
        <h2 class="page-title">Block accounts</h2>

        <?php
        if ($result->num_rows > 0) {
            while ($row = $result->fetch_assoc()) {
                echo "<div class='card'>";
                echo "<p><strong>User name:</strong> ".$row['username']."</p>";
                echo "<p><strong>Role:</strong> ".$row['role']."</p>";
                echo "<a class='btn' href='unblock.php?id=".$row['id']."'>🔓 Unblock /a>";
                echo "</div>";
            }
        } else {
            echo "<p>No accounts are blocked.</p>";
        }
        ?>

        <a class="btn" href="dashboard.php">⬅Back</a>
    </div>
</div>

</body>
</html>
