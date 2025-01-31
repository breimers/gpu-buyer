import sys
import argparse
import logging
import subprocess
from datetime import datetime
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

handler = logging.StreamHandler(sys.stdout)
logger = logging.getLogger("stdout")
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

def install_dependencies():
    subprocess.run(['pip', 'install', 'requests', 'selenium']) 

def newegg_loop(email, pw, keywords=["rx7800"], excludes=["desktop"]):
    logger.info(f"Time: {str(datetime.now())} | Stage: Starting Newegg GPU Buyer")
    logger.info(f"Time: {str(datetime.now())} | Info: Keywords({str(keywords)}) - Excludes: ({str(excludes)})")
    home_url = "https://www.newegg.com"
    login_url = "https://secure.newegg.com/login/signin?nextpage=https%3A%2F%2Fwww.newegg.com%2F"
    search_url = "https://www.newegg.com/p/pl?d="
    cart_url = "https://secure.newegg.com/shop/cart"
    cart_active = False
    logger.info(f"Time: {str(datetime.now())} | Info: Configuring Selenium for Chrome")
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--user-agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"')
    driver = webdriver.Chrome(options=chrome_options)
    tries = 10
    search_url = f"{search_url}{str("+".join(keywords))}"
    logger.info(f"Time: {str(datetime.now())} | Info: Go to Newegg Homepage")
    driver.get(home_url)
    sleep(1)
    while True:
        logger.info(f"Time: {str(datetime.now())} | Stage: Authenticate to Newegg")
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(home_url)
        driver.get(login_url)
        sleep(1)
        emailBox = driver.find_element(By.ID, "labeled-input-signEmail")
        emailBox.send_keys(email)
        sleep(0.2)
        emailBtn = driver.find_element(By.ID, "signInSubmit")
        emailBtn.click()
        sleep(3)
        pw_box = driver.find_element(By.ID, "labeled-input-password")
        pw_box.send_keys(pw)
        submit = driver.find_element(By.ID, "signInSubmit")
        submit.click()
        sleep(1)
        logger.info(f"Time: {str(datetime.now())} | Stage: Searching for product")
        driver.get(search_url)
        sleep(3)
        for i in range(tries):
            try:
                logger.info(f"Time: {str(datetime.now())} | Info: Starting attempt {i}")
                logger.info(f"Time: {str(datetime.now())} | Info: Locating eligible products")
                try:
                    elements = driver.find_elements(By.XPATH, "//button[contains( text( ), 'Add to cart')]")
                except:
                    logger.info(f"Time: {str(datetime.now())} | Info: No eligible products found")
                    continue
                for element in elements:
                    logger.debug(f"Time: {str(datetime.now())} | Debug: Validating product match")
                    title = element.get_attribute("title")
                    if all(kw.lower() in title.lower() for kw in keywords) and not any(ex.lower() in title.lower() for ex in excludes):
                        logger.info(f"Time: {str(datetime.now())} | Info: Added product to cart")
                        element.send_keys(Keys.RETURN)
                        cart_active = True
                        sleep(3)
                        break
                    else:
                        logger.debug(f"Time: {str(datetime.now())} | Debug: Product description does not meet criteria")
                if cart_active:
                    logger.info(f"Time: {str(datetime.now())} | Stage: Checkout")
                    driver.get(cart_url)
                    logger.info(f"Time: {str(datetime.now())} | Info: Page will timeout in 5 minutes")
                    btn2 = driver.find_element(By.XPATH, "//button[contains( text( ), ' Secure Checkout ')]")
                    btn2.click()
                    sleep(300)
                    logger.info(f"Time: {str(datetime.now())} | Info: Timeout")
                else:
                    raise(RuntimeWarning("No items eligible for cart..."))
            except Exception as e:
                logger.error(f"Error: {e}\n{e.__context__}")
                driver.get(search_url)
                sleep(3)
                continue
        driver.close()
        logger.warning(f"Time: {str(datetime.now())} | Warning: Failed to locate and/or add product to cart, trying again.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--email", "-e", type=str, required=True, help="Newegg account email")
    parser.add_argument("--password", "-p", type=str, required=True, help="Newegg account password")
    parser.add_argument("--keywords", "-k", type=str, required=False, default="rtx,5090", help="Product keywords")
    parser.add_argument("--excludes", "-x", type=str, required=False, default="desktop", help="Product exclusions")
    parser.add_argument("--install", "-i", action='store_true', help="Installs dependencies (recommended on first run)")
    args = parser.parse_args()
    if args.install:
        logger.warning(f"Time: {str(datetime.now())} | Warning: Installing dependencies...")
        install_dependencies()
    keywords = args.keywords.split(",") if args.keywords else None
    excludes = args.excludes.split(",") if args.excludes else None
    if keywords:
        keywords = list(keywords) if not isinstance(keywords, list) else keywords
    if excludes:
        excludes = list(excludes) if not isinstance(excludes, list) else excludes
    newegg_loop(args.email, args.password, keywords, excludes)