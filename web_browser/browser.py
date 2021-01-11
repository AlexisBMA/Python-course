import webbrowser

# webbrowser.open("https://www.python.org/", new=1)

# help(webbrowser)

Chrome = webbrowser.get('windows-default')
Chrome.open_new_tab("https://www.python.org/")
