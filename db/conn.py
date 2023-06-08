import psycopg2
from .db import config

def fetch_one_psql(sql):
    # import pdb; pdb.set_trace()
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql)
        db_return = cur.fetchone()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
        #if db_return is None:
        #    return 
        return db_return


def fetch_psql(sql):
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql)
        db_return = cur.fetchall()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
        return db_return


def insert_psql(sql):
    conn = None
    _id = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql)
        _id = cur.fetchone()[0]
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return _id


def insert_only_psql(sql):
    #import pdb; pdb.set_trace()
    conn = None
    _id = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()



# def get_connection():
#     try:
#         return psycopg2.connect(
#             database="contapessoal",
#             user="contapessoal",
#             password="contapessoal",
#             host="127.0.0.1",
#             port=5432,
#         )
#     except:
#         return False
 
# conn = get_connection()