# ベースイメージ
FROM python:3.6

RUN mkdir /var/www
# workdirの指定
WORKDIR /var/www

# 依存Pythonライブラリ一覧コピー
COPY requirements.txt ./

# 依存Pythonライブラリインストール
RUN pip install --no-cache-dir -r requirements.txt
    
# CMD sh -c "rm ./data/photos.sqlite3 && touch ./data/photos.sqlite3 && python setup_database.py && uwsgi --ini /var/www/uwsgi.ini"
CMD sh -c "uwsgi --ini /var/www/uwsgi.ini"