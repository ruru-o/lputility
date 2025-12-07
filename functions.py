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
            return self.installer.install_python()
        if software_key == "nodejs":
            return self.installer.install_python()
        if software_key == "vscode":
            return self.installer.install_python()
        if software_key == "git":
            return self.installer.install_python()
        if software_key == "Android Studio":
            return self.installer.install_python()
        if software_key == "Tableau Public":
            return self.installer.install_python()
        if software_key == "python":
            return self.installer.install_python()
        if software_key == "python":
            return self.installer.install_python()
        if software_key == "python":
            return self.installer.install_python()
        if software_key == "python":
            return self.installer.install_python()
        if software_key == "python":
            return self.installer.install_python()
        
        # implement the rest dito mismo
        

        return False


