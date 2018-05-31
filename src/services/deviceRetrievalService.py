import src.logging.log as log
import os
import json
import src.services.curlExecutionService as Curl


def get_device_app_url(token, device_id):

    curl_statement = 'curl -s --request POST "https://wap.tplinkcloud.com/?token=' + str(token) + ' HTTP/1.1" --data \'{"method":"getDeviceList"}\' --header "Content-Type: application/json"'
    # TODO Break up curl request into smaller parts or even a curl factory class?

    curl_response = Curl.execute_curl_statement(curl_statement, "devices")

    device_list = json.loads(str(curl_response))

    return get_app_server_url(device_id, device_list)


def get_app_server_url(device_id, device_list):

    for device in device_list['result']['deviceList']:
        if device['alias'] == device_id:
            return device['appServerUrl']

    return "count not find app url for device " + device_id
