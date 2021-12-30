import sqlite3
import datetime
# This class is a simple handler for all of our SQL database actions
# Practicing a good separation of concerns, we should only ever call
# These functions from our models

# If you notice anything out of place here, consider it to your advantage and don't spoil the surprise
class SQLDatabase():
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
        self.execute("DROP TABLE IF EXISTS Users")
        self.commit()

        # Create the users table
        self.execute("""CREATE TABLE Users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username VARCHAR(20),
            password VARCHAR(20),
            EMAIL VARCHAR(50),
            admin INTEGER DEFAULT 0,
            mute VARCHAR(20) DEFAULT '0',
            postTime DATETIME
        )""")
        self.commit()
        # Add our admin user
        self.add_user('admin','asdad12313asdqw12e1231','admin@gmail.com','0')
    #-----------------------------------------------------------------------------
    # User handling
    #-----------------------------------------------------------------------------

    # Add a user to the database
    def add_user(self, username, password, email, admin=0,mute='0'):
        sql_cmd = """
                INSERT INTO Users(username,password,email,admin,mute,postTime)
                VALUES('{username}', '{password}','{email}',{admin},'{mute}','{postTime}')
            """
        now = datetime.datetime.now()
        date_time_y = str(now.strftime("%Y"))
        date_time_mo = str(now.strftime("%m"))
        date_time_d = str(now.strftime("%d"))
        date_time_h = str(now.strftime("%H"))
        date_time_mi = str(now.strftime("%M"))
        date_time_s = str(now.strftime("%S"))

        date_time = date_time_y + ':' + date_time_mo + ':' + date_time_d + ':' + date_time_h + ':' + date_time_mi + ':' + date_time_s
        sql_cmd = sql_cmd.format(username=username, password=password, email=email,admin=admin,mute=mute,postTime=date_time)
        self.execute(sql_cmd)
        print("User added")
        self.commit()
        return True

    #-----------------------------------------------------------------------------
    def add_post_time(self, id):
        sql_cmd = """
                        UPDATE Users
                        SET postTime = '{postTime}'
                        WHERE id = '{user_id}'
                    """
        now = datetime.datetime.now()
        date_time_y = str(now.strftime("%Y"))
        date_time_mo = str(now.strftime("%m"))
        date_time_d = str(now.strftime("%d"))
        date_time_h = str(now.strftime("%H"))
        date_time_mi = str(now.strftime("%M"))
        date_time_s = str(now.strftime("%S"))

        date_time = date_time_y + ':' + date_time_mo + ':' + date_time_d + ':' + date_time_h + ':' + date_time_mi + ':' + date_time_s
        print(date_time)
        sql_cmd = sql_cmd.format(postTime=date_time, user_id=int(id))
        self.execute(sql_cmd)
        self.commit()
        return True

    def get_post_time(self, user_id):
        sql_cmd = """
                        SELECT postTime
                        FROM Users
                        WHERE id = '{user_id}'
                    """
        sql_cmd = sql_cmd.format(user_id=int(user_id))
        self.execute(sql_cmd)
        postTime = self.cur.fetchone()[0]
        print(postTime)
        return postTime

    # Check login credentials
    def check_credentials(self, username, password):
        sql_query = """
                SELECT 1
                FROM Users
                WHERE username = '{username}' AND password = '{password}'
            """
        sql_query = sql_query.format(username=username, password=password)
        self.execute(sql_query)
        # If our query returns
        if self.cur.fetchone():
            print("login successful")
            return True
        else:
            return False

    # -----------------------------------------------------------------------------
    def get_userid_by_username_and_password(self, username, password):
        sql_query = """
                SELECT id
                FROM Users
                WHERE username = '{username}' AND password = '{password}'
            """
        sql_query = sql_query.format(username=username, password=password)
        self.execute(sql_query)
        # If our query returns

        # print (self.cur.fetchone()[0])
        user_id = self.cur.fetchone()[0]
        if user_id ==None:
            return 0
        print(user_id)
        return user_id

    #-----------------------------------------------------------------------------
    def get_allusers(self):

        qu = """
        SELECT * FROM Users WHERE username != '{username}'
        """
        qu = qu.format(username='admin')
        self.cur.execute(qu)
        dic_list = []
        result = self.cur.fetchall()
        for row in result:
            dic = {"user_id": row[0], "username": row[1], "password": row[2], "email": row[3],"admin": row[4],"mute":row[5]}
            dic_list.append(dic)


        # Return a list of dictionaries : [{Id:int, username:string, title:string, content:string},{...},{...}]
        return dic_list

    def count_users(self):
        qu = """
            SELECT COUNT(*)
            FROM Users
            WHERE username != '{username}'
        """
        qu = qu.format(username='admin')
        self.cur.execute(qu)
        return self.cur.fetchone()[0]

    def delete_single_user(self,user_id):
        qu = """
            DELETE FROM Users WHERE id = '{user_id}'
        """
        sql = qu.format(user_id=user_id)
        self.cur.execute(sql)
        self.commit()
        return True

    def delete_all_users(self):
        qu = """
            DELETE FROM Users
        """
        self.cur.execute(qu)
        self.commit()
        return True

    def mute_single_user(self,user_id):
        qu = """
            UPDATE Users
            SET mute = '1'
            WHERE id = '{user_id}'
        """
        qu = qu.format(user_id=user_id)
        print("mute success")
        self.cur.execute(qu)
        self.commit()
        return True

    def unmute_single_user(self, user_id):
        qu = """
               UPDATE Users
               SET mute = '0'
               WHERE id = '{user_id}'
           """
        qu = qu.format(user_id=user_id)
        print("mute success")
        self.cur.execute(qu)
        self.commit()
        return True

    def get_if_mute(self,user_id):
        qu="""
            SELECT mute
            FROM Users
            WHERE id = '{user_id}'
        """
        qu = qu.format(user_id=user_id)
        self.cur.execute(qu)
        if user_id == 1:
            return '0'
        if_mute = self.cur.fetchone()[0]
        if if_mute==None:
            return 0
        print(if_mute)
        return if_mute

