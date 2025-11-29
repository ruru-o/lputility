# PROGRAMS/INSTALLERS - RAPHIGGA HERRRA & YUANIGGA RUBIO

import webbrowser

class SoftwareInstaller:
    def __init__(self, logger):
        self.logger = logger
        
        # download urls - update if needed 
        # we'll keep it browser muna so we can complete it. soon na yung winget (auto install)
        self.urls = {
            'python': 'https://www.python.org/downloads/',
            'vscode': 'https://code.visualstudio.com/download',
            'git': 'https://git-scm.com/downloads',
            'java': 'https://www.oracle.com/java/technologies/downloads/',
            'nodejs': 'https://nodejs.org/en/download/',
            'visual_studio': 'https://visualstudio.microsoft.com/downloads/',
            'intellij': 'https://www.jetbrains.com/idea/download/',
            'mysql': 'https://dev.mysql.com/downloads/installer/',
            'postgresql': 'https://www.postgresql.org/download/',
            'github_desktop': 'https://desktop.github.com/',
            'postman': 'https://www.postman.com/downloads/',
            'docker': 'https://www.docker.com/products/docker-desktop/',
            'anaconda': 'https://www.anaconda.com/download',
            'jupyter': 'https://jupyter.org/install',
            'virtualbox': 'https://www.virtualbox.org/wiki/Downloads',
            'wireshark': 'https://www.wireshark.org/download.html',
            'office365': 'https://www.office.com/',
            'libreoffice': 'https://www.libreoffice.org/download/download/',
            'chrome': 'https://www.google.com/chrome/',
            'firefox': 'https://www.mozilla.org/en-US/firefox/new/',
            'zoom': 'https://zoom.us/download',
            'discord': 'https://discord.com/download',
            'vlc': 'https://www.videolan.org/vlc/',
            '7zip': 'https://www.7-zip.org/download.html',
        }
    
    def install_python(self):
        # incomplete code. dalihin mo na bengbang
        self.logger.log("Installing Python")
        try:
            webbrowser.open(self.urls['python'])
            return True
        except:
            return False
    
    # create install methods for all other software
    # follow the same pattern as install_python()
    
    # ides & editors
    def install_vscode(self):
        """install visual studio code"""
        # implement here
        pass
    
    def install_visual_studio(self):
        """install visual studio"""
        # implement here
        pass
    
    def install_intellij(self):
        """install intellij idea"""
        # implement here
        pass
    
    # languages & runtimes
    def install_java(self):
        """install java jdk"""
        # implement here
        pass
    
    def install_nodejs(self):
        """install nodejs"""
        # implement here
        pass
    
    # databases
    def install_mysql(self):
        """install mysql"""
        # implement here
        pass
    
    def install_postgresql(self):
        """install postgresql"""
        # implement here
        pass
    
    # version control
    def install_git(self):
        """install git"""
        # implement here
        pass
    
    # development tools
    def install_github_desktop(self):
        """install github desktop"""
        # implement here
        pass
    
    def install_postman(self):
        """install postman"""
        # implement here
        pass
    
    def install_docker(self):
        """install docker"""
        # implement here
        pass
    
    # data science
    def install_anaconda(self):
        """install anaconda"""
        # implement here
        pass
    
    def install_jupyter(self):
        """install jupyter notebook"""
        # implement here
        pass
    
    # utilities
    def install_virtualbox(self):
        """install virtualbox"""
        # implement here
        pass
    
    def install_wireshark(self):
        """install wireshark"""
        # implement here
        pass
    
    # office suites
    def install_office365(self):
        """install office 365"""
        # implement here
        pass
    
    def install_libreoffice(self):
        """install libreoffice"""
        # implement here
        pass
    
    # browsers
    def install_chrome(self):
        """install chrome"""
        # implement here
        pass
    
    def install_firefox(self):
        """install firefox"""
        # implement here
        pass
    
    # communication
    def install_zoom(self):
        """install zoom"""
        # implement here
        pass
    
    def install_discord(self):
        """install discord"""
        # implement here
        pass
    
    # media & files
    def install_vlc(self):
        """install vlc player"""
        # implement here
        pass
    
    def install_7zip(self):
        """install 7zip"""
        # implement here
        pass