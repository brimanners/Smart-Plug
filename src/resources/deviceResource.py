import sys
import src.controllers.smartPlugController as smartPlugController
import src.logging.log as log
import src.services.configurationService as config

# This is the main entry, that will dispatch based upon argument provided
if __name__ == "__main__":

    device_id = sys.argv[1]     # Get the device that needs to be controlled
    dispatch_mode = sys.argv[2]         # Get the operation needed - e.g. on or off

    environment = config.get_environment()

    log.save_info("Start services in environment " + environment + ' - for device : ' + device_id + " - Set state = " + dispatch_mode)

    smartPlugController.action_device(device_id, dispatch_mode)