#!/usr/bin/env python3

import webbrowser
tipo=input("Search file or text?")

print(tipo)
browser=input("What browser do you want use? (google or firefox)")
print(browser)

if tipo=="file":
	name= input ("What content of the text file do you want to search on web? ")
	file=open(name)

	cicli=int(input ("how many lines of text file do you want to search?"))

	if browser=="google":
    #print("google")
    		for n in range(cicli):
            		lettura=file.readline()
            		print(lettura)
            		webbrowser.open('https://www.bing.com/search?q='+str(lettura))
	elif browser=="firefox":
    #print("firefox")
    		for n in range(cicli):
            		lettura=file.readline()
            		print(lettura)
            		webbrowser.get("firefox").open('https://www.bing.com/search?q='+str(lettura))
	else:
         	   print("Error browser Name!")
elif tipo=="text":
	   lettura= input("What do you want search?")
	   webbrowser.open('https://www.bing.com/search?q='+str(lettura))      
	   
else:
	print("Search ERROR, please insert file or text!")  
