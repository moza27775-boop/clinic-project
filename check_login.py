<?php
session_start();
include 'config.php';

$username = $_POST['username'];
$password = $_POST['password'];

$sql = "SELECT * FROM users WHERE username='$username'";
$result = $conn->query($sql);

if ($result->num_rows > 0) {

    $user = $result->fetch_assoc();

    if ($user['blocked'] == 1) {
        $_SESSION['msg'] = "This account is blocked. Admin must unblock it.";
        header("Location: login.php");
        exit();
    }

    if (password_verify($password, $user['password'])) {

        $conn->query("UPDATE users SET attempts=0 WHERE id=" . $user['id']);

        $_SESSION['username'] = $user['username'];
        $_SESSION['role'] = $user['role'];
        $_SESSION['user_id'] = $user['id'];

        header("Location: dashboard.php");
        exit();

    } else {

        $attempts = $user['attempts'] + 1;

        if ($attempts == 3) {
            $message = "User " . $username . " entered the wrong password 3 times";
            $conn->query("INSERT INTO alerts(username, message) VALUES('$username', '$message')");
        }

        if ($attempts >= 4) {
            $conn->query("UPDATE users SET attempts=$attempts, blocked=1 WHERE id=" . $user['id']);
            $_SESSION['msg'] = "Account has been blocked after 4 failed attempts";
        } else {
            $conn->query("UPDATE users SET attempts=$attempts WHERE id=" . $user['id']);
            $_SESSION['msg'] = "Wrong password. Attempt $attempts of 4";
        }

        header("Location: login.php");
        exit();
    }

} else {
    $_SESSION['msg'] = "User not found";
    header("Location: login.php");
    exit();
}
?>
