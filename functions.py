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
        
        # implement the rest dito mismo
        

        return False
