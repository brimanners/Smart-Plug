import src.logging.log as log
import src.services.configurationService as config
import os
import src.test.fixtures.tokenResponse as tokenResponse
import src.test.fixtures.deviceListResponse as deviceListResponse


def execute_curl_statement(curl_statement, curl_type):

    response = ""
    if config.get_environment() == "prod":
        response = (os.popen(curl_statement).read())
    # Mocks
    else:
        if curl_type == "token":
            response = tokenResponse.return_mock_token_response()
        if curl_type == "devices":
            response = deviceListResponse.return_device_response()

    return response
