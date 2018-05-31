import src.logging.log as log
import src.services.curlExecutionService as curl


def get_curl_statement(mode, device_id, application_url, token_id):

    curl_statement = 'curl --request POST "' + str(application_url) + '/?token=' +  str(token_id) + \
                     ' HTTP/1.1" --data \'{"method":"passthrough", "params": {"deviceId": "' + device_id + '", "requestData": "{\\"system\\":{\\"set_relay_state\\":{\\"state\\":' + str(mode) + '}}}"}}\' --header "Content-Type: application/json"'
    log.save_info('curl statment to turn on/off => ' + str(curl_statement))
    return curl_statement


def turn_on_device(device_id , application_url, token_id):

    log.save_info('Turn on ' + str(device_id) + " using url " + application_url)
    curl.execute_curl_statement(get_curl_statement(1, device_id, application_url, token_id), "on")


def turn_off_device(device_id, application_url, token_id):

    log.save_info('Turn off ' + str(device_id) + " using url " + application_url + " using token " + str(token_id))
    curl.execute_curl_statement(get_curl_statement(0, device_id, application_url, token_id), "off")
