from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

query = "rtx 4060"
email = "b.a.reimers@gmail.com"
password = "Molly5683"
login = "https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fref%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--user-agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9"')
driver = webdriver.Chrome(options=chrome_options)

driver.get(login)
sleep(2)
login_email = driver.find_element(by=By.NAME, value="email")
login_email.send_keys(email)
login_email.submit()
sleep(2)

pw_box = driver.find_element(by=By.ID, value="ap_password")
pw_box.send_keys(password)
sleep(2)
pw_box.submit()


# driver.get("https://amazon.com")
# home_search_bar = driver.find_element(by=By.ID, value="twotabsearchtextbox")
# home_search_bar.send_keys(query)
# home_search_bar.submit()
sleep(30)