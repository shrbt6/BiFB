# BiFB
### Bi-FeedBack: 双方向フィードバック
BiFBは開発者同士が相互にフィードバックを行うアプリです。
開発者はBiFAにアプリを掲載することでフィードバックを受けることができます。
掲載できる期間には限りがありますが、他の開発者のアプリのフィードバックをすることで掲載期間を延長することができます。
<br>
#### 以下BiFB開発メンバー向け
Docker/docker-composeを利用して実行します。
はじめに`cd`コマンドでBiFBフォルダに移動します。
<br>
アプリ起動
```
docker-compose up -d --build
```
アプリ停止
```
docker-compose down down --rmi all
```
起動したアプリを確認するにはブラウザで`http://localhost:4231/`にアクセスします。