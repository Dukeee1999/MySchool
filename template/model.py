'''
    Our Model class
    This should control the actual "logic" of your website
    And nicely abstracts away the program logic from your page loading
    It should exist as a separate layer to any database or data structure that you might be using
    Nothing here should be stateful, if it's stateful let the database handle it
'''
import view
import sql
import random
from bottle import route, get, post, error, request,response,redirect, static_file,template
import json
import sql_post
import sql_comment
import datetime



from parser import Parser
pars = Parser()


# Initialise our views, all arguments are defaults for the template
page_view = view.View()
database_args = "user.db"
#-----------------------------------------------------------------------------
# Index
#-----------------------------------------------------------------------------
def index():
    '''
        index
        Returns the view for the index
    '''
    return page_view("index")

#-----------------------------------------------------------------------------
# Login
#-----------------------------------------------------------------------------

def login_form():
    '''
        login_form
        Returns the view for the login_form
    '''
    return page_view("login")

#-----------------------------------------------------------------------------

def add_user(user):
    db = sql.SQLDatabase("user.db")
    db.add_user(user.getUserName(), user.getPassWord(), user.getEmail())
    users = db.get_allusers()
    count = db.count_users()
    return template("/home/yunqi/git_version/INFO2222-Group-Project/template/views/manager.tpl", users=users, count=count)

def register(user):
    sql_db = sql.SQLDatabase(database_args)
    sql_db.add_user(user.getUserName(),user.getPassWord(),user.getEmail())
    return page_view("login")


# Check the login credentials
def login_check(username, password):
    '''
        login_check
        Checks usernames and passwords

        :: username :: The username
        :: password :: The password

        Returns either a view for valid credentials, or a view for invalid credentials
    '''

    # By default assume good creds
    login = True
    sql_db = sql.SQLDatabase(database_args)

    if username=="admin" and password=="admin123":
        db = sql.SQLDatabase("user.db")
        users = db.get_allusers()
        count = db.count_users()
        response.set_cookie('username', 'admin')
        response.set_cookie('user_id', str(1))
        return template("/home/yunqi/git_version/INFO2222-Group-Project/template/views/manager.tpl", users=users, count=count)

    print("username: "+username)
    print("password: "+password)
    login = sql_db.check_credentials(username,password)
    if login:
        user_id = sql_db.get_userid_by_username_and_password(username, password)
        response.set_cookie('username',username)
        response.set_cookie('user_id',str(user_id))
        return page_view("index", name=username)
    else:
        return "<p>Wrong password or username, please try again. Click</p> <a href='/login'>here</a>"

#-----------------------------------------------------------------------------
# About
#-----------------------------------------------------------------------------

#html contents
def get_html_home():
    return page_view("html/html-home")

def get_html_introduction():
    return page_view("html/html-introduction")

def get_html_basic():
    return page_view("html/html-basic")

def get_html_elements():
    return page_view("html/html-elements")

#CSS contents
def get_css_home():
    return page_view("Css/css-home")

def get_css_introduction():
    return page_view("Css/css-introduction")

def get_css_syntax():
    return page_view("Css/css-syntax")

def get_css_selectors():
    return page_view("Css/css-selectors")

def get_css_how():
    return page_view("Css/css-how")




def get_express_intro():
    return page_view("Express/express-intro")

def get_express_routing():
    return page_view("Express/express-routing")

def get_express_template():
    return page_view("Express/express-template")

def get_express_middleware():
    return page_view("Express/express-middleware")

def get_express_database():
    return page_view("Express/express-database")

def about():
    '''
        about
        Returns the view for the about page
    '''
    return page_view("about", garble=about_garble())

def contact():
    '''
        contact
        Returns the view for the about page
    '''
    return page_view("contact")

def HTML():
    '''
    contact
    Returns the view for the about page
    '''
    return page_view("htmlcss-home")

def JavaScript():
    '''
    contact
    Returns the view for the about page
    '''
    return page_view("JavaScript")

def css():
    '''
    contact
    Returns the view for the about page
    '''
    return page_view("css")


def get_manager():
    return page_view("manager")

def get_forum():
    '''
    contact
    Returns the view for the about page
    '''
    db = sql_post.SQLDatabasePost("post.db")
    posts = db.get_allposts()
    db_comments= sql_comment.SQLDatabaseComment("comment.db")
    db_users = sql.SQLDatabase("user.db")
    users = db_users.get_allusers()
    user_id = request.get_cookie('user_id')
    if user_id!='1':
        if_mute = db_users.get_if_mute(int(user_id))
#    else:
#        if_mute = db_users.get_admin_if_mute()
    my_dict={}
    for post in posts:
        if db_comments.get_comment_by_postid(post['post_id'])==None:
            number_of_comments =0
        else:
            number_of_comments = len(db_comments.get_comment_by_postid(post['post_id']))
        my_dict[str(post['post_id'])]=number_of_comments
    return template("/home/yunqi/git_version/INFO2222-Group-Project/template/views/forum.tpl",posts = posts,my_dict=my_dict,users=users,mute=if_mute,user_id=user_id)
    # return page_view.simple_render("forum",posts)

def get_add_post():
    return page_view("add_post")

def get_add_user():
    return page_view("add_user")

def add_post(title,username,content,id):
    db_user = sql.SQLDatabase("user.db")
    db = sql_post.SQLDatabasePost("post.db")
    postTime = db_user.get_post_time(id)
    last = datetime.datetime(int(postTime.split(":")[0]),int(postTime.split(":")[1]),int(postTime.split(":")[2]),int(postTime.split(":")[3]),int(postTime.split(":")[4]),int(postTime.split(":")[5]))
    now = datetime.datetime.now()
    diff = (now -last).total_seconds()/60
    if diff <1:
        return "<p>You are posting or commenting too frequent. Or you just registered this account. There is a 1 minute cool down before you can leave a post or comment. </p><a href='/forum'>Click here to go back to forum</a>"
    else:
        db_user.add_post_time(id)
        db.add_post(content,username,title)
        return redirect("/forum")

def get_post(post_id):
    db = sql_post.SQLDatabasePost("post.db")
    post = db.get_post(post_id)
    db = sql_comment.SQLDatabaseComment("comment.db")
    comments = db.get_comment_by_postid(post_id)
    username = request.get_cookie('username')
    user_id = request.get_cookie("user_id")
    db_user = sql.SQLDatabase("user.db")
    mute = db_user.get_if_mute(int(user_id))
    return template("/home/yunqi/git_version/INFO2222-Group-Project/template/views/post.tpl",post = post, comments = comments,username=username,mute=mute)

def delete_single_post(post_id):
    db = sql_post.SQLDatabasePost("post.db")
    db.delete_single_post(post_id)
    posts = db.get_allposts()
    db_comments = sql_comment.SQLDatabaseComment("comment.db")
    db_comments.delete_all_comments(post_id)
    db_users = sql.SQLDatabase("user.db")
    users = db_users.get_allusers()
    user_id = request.get_cookie('user_id')
    if_mute = db_users.get_if_mute(int(user_id))
    my_dict = {}
    for post in posts:
        if db_comments.get_comment_by_postid(post['post_id'])==None:
            number_of_comments = 0
        else:
            number_of_comments = len(db_comments.get_comment_by_postid(post['post_id']))
        my_dict[str(post['post_id'])] = number_of_comments
    return template("/home/yunqi/git_version/INFO2222-Group-Project/template/views/forum.tpl", posts=posts, my_dict=my_dict,users=users,mute=if_mute)

def get_allusers():
    db = sql.SQLDatabase("user.db")
    users = db.get_allusers()
    count = db.count_users()
    return template("/home/yunqi/git_version/INFO2222-Group-Project/template/views/manager.tpl",users= users,count = count)

def delete_single_user(username):
    db = sql.SQLDatabase("user.db")
    db.delete_single_user(username)
    users = db.get_allusers()
    count = db.count_users()
    return template("/home/yunqi/git_version/INFO2222-Group-Project/template/views/manager.tpl", users=users, count=count)

def delete_all_users():
    db = sql.SQLDatabase("user.db")
    db.delete_all_users()
    users = db.get_allusers()
    count = db.count_users()
    return template("/home/yunqi/git_version/INFO2222-Group-Project/template/views/manager.tpl", users=users, count=count)

def mute_single_users(user_id):
    db = sql.SQLDatabase("user.db")
    db.mute_single_user(user_id)
    users = db.get_allusers()
    count = db.count_users()
    return template("/home/yunqi/git_version/INFO2222-Group-Project/template/views/manager.tpl", users=users, count=count)

def unmute_single_users(user_id):
    db = sql.SQLDatabase("user.db")
    db.unmute_single_user(user_id)
    users = db.get_allusers()
    count = db.count_users()
    return template("/home/yunqi/git_version/INFO2222-Group-Project/template/views/manager.tpl", users=users, count=count)

def add_comment(username,content,post_id):
    db = sql_comment.SQLDatabaseComment("comment.db")
    comments = db.get_comment_by_postid(post_id)
    db_user = sql.SQLDatabase("user.db")
    postTime = db_user.get_post_time(id)
    last = datetime.datetime(int(postTime.split(":")[0]),int(postTime.split(":")[1]),int(postTime.split(":")[2]),int(postTime.split(":")[3]),int(postTime.split(":")[4]),int(postTime.split(":")[5]))
    now = datetime.datetime.now()
    diff = (now -last).total_seconds()/60
    postTime = db_user.get_post_time(id)
    db_user.add_post_time(id)
    if diff <1:
        return "<p>You are posting or commenting too frequent. Or you just registered this account. There is a 1 minute cool down before you can leave a post or comment. </p><a href='/forum/{}'>Click here to go back to forum</a>".format(post_id)
    else:
        db_user.add_post_time(id)
        db.add_comment(username,content,post_id)
        return redirect("/forum/{}".format(post_id))
    

def delete_single_comment(post_id,comment_id):
    db = sql_comment.SQLDatabaseComment("comment.db")
    db.delete_single_comment(comment_id)
    return redirect("/forum/{}".format(post_id))

def pin_post(post_id):
    db_post = sql_post.SQLDatabasePost("post.db")
    post = db_post.pin_unpin_post("TRUE",post_id)
    return redirect("/forum")

def unpin_post(post_id):
    db_post = sql_post.SQLDatabasePost("post.db")
    post = db_post.pin_unpin_post("FALSE",post_id)
    return redirect("/forum")

    
# Returns a rget_postandom string each time
def about_garble():
    '''
        about_garble
        Returns one of several strings for the about page
    '''
    garble = ["leverage agile frameworks to provide a robust synopsis for high level overviews.",
    "iterate approaches to corporate strategy and foster collaborative thinking to further the overall value proposition.",
    "organically grow the holistic world view of disruptive innovation via workplace change management and empowerment.",
    "bring to the table win-win survival strategies to ensure proactive and progressive competitive domination.",
    "ensure the end of the day advancement, a new normal that has evolved from epistemic management approaches and is on the runway towards a streamlined cloud solution.",
    "provide user generated content in real-time will have multiple touchpoints for offshoring."]
    return garble[random.randint(0, len(garble) - 1)]



#-----------------------------------------------------------------------------
# htmlcss-home
#-----------------------------------------------------------------------------

def htmlcss_home():
    return page_view("htmlcss-home")



#-----------------------------------------------------------------------------
# Debug
#-----------------------------------------------------------------------------

def debug(cmd):
    try:
        return str(eval(cmd))
    except:
        pass

#-----------------------------------------------------------------------------
# 404
# Custom 404 error page
#-----------------------------------------------------------------------------

def handle_errors(error):
    error_type = error.status_line
    error_msg = error.body
    return page_view("error", error_type=error_type, error_msg=error_msg)

def register_form():
    return page_view("register")

def get_js_intro():
    return page_view("Javascript/js-intro")

def get_js_comparison():
    return page_view("Javascript/js-comparison")

def get_js_dates():
    return page_view("Javascript/js-dates")

def get_js_statements():
    return page_view("Javascript/js-Statements")

def get_js_syntax():
    return page_view("Javascript/js-syntax")

def get_bottle_intro():
    return page_view("WebFrameworks/bottle-intro")

def get_bottle_congen():
    return page_view("WebFrameworks/bottle-congen")

def get_bottle_installation():
    return page_view("WebFrameworks/bottle-installation")

def get_bottle_routing():
    return page_view("WebFrameworks/bottle-routing")
