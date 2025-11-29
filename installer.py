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
            # ADD MORE
            # ALSO, ADD KO LANG NA I-CATEGORIZE NIYO YUNG BAWAT PROGRAMS AND COMMENT
            # (ex. PYTHON,MYSQL - #LANGUAGE & RUNTIMES) 
            # (ex. VSCODE - #IDE)
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
