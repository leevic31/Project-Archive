import pymysql.cursors


def get_db_connection(username, password, database):
    '''coonect to the database server

    Args:
        username (string): username
        password (string): password
        database (string): database schemas

    Returns:
        object: database
    '''

    connection = pymysql.connect(host='localhost',
                                 user=username,
                                 password=password,
                                 db=database,
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection
