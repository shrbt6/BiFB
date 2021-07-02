<?php

require_once('config.php');

session_start();
//POSTのvalidate
if (!filter_var($_POST['account'], FILTER_VALIDATE_ACCOUNT)) {
  echo '入力された値が不正です。';
  return false;
}
//DB内でPOSTされたメールアドレスを検索
try {
  $pdo = new PDO(DSN, DB_USER, DB_PASS);
  $stmt = $pdo->prepare('select * from userDeta where account = ?');
  $stmt->execute([$_POST['account']]);
  $row = $stmt->fetch(PDO::FETCH_ASSOC);
} catch (\Exception $e) {
  echo $e->getMessage() . PHP_EOL;
}
//accountがDB内に存在しているか確認
if (!isset($row['account'])) {
  echo 'メールアドレス又はパスワードが間違っています。';
  return false;
}
//パスワード確認後sessionにメールアドレスを渡す
if (password_verify($_POST['password'], $row['password'])) {
  session_regenerate_id(true); //session_idを新しく生成し、置き換える
  $_SESSION['ACCOUNT'] = $row['account'];
  echo 'ログインしました';
} else {
  echo 'メールアドレス又はパスワードが間違っています。';
  return false;
}
