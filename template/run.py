'''
    This is a file that configures how your server runs
    You may eventually wish to have your own explicit config file
    that this reads from.

    For now this should be sufficient.

    Keep it clean and keep it simple, you're going to have
    Up to 5 people running around breaking this constantly
    If it's all in one file, then things are going to be hard to fix

    If in doubt, `import this`
'''

#-----------------------------------------------------------------------------
#!/usr/bin/python3
import sys
from bottle import run

#-----------------------------------------------------------------------------
# You may eventually wish to put these in their own directories and then load
# Each file separately

# For the template, we will keep them together

import model
import view
import controller
import os
#-----------------------------------------------------------------------------

# It might be a good idea to move the following settings to a config file and then load them
# Change this to your IP address or 0.0.0.0 when actually hosting
host = 'localhost'
admin_password = '1234'

# Test port, change to the appropriate port to host
port = 8090

# Turn this off for production
debug = True

def run_server():
    '''
        run_server
        Runs a bottle server
    '''
    run(host=host,port=1111, debug=debug)

#-----------------------------------------------------------------------------
# Optional SQL support
# Comment out the current manage_db function, and
# uncomment the following one to load an SQLite3 database


import sql
import sql_post
import sql_comment

def manage_db():
    '''
        manage_db
        Starts up and re-initialises an SQL databse for the server
    '''
    user_db_args="user.db"
    post_db_args="post.db"
    comment_db_args="comment.db"
    user_db = sql.SQLDatabase(user_db_args)
    post_db_args = sql_post.SQLDatabasePost(post_db_args)
    comment_db = sql_comment.SQLDatabaseComment(comment_db_args)
    user_db.database_setup()
    post_db_args.database_setup()
    comment_db.database_setup()

    return


#-----------------------------------------------------------------------------

# What commands can be run with this python file
# Add your own here as you see fit

command_list = {
    'manage_db' : manage_db,
    'server'       : run_server
}

# The default command if none other is given
default_command = 'server'

def run_commands(args):
    '''
        run_commands
        Parses arguments as commands and runs them if they match the command list

        :: args :: Command line arguments passed to this function
    '''
    commands = args[1:]

    # Default command
    if len(commands) == 0:
        commands = [default_command]

    for command in commands:
        if command in command_list:
            command_list[command]()
        else:
            print("Command '{command}' not found".format(command=command))

#-----------------------------------------------------------------------------
manage_db()
run_server()
