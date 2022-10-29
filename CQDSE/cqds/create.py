import sqlite3
try:
    conn = sqlite3.connect('te.db')
    c = conn.cursor()

    query = '''
            PRAGMA foreign_keys = ON;
            CREATE TABLE IF NOT EXISTS user(
                [id_u] INTEGER PRIMARY KEY AUTOINCREMENT,
                [email] STRING, 
                [senha] STRING);
            
            CREATE TABLE IF NOT EXISTS pessoa(
                [dre] STRING PRIMARY KEY,
                [nome] STRING,  
                [curso] STRING,
                [senha] STRING,
                [user_id] INTEGER,
                CONSTRAINT fk_id_u FOREIGN KEY (user_id) REFERENCES user(id_u) 
                );

            CREATE TABLE IF NOT EXISTS sala(
                [id_s] INTEGER PRIMARY KEY AUTOINCREMENT,
                [nome] STRING,
                [np] INTEGER);
            '''
    drop_query = '''
            DROP TABLE user;
            DROP TABLE pessoa;
            DROP TABLE sala;
    '''

    c.executescript(query)
    conn.commit()
except Exception as e:
    # print(e)
    raise
