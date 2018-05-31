import src.logging.log as log
import src.services.tokenRetrievalService as tokenRetrievalService
import src.services.deviceRetrievalService as deviceRetrievalService
import src.services.deviceActionService as action


def action_device(device_id, dispatch_mode):

    # Get token
    token = tokenRetrievalService.get_token()
    log.save_info('token = ' + str(token))

    # TODO - Exception handling - bubble back up? - e.g. can't find device

    #Get application server
    app_server_url = deviceRetrievalService.get_device_app_url(token, device_id)

    log.save_info('app_server_url ' + str(app_server_url))

    # TODO - Temperary turn off/on based on script call... Expand to only turn on/off when some threshold parameter is made, or just rely on cron jobs?
    # Now turn off or on?
    # Just testing before these are moved to a differnet location that can be called via some timed job or value changing?

    log.save_info('We would turn the device ' + str(dispatch_mode))

    if dispatch_mode == "on":
        action.turn_on_device(device_id, app_server_url, token)

    if dispatch_mode == "off":
        action.turn_off_device(device_id, app_server_url, token)

    return "end"  # TODO - Return a success or failure response based upon catching any exceptions?
