import sqlite3
import datetime
from parser import Parser

pars = Parser()
# This class is a simple handler for all of our SQL database actions
# Practicing a good separation of concerns, we should only ever call
# These functions from our models

# If you notice anything out of place here, consider it to your advantage and don't spoil the surprise
class SQLDatabasePost():
    '''
        Our SQL Database

    '''

    # Get the database running
    def __init__(self, database_arg):
        print("Connected to database at: ")
        self.conn = sqlite3.connect(database_arg)
        self.cur = self.conn.cursor()
        self.location = database_arg

    # SQLite 3 does not natively support multiple commands in a single statement
    # Using this handler restores this functionality
    # This only returns the output of the last command
    def execute(self, sql_string):
        out = None
        for string in sql_string.split(";"):
            try:
                out = self.cur.execute(string)
            except:
                print("excution failed: "+sql_string)
                print("DB location: "+self.location)
                raise
                pass
        return out

    # Commit changes to the database
    def commit(self):
        self.conn.commit()

    #-----------------------------------------------------------------------------

    # Sets up the database
    # Default admin password
    def database_setup(self):

        # Clear the database if needed
        self.execute("DROP TABLE IF EXISTS Posts")
        self.commit()

        # Create the users table
        self.execute("""CREATE TABLE Posts(
            post_id INTEGER,
            post_time DATETIME,
            username TEXT,
            title TEXT,
            content TEXT,
            pinned TEXT
        )""")

        self.commit()

    #-----------------------------------------------------------------------------
    # User handling
    #-----------------------------------------------------------------------------
    # Add a post to the database
    def add_post(self, username, title, content,pinned="FALSE"):
        sql_cmd = """
                INSERT INTO Posts(post_id,post_time,username,title,content,pinned)
                VALUES({post_id}, '{post_time}', '{username}', '{title}', '{content}','{pinned}')
            """
        now = datetime.datetime.now()
        #date_time = now.strftime("%m/%d/%Y/%H/%M/%S")
        date_time_y = str(now.strftime("%Y"))
        date_time_mo = str(now.strftime("%m"))
        date_time_d = str(now.strftime("%d"))
        date_time_h = str(now.strftime("%H"))
        date_time_mi = str(now.strftime("%M"))
        date_time_s = str(now.strftime("%S"))


        date_time = date_time_y + '-' + date_time_mo + '-' + date_time_d + ' ' + date_time_h + ':' + date_time_mi + ':' + date_time_s


        next_id = len(self.get_allposts()) + 1

        sql_cmd = sql_cmd.format(post_id=next_id, post_time=date_time, username=username, title=title, content=content,pinned=pinned)
        print(sql_cmd)
        self.execute(sql_cmd)
        self.commit()
        return True

    #-----------------------------------------------------------------------------

    # Retrive a post by id
    def get_post(self, id):
        qu = """
            SELECT *
            FROM Posts
        """
        sql_cmd = qu.format(id=id)
        self.cur.execute(sql_cmd)
        result = self.cur.fetchall()
        for row in result:
            if row[0] == id:
                dic = {"post_id": row[0], "post_time":row[1],"username": row[3], "title": pars.decode(row[4])[0], "content": pars.decode(row[2])[0],"pinned":row[5]}

        # Return a dictionary : {Id:int, username:string, title:string, content:string}
        return dic

    def pin_unpin_post(self, pinned,id):
        qu = """
            UPDATE Posts
            SET pinned="{pinned}"
            WHERE post_id={id}
        """
        sql_cmd = qu.format(id=id,pinned=pinned)
        self.cur.execute(sql_cmd)
        self.commit()
        return

    def get_allposts(self):

        qu = """
        SELECT * FROM Posts
        """
        qu = qu.format()
        self.cur.execute(qu)
        dic_list = []
        result = self.cur.fetchall()
        for row in result:
            dic = {"post_id": row[0], "post_time": row[1], "username": row[3], "title": pars.decode(row[4])[0], "content": pars.decode(row[2])[0],"pinned":row[5]}
            dic_list.append(dic)


        # Return a list of dictionaries : [{Id:int, username:string, title:string, content:string},{...},{...}]
        return dic_list

    def delete_single_post(self,post_id):
        qu = """
            DELETE FROM Posts WHERE post_id = '{post_id}'
        """
        sql = qu.format(post_id=post_id)
        self.cur.execute(sql)
        self.commit()
        return True
