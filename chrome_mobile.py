from selenium import webdriver
from time import sleep

WIDTH = 768
HEIGHT = 1024
PIXEL_RATIO = 3.0
UA = 'Mozilla/5.0 (Linux; Android 4.1.1; GT-N7100 Build/JRO03C) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/35.0.1916.138 Mobile Safari/537.36 T7/6.3'

mobileEmulation = {"deviceMetrics": {"width": WIDTH, "height": HEIGHT, "pixelRatio": PIXEL_RATIO}, "userAgent": UA}
options = webdriver.ChromeOptions()
options.add_experimental_option('mobileEmulation', mobileEmulation)

#insert in the folder chromedriver.exe, download from https://chromedriver.chromium.org/

driver = webdriver.Chrome(r"C:\Users\Giorgio\Desktop\py\chromedriver.exe", chrome_options=options)
driver.get('https://www.zoomingin.net')


#for close the browser after 20 seconds enable the following 2 lines
#sleep(20)
#driver.close()
