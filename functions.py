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
        if software_key == "java":
            return self.installer.install_java()
        if software_key == "nodejs":
            return self.installer.install_nodejs()
        if software_key == "vscode":
            return self.installer.install_vscode()
        if software_key == "git":
            return self.installer.install_git()
        if software_key == "Android Studio":
            return self.installer.install_androidstudio()
        if software_key == "Tableau Public":
            return self.installer.install_tableaupublic()
        if software_key == "Canva":
            return self.installer.install_Canva()
        if software_key == "GIMP":
            return self.installer.install_GIMP()
        if software_key == "Blender":
            return self.installer.install_Blender()
        if software_key == "Audacity":
            return self.installer.install_Audacity()
        if software_key == "Krita":
            return self.installer.install_Krita()
        if software_key == "Grammarly":
            return self.installer.install_Grammarly()
        if software_key == "CapCut":
            return self.installer.install_Capcut()
        if software_key == "Microsoft Teams":
            return self.installer.install_Microsoft()
        
        # implement the rest dito mismo
        

        return False



