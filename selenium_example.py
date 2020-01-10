import re
import config

from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.codechef.com/")

assert "Programming Competition,Programming Contest,Online Computer Programming" in driver.title

username = driver.find_element_by_id("edit-name")
username.clear()
username.send_keys(config.DATACOUP_USERNAME)

password = driver.find_element_by_id("edit-pass")
password.clear()
password.send_keys(config.DATACOUP_PASSWORD)

driver.find_element_by_id("edit-submit").click()

src = driver.find_element_by_class_name("right").text

start = 'Hello <a>'
end = '<i class="fa fa-caret-down" aria-hidden="true"></i></a>'

user = re.search('%s(.*)%s' % (start, end), src)

print(src)


# <li class="loggedin-user no-select">
#   <span class="left">
#   <a href="/users/squale96"><div class="picture"><img src="/sites/all/themes/abessive/images/user_default_thumb.jpg" width="30px" height="30px"></div></a>
#   </span>
  
#   <span class="right">
#   Hello <a>squale96<i class="fa fa-caret-down" aria-hidden="true"></i></a>
#   <ul class="user-dropdown" style="display: none;">
#   <span class="caret"></span>
#   <li><a href="/users/squale96" title="Edit Your Account">Account</a></li>
#   <li><a href="/users/squale96/edit">Edit Profile</a></li>
#   <li><a href="https://goodies.codechef.com/my-laddus/">My Laddus</a></li>
#   <li><a href="/apps">My Apps</a></li>
#   <li><a href="/todos">My Todos</a></li>
#   <li><a href="/sets">My Sets</a></li>
#   <li><a href="/certificates">My Certificates</a></li>
#   <li><a href="/users/squale96/teams">My Teams</a></li>
#     <li><a href="/teams/invites">Team Invites</a></li>
#   <li><a href="/referral">Referrals</a></li>
#   </ul>            </span></li>