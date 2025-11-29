# BROWSER - JASKABADDIE PIMINTALLERS

import webbrowser

class BrowserEmbedder:   
    def __init__(self, logger):
        self.logger = logger
    
    def open_portal(self, url):
        self.logger.log(f"Opening portal: {url}")
        
        # add https:// if missing
        if not url.startswith('http'):
            url = 'https://' + url
        
        try:
            webbrowser.open(url)
            return True
        except:

            return False
