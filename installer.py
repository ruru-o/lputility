import webbrowser

class SoftwareInstaller:
    def __init__(self, logger):
        self.logger = logger
        
        # download urls - update if needed 
        # we'll keep it browser muna so we can complete it. soon na yung winget (auto install)
        self.urls = {
            'python': 'https://www.python.org/ftp/python/3.14.0/python-3.14.0-amd64.exe',
            'java': 'https://download.oracle.com/java/25/latest/jdk-25_windows-x64_bin.exe',
            'nodejs': 'https://nodejs.org/dist/v24.11.1/node-v24.11.1-x64.msi',
            'vscode': 'https://code.visualstudio.com/sha/download?build=stable&os=win32-x64-user',                  
            'git': 'https://github.com/git-for-windows/git/releases/download/v2.52.0.windows.1/Git-2.52.0-64-bit.exe',
            'Android Studio': 'https://redirector.gvt1.com/edgedl/android/studio/install/2025.2.2.7/android-studio-2025.2.2.7-windows.exe',
            'Tableau Public': 'https://www.tableau.com/en-us/downloads/public/pc64',
            'Canva': 'https://www.canva.com/download/windows/canva-desktop/',
            'GIMP': 'https://download.gimp.org/gimp/v3.0/windows/gimp-3.0.6-setup-1.exe',
            'Blender': 'https://www.blender.org/download/release/Blender5.0/blender-5.0.0-windows-x64.msi/',
            'Audacity': 'https://muse-cdn.com/Audacity_Installer_via_MuseHub.exe',
            'Krita': 'https://download.kde.org/stable/krita/5.2.13/krita-x64-5.2.13-setup.exe',
            'Grammarly': 'https://download-windows.grammarly.com/w/GrammarlyInstaller.exe', 
            'CapCut': 'https://www.capcut.com/activity/download_pc',
            'Microsoft Teams': 'https://statics.teams.cdn.office.net/production-windows-x86/lkg/MSTeamsSetup.exe'
        }
        # ADD MORE
            # ALSO, ADD KO LANG NA I-CATEGORIZE NIYO YUNG BAWAT PROGRAMS AND COMMENT
            # (ex. PYTHON,MYSQL - #LANGUAGE & RUNTIMES) 
            # (ex. VSCODE - #IDE)
    
    def install_python(self):
        self.logger.log("Installing Python")
        try:
            webbrowser.open(self.urls['python'])
            return True
        except:
            return False

    def install_java(self):
        self.logger.log("Installing Java JDK")
        try:
            webbrowser.open(self.urls['java'])
            return True
        except:
            return False

    def install_nodejs(self):
        self.logger.log("Installing NodeJS")
        try:
            webbrowser.open(self.urls['nodejs'])
            return True
        except:
            return False

    
    def install_vscode(self):
        self.logger.log("Installing Visual Studio Code")
        try:
            webbrowser.open(self.urls['vscode'])
            return True
        except:
            return False

    def install_visual_studio(self):
        self.logger.log("Installing Visual Studio")
        try:
            webbrowser.open(self.urls['visual_studio'])
            return True
        except:
            return False

    def install_intellij(self):
        self.logger.log("Installing IntelliJ IDEA")
        try:
            webbrowser.open(self.urls['intellij'])
            return True
        except:
            return False

    
    def install_git(self):
        self.logger.log("Installing Git")
        try:
            webbrowser.open(self.urls['git'])
            return True
        except:
            return False

    def install_androidstudio(self):
        self.logger.log("Installing Android Studio")
        try:
            webbrowser.open(self.urls['Android Studio'])
            return True
        except:
            return False

    def install_tableaupublic(self):
        self.logger.log("Installing Tableau Public")
        try:
            webbrowser.open(self.urls['Tableau Public'])
            return True
        except:
            return False

    def install_Canva(self):
        self.logger.log("Installing Canva")
        try:
            webbrowser.open(self.urls['Canva'])
            return True
        except:
            return False

    def install_GIMP(self):
        self.logger.log("Installing GIMP")
        try:
            webbrowser.open(self.urls['GIMP'])
            return True
        except:
            return False

    def install_Blender(self):
        self.logger.log("Installing Blender")
        try:
            webbrowser.open(self.urls['Blender'])
            return True
        except:
            return False

    def install_Audacity(self):
        self.logger.log("Installing Audacity")
        try:
            webbrowser.open(self.urls['Audacity'])
            return True
        except:
            return False

    def install_Krita(self):
        self.logger.log("Installing Krita")
        try:
            webbrowser.open(self.urls['Krita'])
            return True
        except:
            return False

    def install_Grammarly(self):
        self.logger.log("Installing Grammarly")
        try:
            webbrowser.open(self.urls['Grammarly'])
            return True
        except:
            return False

    def install_Capcut(self):
        self.logger.log("Installing CapCut")
        try:
            webbrowser.open(self.urls['CapCut'])
            return True
        except:
            return False

    def install_Microsoft(self):
        self.logger.log("Installing Microsoft Teams")
        try:
            webbrowser.open(self.urls['Microsoft Teams'])
            return True
        except:
            return False
