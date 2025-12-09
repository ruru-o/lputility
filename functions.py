# FUNCTION - JOSWENIGGA PINKGUY

from installer import SoftwareInstaller

class ToolkitFunctions:
    def __init__(self, logger):
        self.logger = logger
        self.installer = SoftwareInstaller(logger)
    
    def install(self, software_key):
        #IDE
        if software_key == "notepad++":
            return self.installer.install_notepad()
        elif software_key == "Pycharm":
            return self.installer.install_pycharm()
        elif software_key == "intellij":
            return self.installer.install_intellij()
        elif software_key == "eclipse":
            return self.installer.install_eclipse()
        elif software_key == "vscode":
            return self.installer.install_vscode()
        elif software_key == "android studio":
            return self.installer.install_androidstudio()
        elif software_key == "sublime_text":
            return self.installer.install_sublimetext()

        #LANGUAGE & RUNTIMES
        elif software_key == "python":
            return self.installer.install_python()
        elif software_key == "java":
            return self.installer.install_java()
        elif software_key == "nodejs":
            return self.installer.install_nodejs()
        elif software_key == "visual c++":
            return self.installer.install_visualcplusplus()
        elif software_key == "git":
            return self.installer.install_git()
        elif software_key == "php":
            return self.installer.install_php()

        #DATABASE
        elif software_key == "mysql  workbench":
            return self.installer.install_mysqlworkbench()
        elif software_key == "potgresql":
            return self.installer.install_Postgresql()
        elif software_key == "mongodb compass":
            return self.installer.install_mongodbcompass()
        elif software_key == "sqlite browser":
            return self.installer.install_sqliteBrowser()
        elif software_key == "dbeaver":
            return self.installer.install_dbeaver()

        #ACADEMICS
        elif software_key == "notion":
            return self.installer.install_notion()
        elif software_key == "grammarly":
            return self.installer.install_Grammarly()
        elif software_key == "cobalt":
            return self.installer.install_cobalt()
        elif software_key == "Canva":
            return self.installer.install_Canva()

        #PRODUCTIVITY
        elif software_key == "M365":
            return self.installer.install_M365()
        elif software_key == "Tableau Public":
            return self.installer.install_tableaupublic()

        #CREATIVITY
        elif software_key == "GIMP":
            return self.installer.install_GIMP()
        elif software_key == "Blender":
            return self.installer.install_Blender()
        elif software_key == "Audacity":
            return self.installer.install_Audacity()
        elif software_key == "Krita":
            return self.installer.install_Krita()
        elif software_key == "CapCut":
            return self.installer.install_Capcut()

        #WEB BROWSERS
        elif software_key == "mozilla firefox":
            return self.installer.install_MozillaFirefox()
        elif software_key == "Opera":
            return self.installer.install_Opera()
        elif software_key == "Opera GX":
            return self.installer.install_OperaGX()
        elif software_key == "Brave":
            return self.installer.install_Brave()
        elif software_key == "vivaldi":
            return self.installer.install_vivaldi()
        
        #COMMUNICATION
        elif software_key == "discord":
            return self.installer.install_Discord()
        elif software_key == "telegram":
            return self.installer.install_Telegram()
        elif software_key == "Microsoft Teams":
            return self.installer.install_Microsoft()

        #MEDIA AND FILES
        elif software_key == "vlc":
            return self.installer.install_VLC()
        elif software_key == "7zip":
            return self.installer.install_7zip()
        elif software_key == "winrar":
            return self.installer.install_Winrar()
        elif software_key == "nanazip":
            return self.installer.install_Nanazip()

        return False





