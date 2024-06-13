

import webbrowser

_facebook_link = "facebook.com"
_google_link = "google.com"
_yahoo_link = "yahoo.com"

def firefox(fav_urL):
    chrome_path = "C:\Program Files\Google\Chrome\Application\chrome.exe"
    webbrowser.register("chrome", None, webbrowser.BackgroundBrowser(chrome_path))
    urL = ["facebook.com", "google.com", "yahoo.com"]
    if fav_urL in urL:
        webbrowser.get("chrome").open(fav_urL)
