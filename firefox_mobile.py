import os
import selenium.webdriver as webdriver
from time import sleep

user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/12.0 Mobile/15A372 Safari/604.1'
#if you want to change user agent open firefox> Ctrl+Alt+m and choose the new user_agent
profile= webdriver.FirefoxProfile()
profile.set_preference('general.useragent.override',user_agent)
#insert in the folder geckodriver.exe, download from https://github.com/mozilla/geckodriver/releases
FireFoxDriverPath= os.path.join(os.getcwd(), 'Drivers',r"C:\Users\Giorgio\Desktop\py\geckodriver.exe")
url='https://www.bing.com'
browser=webdriver.Firefox(executable_path=FireFoxDriverPath,firefox_profile=profile)
browser.get(url)

#for close the browser after 20 seconds enable the following 2 lines
#sleep(20)
#browser.close()
