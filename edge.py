import webbrowser    
url='https://www.bing.com'
#insert address edge file location on your system
edge="C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
webbrowser.register('edge', None,webbrowser.BackgroundBrowser(edge))
webbrowser.get('edge').open_new_tab(url)
