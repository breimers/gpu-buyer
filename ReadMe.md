# GPU Buyer
Vendor specific scripts for monitoring the stock of computer hardware and automating the process up to checkout.
Due to both site regulations and safety concerns, this project will *not* be adding features to automatically complete payment or the transaction process. 

This script takes you from opening the browser to beginning checkout, in order to save time and level the playing field with bots and power users.

## Setup
- Requires Google Chrome
- Requires Python 3.9 or higher
- Requires Pip 22 or higher for installing dependencies
- Requires a VPN (personally I use [Proton](https://account.protonvpn.com/signup?plan=free&ref=noupsell), but it doesn't really matter)


## Newegg
The Newegg script uses Selenium to quickly navigate across the site and add the product to your cart. When you run this script, a Chrome window will open on its own, please do not interact with it until it's on the checkout page.

Provide keywords for your product such as the model, brand, make etc. Additionally, you can provide words to filter out other product in the exclude variable. See the examples below for more detail.

### Get Help
```bash
python3 ./newegg.py --help
...
usage: newegg.py [-h] --email EMAIL --password PASSWORD [--keywords KEYWORDS] [--excludes EXCLUDES] [--install]

options:
  -h, --help            show this help message and exit
  --email EMAIL, -e EMAIL
                        Newegg account email
  --password PASSWORD, -p PASSWORD
                        Newegg account password
  --keywords KEYWORDS, -k KEYWORDS
                        Product keywords
  --excludes EXCLUDES, -x EXCLUDES
                        Product exclusions
  --install, -i         Installs dependencies (recommended on first run)
```

### Run script
```bash
python3 ./newegg.py --email joe.schmo@tech.org --password badpass123 --keywords 5080,gigabyte --excludes desktop,pc [--install]
```

## Amazon
Coming Soon!

## BestBuy
Coming Soon!
