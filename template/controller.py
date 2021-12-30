'''
    This file will handle our typical Bottle requests and responses
    You should not have anything beyond basic page loads, handling forms and
    maybe some simple program logic
'''

from bottle import route, get, post, error, request,response,redirect, static_file

import model
import sql
import os
#-----------------------------------------------------------------------------
# Static file paths
#-----------------------------------------------------------------------------
# Allow image loading
from pojo.User import User
from pojo.Users import Users
from parser import Parser

pars = Parser()

@route('/img/<picture:path>')
def serve_pictures(picture):
    '''
        serve_pictures

        Serves images from static/img/

        :: picture :: A path to the requested picture

        Returns a static file object containing the requested picture
    '''
    return static_file(picture, root='/home/yunqi/git_version/INFO2222-Group-Project/template/static/img/')

#-----------------------------------------------------------------------------

# Allow CSS
@route('/css/<css:path>')
def serve_css(css):
    '''
        serve_css

        Serves css from static/css/

        :: css :: A path to the requested css

        Returns a static file object containing the requested css
    '''
    return static_file(css, root='/home/yunqi/git_version/INFO2222-Group-Project/template/static/css/')

#-----------------------------------------------------------------------------

# Allow javascript
@route('/js/<js:path>')
def serve_js(js):
    '''
        serve_js

        Serves js from static/js/

        :: js :: A path to the requested javascript

        Returns a static file object containing the requested javascript
    '''
    return static_file(js, root='/home/yunqi/git_version/INFO2222-Group-Project/template/static/js/')

@route('/layui/<layui:path>')
def serve_layui(layui):
    '''
        serve_layui

        Serves js from static/layui/

        :: layui :: A path to the requested javascript

        Returns a static file object containing the requested javascript
    '''
    return static_file(layui, root='/home/yunqi/git_version/INFO2222-Group-Project/template/static/layui/')



#-----------------------------------------------------------------------------
# Pages
#-----------------------------------------------------------------------------

# Redirect to login
@get('/')
@get('/home')
def get_index():
    '''
        get_index

        Serves the index page
    '''
    # return f"served from {os.getpid()}"
    return model.index()

#-----------------------------------------------------------------------------

# Display the login page
@get('/login')
def get_login_controller():
    '''
        get_login

        Serves the login page
    '''
    return model.login_form()


@get('/register')
def get_register():
    return model.register_form()



#-----------------------------------------------------------------------------

# Attempt the login
@post('/login')
def post_login():
    '''
        post_login

        Handles login attempts
        Expects a form containing 'username' and 'password' fields
    '''

    # Handle the form processing
    username = request.forms.get('username')
    password = request.forms.get('password')
    username= pars.encode(username)[0]
    password= pars.encode(password)[0]
    # Call the appropriate method
    return model.login_check(username, password)

@post('/register')
def post_register():
    '''
        post_login

        Handles login attempts
        Expects a form containing 'username' and 'password' fields
    '''

    # Handle the form processing
    username = request.forms.get('username')
    password = request.forms.get('password')
    username, malicious1 = pars.encode(username)
    password, malicious2 = pars.encode(password)
    if malicious1 == True or malicious2 ==True:
        log = open("/home/yunqi/git_version/INFO2222-Group-Project/template/log.txt","a")
        log.write("username: {},password: {} \n".format(pars.decode(username),pars.decode(password)))
        log.close() #to change file access modes
        return "<p>Username or password contain illegal string, click here to try again: </p><a href='/register'>Register again</a>"
    email = request.forms.get('email')
    user = User(None,username,password,email)
    # Call the appropriate method
    return model.register(user)


#-----------------------------------------------------------------------------

@get('/about')
def get_about():
    '''
        get_about

        Serves the about page
    '''
    return model.about()
#-----------------------------------------------------------------------------

@get('/contact')
def get_contact():
    '''
        get_contact

        Serves the contact page
    '''
    return model.contact()

@get('/HTML')
def get_html():
    '''
        get_html

        Serves the html page
    '''
    if request.get_cookie('username')==None:
        return model.login_form()
    return model.HTML()

@get('/css')
def get_css():
    '''
        get_css

        Serves the css page
    '''
    if request.get_cookie('username')==None:
        return model.login_form()
    return model.css()

@get('/JavaScript')
def get_javascript():
    '''
        get_Javascript

        Serves the javascript page
    '''
    if request.get_cookie('username')==None:
        return model.login_form()
    return model.JavaScript()

@get('/htmlcss-home')
def get_htmlcss_home():
    '''
        get_about

        Serves the about page
    '''
    if request.get_cookie('username')==None:
        return model.login_form()
    return model.htmlcss_home()

@get('/html-home')
def get_html_home():
    return model.get_html_home()

@get('/html-introduction')
def get_html_introduction():
    return model.get_html_introduction()

@get('/html-basic')
def get_html_basic():
    return model.get_html_basic()

@get('/html-elements')
def get_html_elements():
    return model.get_html_elements()


@get('/css-home')
def get_css_home():
    return model.get_css_home()

@get('/css-introduction')
def get_css_introduction():
    return model.get_css_introduction()

@get('/css-syntax')
def get_css_syntax():
    return model.get_css_syntax()

@get('/css-selectors')
def get_css_selectors():
    return model.get_css_selectors()

@get('/css-how')
def get_css_how():
    return model.get_css_how()









@get('/express-intro')
def get_express_intro():
    return model.get_express_intro()

@get('/express-routing')
def get_express_routing():
    return model.get_express_routing()

@get('/express-database')
def get_express_database():
    return model.get_express_database()

@get('/express-middleware')
def get_express_middleware():
    return model.get_express_middleware()

@get('/express-template')
def get_express_template():
    return model.get_express_template()


@get('/add')
def add_post():
    '''
        get_addPost

        Serves the addPost page
    '''
    return model.add_post()

@post('/addUser')
def add_user():
    username = request.forms.get('username')
    password = request.forms.get('password')
    email = request.forms.get('email')
    user = User(None,username,password,email)
    # Call the appropriate method
    return model.add_user(user)


#-----------------------------------------------------------------------------
# Help with debugging
@post('/debug/<cmd:path>')
def post_debug(cmd):
    return model.debug(cmd)




#-----------------Discussion Forum-------------------------------------------
# overview
@get('/forum')
def get_discussion_forum():
    # a list of dictionaries of post
    #posts = model.get_allposts()
    #model.get_forum(posts)
    # render /discussion-forum

    #test
    if request.get_cookie('username')==None:
        return model.login_form()
    return model.get_forum()
# example


@get('/add_post')
def get_add_post():
    return model.get_add_post()

@get('/post/<post_id:int>')
def delete_single_post_page(post_id):
    return model.delete_single_post(post_id)

@get('/comment/<post_id:int>/<comment_id:int>')
def delete_single_comment(post_id,comment_id):
    return model.delete_single_comment(post_id,comment_id)

@post('/new-post')
def post_debug():
    username = pars.encode(request.forms.get('usrname'))[0]
    title =  pars.encode(request.forms.get("title"))[0]
    content =  pars.encode(request.forms.get('content'))[0]
    id = request.get_cookie("user_id")
    return model.add_post(title,username,content,int(id))

# clicked a post
@get('/forum/<post_id:int>')
def get_single_post_page(post_id):
    return model.get_post(post_id)


@get('/manager/<username>')
def delete_single_user(username):
    return model.delete_single_user(username)

@get('/manager/all')
def delete_all_users():
    return model.delete_all_users()

@get('/manager/mute/<user_id:int>')
def mute_single_users(user_id):
    return model.mute_single_users(user_id)

@get('/manager/unmute/<user_id:int>')
def unmute_single_users(user_id):
    return model.unmute_single_users(user_id)

@get('/pin/<post_id:int>')
def pin_post(post_id):
    return model.pin_post(post_id)

@get('/unpin/<post_id:int>')
def unpin_post(post_id):
    return model.unpin_post(post_id)
    

@post('/new-comment/<post_id:int>')
def add_comment(post_id):
    username = pars.encode(request.forms.get('usrname'))[0]
    content =  pars.encode(request.forms.get('content'))[0]
    return model.add_comment(username,content,post_id)

#-----------------------------------------------------------------------------
# admin background
@get("/manager")
def get_users():
    return model.get_allusers()

@get("/add_user")
def get_add_users():
    return model.get_add_user()

@get('/js-intro')
def get_js_intro():
    return model.get_js_intro()

@get('/js-comparison')
def get_js_comparison():
    return model.get_js_comparison()

@get('/js-dates')
def get_js_dates():
    return model.get_js_dates()

@get('/js-statements')
def get_js_statements():
    return model.get_js_statements()

@get('/js-syntax')
def get_js_syntax():
    return model.get_js_syntax()

@get('/bottle-intro')
def get_bottle_intro():
    return model.get_bottle_intro()

@get('/bottle-congen')
def get_bottle_congen():
    return model.get_bottle_congen()

@get('/bottle-installation')
def get_bottle_installation():
    return model.get_bottle_installation()

@get('/bottle-routing')
def get_bottle_routing():
    return model.get_bottle_routing()


#-----------------------------------------------------------------------------

# 404 errors, use the same trick for other types of errors
@error(404)
def error(error):
    return model.handle_errors(error)


