# FUNCTION - JOSWENIGGA PINKGUY

from installer import SoftwareInstaller

class ToolkitFunctions:
    def __init__(self, logger):
        self.logger = logger
        self.installer = SoftwareInstaller(logger)
    
    def install(self, software_key):
        # example implementation for one software:
        if software_key == "python":
            return self.installer.install_python()
        elif software_key == "java":
            return self.installer.install_java()
        elif software_key == "nodejs":
            return self.installer.install_nodejs()
        elif software_key == "vscode":
            return self.installer.install_vscode()
        elif software_key == "git":
            return self.installer.install_git()
        elif software_key == "Android Studio":
            return self.installer.install_androidstudio()
        elif software_key == "Tableau Public":
            return self.installer.install_tableaupublic()
        elif software_key == "Canva":
            return self.installer.install_Canva()
        elif software_key == "GIMP":
            return self.installer.install_GIMP()
        elif software_key == "Blender":
            return self.installer.install_Blender()
        elif software_key == "Audacity":
            return self.installer.install_Audacity()
        elif software_key == "Krita":
            return self.installer.install_Krita()
        elif software_key == "Grammarly":
            return self.installer.install_Grammarly()
        elif software_key == "CapCut":
            return self.installer.install_Capcut()
        elif software_key == "Microsoft Teams":
            return self.installer.install_Microsoft()
        
        # implement the rest dito mismo
        

        return False




