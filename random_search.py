#!/usr/bin/env python3

import random
import webbrowser
import time
import os
name= input ("What content of the text file do you want to search on web? ")
file=open(name)
cicli=int(input ("how many lines do you want to search for:"))

for n in range(cicli):
        a=n+1
        print('iteration',+(a),'of',+(cicli))
        lettura=file.readline()
        value=random.randint(4,13)
        print(lettura)
        
        webbrowser.open('https://www.bing.com/search?q='+str(lettura))
        time.sleep(value)
        #firefox browser
        #webbrowser.get("firefox").open('https://www.bing.com/search?q='+str(lettura))            

time.sleep(10)
#os.system("taskkill /im chrome.exe /f")

