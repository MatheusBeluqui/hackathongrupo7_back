import os
import pymysql
from flask import jsonify

db_user = 'admin'
db_password = 'admin_password'
db_name = 'app-database'
db_local_host = os.environ.get('DB_LOCAL_HOST')
db_connection_name = 'projeto-7-404421:us-west1:app-database'

def open_connection():
    try:
        if db_connection_name:
            unix_socket = '/cloudsql/{}'.format(db_connection_name)
            conn = pymysql.connect(user=db_user, password=db_password,
                                unix_socket=unix_socket, db=db_name,
                                cursorclass=pymysql.cursors.DictCursor
                                )
            print ('tchau')
        else:
            print ('oi')
            conn = pymysql.connect(user=db_user, password=db_password,
                                host=db_local_host, db=db_name,cursorclass=pymysql.cursors.DictCursor)

    except pymysql.MySQLError as e:
        print(e)

    return conn

def get_songs():
    conn = open_connection()
    with conn.cursor() as cursor:
        result = cursor.execute('SELECT * FROM songs;')
        songs = cursor.fetchall()
        if result > 0:
           got_songs = jsonify(songs)

        else:
            got_songs = 'Nenhuma Musica Cadastrada na Playlist'

    conn.close()

    return got_songs
