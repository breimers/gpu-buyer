import os
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

from time import sleep

SKU_MAP = {
    "RTX.5080": 6614153,
    "RTX.5090": 6614151,
    "CORSAIR.32G": "6562314"
}

BASE_URL = "https://api.bestbuy.com/v1"

PRODUCTS_API = "/products/"

API_KEY = os.getenv("BESTBUY_KEY", "zp44vUERZmGMgxHmlezEj3me6upTNmkz")

def get_product_url_by_sku(sku=SKU_MAP["CORSAIR.32G"]):
    res = requests.get(
        url = BASE_URL + PRODUCTS_API + str(sku) + ".json",
        params={"apiKey": API_KEY}
    )
    product_data = res.json()
    print(product_data)

email = "b.a.reimers@gmail.com"
password = "..."
# product_url = get_product_url_by_sku()
product_url = "https://www.bestbuy.com/site/corsair-vengeance-rgb-32gb-2x16gb-ddr5-7200mhz-c34-udimm-desktop-memory-black/6554930.p?skuId=6554930"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--user-agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9"')
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://bestbuy.com/login")
sleep(0.5)

login_email = driver.find_element(by=By.CLASS_NAME, value="tb-input")
login_email.send_keys(email)
login_email.submit()
sleep(2)
radio_fields = driver.find_elements(by=By.CLASS_NAME, value="cia-signin-options__container")
pw_field = radio_fields[-1]
pw_field.click()
sleep(0.5)
pw_field = driver.find_element(by=By.ID, value="fld-p1")
pw_field.send_keys(password)
sleep(0.5)
pw_field.submit()
sleep(5)
pw_field.submit()
sleep(5)
driver.get(product_url)
sleep(3)
# ship_options = driver.find_elements(by=By.CLASS_NAME, value="c-tile border rounded v-base")
# print(ship_options)
# ship_btn = ship_options[-1]
# ship_btn.click()
add_to_cart = driver.find_element(by=By.CLASS_NAME, value="c-button c-button-primary c-button-lg c-button-block c-button-icon c-button-icon-leading add-to-cart-button ")
add_to_cart.click()
sleep(1)
driver.get("https://www.bestbuy.com/cart")
sleep(0.5)
