import sqlite3
from datetime import datetime
from parser import Parser
pars = Parser()
# This class is a simple handler for all of our SQL database actions
# Practicing a good separation of concerns, we should only ever call
# These functions from our models

# If you notice anything out of place here, consider it to your advantage and don't spoil the surprise
class SQLDatabaseComment():
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
        self.execute("DROP TABLE IF EXISTS Comments")
        self.commit()

        # Create the users table
        self.execute("""CREATE TABLE Comments(
            comment_id INTEGER,
            username TEXT,
            post_time DATETIME,
            content TEXT,
            post_id INTEGER
        )""")

        self.commit()
    #-----------------------------------------------------------------------------
    # User handling
    #-----------------------------------------------------------------------------

    # Add a post to the database
    def add_comment(self, username,content,post_id):
        sql_cmd = """
                INSERT INTO Comments
                VALUES ({comment_id}, '{username}', '{post_time}', '{content}', {post_id})
            """
        id = self.get_num_comments()+1
        now = datetime.now()
        time_y  = str(now.strftime("%Y"))
        time_m  = str(now.strftime("%m"))
        time_d  = str(now.strftime("%d"))
        hours   = str(now.strftime("%H"))
        minutes = str(now.strftime("%M"))
        seconds = str(now.strftime("%S"))
        p_time = time_y + '-' + time_m + '-' + time_d + ' ' + hours + ':' + minutes + ':' + seconds

        sql_cmd = sql_cmd.format(comment_id= id, username=username, post_time = p_time, content=content, post_id = post_id)
        self.execute(sql_cmd)
        self.commit()
        return True

    #-----------------------------------------------------------------------------


    # retrieve the comments of a specific post
    def get_comment_by_postid(self, id):
        if (type(id)!= int)|(id<0):
            return None
        sql_cmd = """
            SELECT * FROM Comments
            WHERE post_id={id}"""
        sql_cmd = sql_cmd.format(id=id)
        self.cur.execute(sql_cmd)
        cmnts=self.cur.fetchall()
        if len(cmnts)== 0:
            return
        c_list = []
        for cmnt in cmnts:
            dic = {"Id": cmnt[0], "post_time": cmnt[2], "username": cmnt[1], "content": pars.decode(cmnt[3])[0], "post_id": cmnt[4]}
            c_list.append(dic)
        return c_list
        # todo

        # Return a list of dictionaries :
        #[{comment_id: 123,post_time: 2012-10-22 9:00,username:"ruilin",content:"good day",post_id: 2},{...},{...}]

    def get_num_comments(self):
        sql_cmd = """
                SELECT COUNT(*) FROM Comments
            """
        self.cur.execute(sql_cmd)
        db_length = self.cur.fetchone()[0]
        if db_length == None:
            return 0
        return db_length

    def delete_single_comment(self,comment_id):
        qu = """
            DELETE FROM Comments WHERE comment_id = '{comment_id}'
        """
        sql = qu.format(comment_id=comment_id)
        self.cur.execute(sql)
        self.commit()
        return True

    def delete_all_comments(self,post_id):
        qu = """
            DELETE FROM Comments WHERE post_id = '{post_id}'
        """
        qu = qu.format(post_id=post_id)
        self.cur.execute(qu)
        self.commit()
        return True
