
def get_configuration():

    configurations = {}
    with open("./config/properties", "r") as f:
        for line in f:
            if ":" in line:
                key_value = line.split(":")
                configurations[key_value[0]] = key_value[1].strip()

    return configurations


def get_smart_plug_credentials():

    config = get_configuration()

    smart_plug_credentials = {}
    smart_plug_credentials['userId'] = config["userId"]
    smart_plug_credentials['password'] = config["password"]

    return smart_plug_credentials


def get_environment():

    config = get_configuration()
    return config["environment"]
