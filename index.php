<?php

function h($s){
  return htmlspecialchars($s, ENT_QUOTES, 'utf-8');
}

session_start();
//ログイン済みの場合
if (isset($_SESSION['ACCOUNT'])) {
  echo 'ようこそ' .  h($_SESSION['ACCOUNT']) . "さん<br>";
  echo "<a href='/logout.php'>ログアウトはこちら。</a>";
  exit;
}

 ?>

<!DOCTYPE html>
<html lang="ja">
 <head>
   <meta charset="utf-8">
   <title>Login</title>
 </head>
 <body>
   <h1>ようこそ、ログインしてください。</h1>
   <form  action="login.php" method="post">
     <label for="account">account</label>
     <input type="account" name="account">
     <label for="password">password</label>
     <input type="password" name="password">
     <button type="submit">Sign In!</button>
   </form>
   <h1>初めての方はこちら</h1>
   <form action="signUp.php" method="post">
     <label for="account">account</label>
     <input type="account" name="account">account
     <label for="password">password</label>
     <input type="password" name="password">
     <button type="submit">Sign Up!</button>
     <p>※パスワードは半角英数字をそれぞれ１文字以上含んだ、８文字以上で設定してください。</p>
   </form>
 </body>
</html>