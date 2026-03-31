<?php session_start(); ?>
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Login</title>
<link rel="stylesheet" href="style.css">
</head>

<body>

<div class="login-page">

<div class="login-box">

<img src="assets/logo.png" class="logo">

<h2>Clinic Management System</h2>
<p class="login-subtitle">Secure medical system login</p>

<form method="POST" action="check_login.php">

<label>Username</label>
<input type="text" name="username" required>

<label>Password</label>
<input type="password" name="password" required>

<button type="submit">Sign In</button>

</form>

<?php
if(isset($_SESSION['msg'])){
echo "<p class='error'>".$_SESSION['msg']."</p>";
unset($_SESSION['msg']);
}
?>

</div>

</div>

</body>
</html>
