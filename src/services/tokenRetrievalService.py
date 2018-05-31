import src.logging.log as log
import os
import json
import src.services.configurationService as Config
import src.services.curlExecutionService as Curl


def get_token():

    smart_plug_auth = Config.get_smart_plug_credentials()

    url = 'https://wap.tplinkcloud.com/'
    payload = '\'{"method": "login", "params": { "appType": "Kasa_Android", "cloudUserName": "' + smart_plug_auth["userId"] + \
              '", "cloudPassword": "' + smart_plug_auth["password"] + \
              '", "terminalUUID": "d28fd119-9675-4659 b9a4-5c60b624723b"}}\''

    curl_statement = 'curl -X POST ' + url + ' -H \'cache-control: no-cache\' -H \'content-type: application/json\' -d ' + payload

    curl_response = Curl.execute_curl_statement(curl_statement, "token")

    response = json.loads(str(curl_response))

    return response['result']['token']