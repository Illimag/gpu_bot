import time
from selenium import webdriver

driver = webdriver.Chrome('/usr/bin/chromedriver')  # Optional argument, if not specified will search path.



RTX3070LINK1 = "https://www.bestbuy.com/site/nvidia-geforce-rtx-3070-8gb-gddr6-pci-express-4-0-graphics-card-dark-platinum-and-black/6429442.p?skuId=6429442"
RTX3070LINK2 = "https://www.bestbuy.com/site/gigabyte-geforce-rtx-3070-8g-gddr6-pci-express-4-0-graphics-card-black/6437912.p?skuId=6437912"
XBOXONETEST = "https://www.bestbuy.com/site/microsoft-xbox-one-s-1tb-console-bundle-white/6415222.p?skuId=6415222"



driver.get(RTX3070LINK1)




time.sleep(5) # Let the user actually see something!
print('test')
time.sleep(5) # Let the user actually see something!
driver.quit()