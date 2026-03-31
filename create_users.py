<?php
include 'config.php';

$users = [
    ['doctor', '123456', 'admin', 'doctor@gmail.com'],
    ['nurse', '123456', 'user', 'nurse@gmail.com'],
    ['reception', '123456', 'user', 'reception@gmail.com']
];

foreach ($users as $user) {
    $username = $user[0];
    $password = password_hash($user[1], PASSWORD_DEFAULT);
    $role = $user[2];
    $email = $user[3];

    $check = $conn->query("SELECT id FROM users WHERE username='$username'");
    if ($check && $check->num_rows == 0) {
        $sql = "INSERT INTO users (username, password, role, email)
                VALUES ('$username', '$password', '$role', '$email')";
        $conn->query($sql);
    }
}

echo "Users created successfully";
?>
