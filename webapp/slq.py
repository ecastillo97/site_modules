
import mysql.connector

def insert_data_query(phrase, letters, ip, browser_string, results):
    """ return RESULTS, BROWSER, IP, LETTERS, PHRASE """
    dbconfig = { 'host' : '127.0.0.1',
             'user' : 'vsearch',
             'password' : 'surium',
             'database' : 'vsearchlogDB'}
    conn = mysql.connector.connect(**dbconfig)
    cursor = conn.cursor()
    _SQL = """insert into log(phrase, letters, ip, browser_string, results) values (%s, %s, %s, %s, %s)"""
    cursor.execute(_SQL, (phrase, letters, ip, browser_string, results))
    conn.commit()
    cursor.close()
    conn.close()
