# BiFB
### Bi-FeedBack: 相互フィードバックアプリ
BiFBは開発者同士が相互にフィードバックを行うアプリです。
開発者はBiFAにアプリを掲載することでフィードバックを受けることができます。
掲載できる期間には限りがありますが、他の開発者のアプリのフィードバックをすることで掲載期間を延長することができます。

### 以下BiFB開発メンバー向け
Docker / Docker Compose を利用して実行します。
はじめに`cd`コマンドでBiFBフォルダに移動します。

アプリ起動
```
docker-compose up -d --build
```
アプリ再起動（ブラウザで再読み込みしても反映されない場合実行）
```
docker-compose restart
```
アプリ停止
```
docker-compose down down --rmi all
```
起動したアプリを確認するにはブラウザで`http://localhost:4231/`にアクセスします。