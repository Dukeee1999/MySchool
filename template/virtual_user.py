import requests
import time
import getpass
import selenium
import time
import sys
import csv
import sql_post
import sql
import getpass



from selenium import webdriver

#------------------------------------------------
from selenium.webdriver.common.keys import Keys

default_target = "https://10.86.225.9/"


# put test db with this virtual_user.py together
posts_sql = sql_post.SQLDatabasePost("test_post.db")
users_sql = sql.SQLDatabase("test_user.db")
# input your web driver path here
web_driver_path  = '/Users/floraison/Documents/INFO2222-Group-Project1234/template/chromedriver'

#------------------------------------------------
# Useage:
# python canvas_group_scraper.py <target groups page>
#------------------------------------------------

def vir_user_main(target):
    driver = webdriver.Chrome(executable_path=web_driver_path)
    groups = {}

    driver.get(default_target)

    time.sleep(1)
    login_button = driver.find_element_by_id("login")
    login_button.click()


    time.sleep(1)
    print("click login pass")


    username = "test"
    password = "test123"
    email = "email@.com"


    print("Logging in")

    driver.get("http://localhost:8090/login")

    register_button = driver.find_element_by_xpath('//a[contains(@href, "/register")]')
    register_button.click()
    time.sleep(2)

    # Enter username
    register_username_field = driver.find_element_by_name("username")
    register_username_field.clear()
    register_username_field.send_keys(username)

    time.sleep(2)

    # Enter password
    register_password_field = driver.find_element_by_name("password")
    register_password_field.clear()
    register_password_field.send_keys(password)

    time.sleep(2)

    # Confirm password
    register_confirm_field = driver.find_element_by_name("confirm")
    register_confirm_field.clear()
    register_confirm_field.send_keys(password)

    time.sleep(2)

    # Enter email
    register_email_field = driver.find_element_by_name("email")
    register_email_field.clear()
    register_email_field.send_keys(email)

    time.sleep(2)

    register_button = driver.find_element_by_id("submit_btn")
    register_button.click()

    time.sleep(2)



    # Enter username
    username_field = driver.find_element_by_name("username")
    username_field.clear()
    username_field.send_keys(username)

    # Enter password
    password_field = driver.find_element_by_name("password")
    password_field.clear()
    password_field.send_keys(password)

    # Hit the button
    login_button = driver.find_element_by_id("submit_btn")
    login_button.click()

    time.sleep(2)

    print("Logged in!")

    time.sleep(2)

    forum_button = driver.find_element_by_id("forum")
    forum_button.click()

    time.sleep(2)

    driver.execute_script("window.scrollTo(0, 3000)")

    time.sleep(1)

    post_question_button = driver.find_element_by_id("post_question")
    post_question_button.click()

    time.sleep(2)



    test_post_title = "title_test"
    test_post_content = "content_test"


    title_field = driver.find_element_by_id("L_title")
    title_field.clear()
    title_field.send_keys(test_post_title)

    content_field = driver.find_element_by_xpath('//*[@id="content"]')
    driver.execute_script("arguments[0].click();", content_field)
    driver.execute_script("arguments[0].click();", content_field)
    time.sleep(2)
    driver.execute_script("arguments[0].value = ' +test_post_content+ ';", content_field)
    time.sleep(2)


    time.sleep(2)

    post_now_button = driver.find_element_by_class_name("layui-btn")
    post_now_button.click()

    time.sleep(2)

    driver.execute_script("window.scrollTo(0, 3000)")

    post_length = str(len(posts_sql.get_allposts()))
    temp_url = "http://localhost:8090/forum/"



    temp_xpath = '//a[contains(@href, "/forum/' + post_length + '")]'
    comment_test_button = driver.find_element_by_xpath(temp_xpath)
    comment_test_button.click()

    time.sleep(2)

    test_comment = "blah"

    comment_field = driver.find_element_by_xpath('//*[@id="content"]')
    driver.execute_script("arguments[0].click();", comment_field)
    driver.execute_script("arguments[0].click();", comment_field)
    time.sleep(2)
    driver.execute_script("arguments[0].value = ' +test_comment+ ';", comment_field)
    time.sleep(2)


    post_now_comment_button = driver.find_element_by_class_name("layui-btn")
    post_now_comment_button.click()

    time.sleep(2)

    gohome_button = driver.find_element_by_xpath('//a[contains(@href, "/home")]')
    gohome_button.click()

    time.sleep(2)

    about_button = driver.find_element_by_xpath('//a[contains(@href, "/about")]')
    about_button.click()
    time.sleep(2)

    contact_button = driver.find_element_by_xpath('//a[contains(@href, "/contact")]')
    contact_button.click()
    time.sleep(2)


    html_home_button = driver.find_element_by_xpath('//a[contains(@href, "/html-home")]')
    html_home_button.click()

    #driver.get("http://localhost:8090/html-home")

    time.sleep(2)

    html_intro_button = driver.find_element_by_xpath('//a[contains(@href, "html-introduction")]')
    html_intro_button.click()
    time.sleep(2)

    html_basic_button = driver.find_element_by_xpath('//a[contains(@href, "html-basic")]')
    html_basic_button.click()
    time.sleep(2)

    html_elements_button = driver.find_element_by_xpath('//a[contains(@href, "html-elements")]')
    html_elements_button.click()
    time.sleep(2)

    #css
    css_home_button = driver.find_element_by_xpath('//a[contains(@href, "/css-home")]')
    css_home_button.click()
    time.sleep(2)

    driver.get("http://localhost:8090/css-home")

    css_intro_button = driver.find_element_by_xpath('//a[contains(@href, "css-introduction")]')
    css_intro_button.click()
    time.sleep(2)

    css_syn_button = driver.find_element_by_xpath('//a[contains(@href, "css-syntax")]')
    css_syn_button.click()
    time.sleep(2)

    css_select_button = driver.find_element_by_xpath('//a[contains(@href, "css-selectors")]')
    css_select_button.click()
    time.sleep(2)

    css_how_button = driver.find_element_by_xpath('//a[contains(@href, "css-how")]')
    css_how_button.click()
    time.sleep(2)

    # express
    express_intro_button = driver.find_element_by_xpath('//a[contains(@href, "/express-intro")]')
    express_intro_button.click()
    time.sleep(2)

    driver.get("http://localhost:8090/express-intro")

    express_routing_button = driver.find_element_by_xpath('//a[contains(@href, "express-routing")]')
    express_routing_button.click()
    time.sleep(2)

    express_middle_button = driver.find_element_by_xpath('//a[contains(@href, "express-middleware")]')
    express_middle_button.click()
    time.sleep(2)

    express_tem_button = driver.find_element_by_xpath('//a[contains(@href, "express-template")]')
    express_tem_button.click()
    time.sleep(2)

    express_db_button = driver.find_element_by_xpath('//a[contains(@href, "express-database")]')
    express_db_button.click()
    time.sleep(2)

    # javascript
    js_intro_button = driver.find_element_by_xpath('//a[contains(@href, "/js-intro")]')
    js_intro_button.click()
    time.sleep(2)

    driver.get("http://localhost:8090/js-intro")

    js_syntax_button = driver.find_element_by_xpath('//a[contains(@href, "js-syntax")]')
    js_syntax_button.click()
    time.sleep(2)

    js_state_button = driver.find_element_by_xpath('//a[contains(@href, "js-statements")]')
    js_state_button.click()
    time.sleep(2)

    js_date_button = driver.find_element_by_xpath('//a[contains(@href, "js-dates")]')
    js_date_button.click()
    time.sleep(2)

    js_compare_button = driver.find_element_by_xpath('//a[contains(@href, "js-comparison")]')
    js_compare_button.click()
    time.sleep(2)

    # framework
    bottle_intro_button = driver.find_element_by_xpath('//a[contains(@href, "/bottle-intro")]')
    bottle_intro_button.click()
    time.sleep(2)

    driver.get("http://localhost:8090/bottle-intro")

    bottle_install_button = driver.find_element_by_xpath('//a[contains(@href, "bottle-installation")]')
    bottle_install_button.click()
    time.sleep(2)

    bottle_routing_button = driver.find_element_by_xpath('//a[contains(@href, "bottle-routing")]')
    bottle_routing_button.click()
    time.sleep(2)

    bottle_cg_button = driver.find_element_by_xpath('//a[contains(@href, "bottle-congen")]')
    bottle_cg_button.click()
    time.sleep(2)

    driver.find_element_by_xpath('//a[contains(@href, "/home")]').click()
    time.sleep(2)


    #sign out
    sign_out = driver.find_element_by_link_text("SignOut")
    sign_out.click()


    time.sleep(2)


    #admin test
    login_button = driver.find_element_by_id("login")
    login_button.click()

    time.sleep(1)
    print("click login pass")

    username = "admin"
    password = "admin123"

    print("Logging in")

    driver.get("http://localhost:8090/login")

    # Enter username
    username_field = driver.find_element_by_name("username")
    username_field.clear()
    username_field.send_keys(username)

    # Enter password
    password_field = driver.find_element_by_name("password")
    password_field.clear()
    password_field.send_keys(password)

    # Hit the button
    login_button = driver.find_element_by_id("submit_btn")
    login_button.click()

    time.sleep(2)



    add_user_button = driver.find_element_by_xpath('//a[contains(@href, "/add_user")]')
    add_user_button.click()

    time.sleep(2)
    driver.get("http://localhost:8090/add_user")

    add_username = "testing"
    add_password = "testing123"
    add_email = "blah@.com"

    # Enter username
    username_field = driver.find_element_by_name("username")
    username_field.clear()
    username_field.send_keys(add_username)

    time.sleep(2)

    # Enter password
    password_field = driver.find_element_by_name("password")
    password_field.clear()
    password_field.send_keys(add_password)

    time.sleep(2)

    email_field = driver.find_element_by_name("email")
    email_field.clear()
    email_field.send_keys(add_email)

    time.sleep(2)

    login_button = driver.find_element_by_xpath("//input[@type='submit']")
    login_button.click()

    time.sleep(2)

    go_manager_button = driver.find_element_by_xpath('//a[contains(@href, "/manager")]')
    go_manager_button.click()

    users_length = str(len(users_sql.get_allusers()))



    tem_xpath = '//a[contains(@href, "/manager/' + users_length + '")]'
    tem_mute_xpath = '//a[contains(@href, "/mute/' + users_length + '")]'
    tem_unmute_xpath = '//a[contains(@href, "/unmute/' + users_length + '")]'

    time.sleep(2)

    mute_button = driver.find_element_by_xpath(tem_mute_xpath)
    mute_button.click()

    time.sleep(2)

    unmute_button = driver.find_element_by_xpath(tem_unmute_xpath)
    unmute_button.click()

    time.sleep(2)

    delete_test_button = driver.find_element_by_xpath(tem_xpath)
    delete_test_button.click()

    time.sleep(2)

    #deleting all users
    clear_all_button = driver.find_element_by_id("clear")
    clear_all_button.click()
    time.sleep(2)

    time.sleep(2)

    driver.close()



#------------------------------------------------

def csv_groups(groups):
    with open('groups.csv', 'w') as groups_file:
        csv_writer = csv.writer(groups_file)
        for count, group in enumerate(groups):
            if len(groups[group]) > 0:
                for member in groups[group]:
                    group_line = ['group_{}'.format(count), member]
                    csv_writer.writerow(group_line)
    print("CSV written")
    return

#------------------------------------------------

if __name__ == '__main__':
    if len(sys.argv) == 1:
        target_url = default_target
    else:
        target_url = sys.argv[1]

    vir_user_main(target_url)

    print("Finished!")
