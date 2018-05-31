# Smart Plug Controller

## These scripts were generated to be used with the TP-Link HS100 smartplug.

### Disclaimer: If they are used to turn on/off electrical applicances attached to the smart plug, please ensure that the attached item is safe to do so and there is no fire risk.
### The author of these scripts cannot be held liable for any damage or injury as a result of implementing these scripts in your own projects


##### After purchasing the HS100 smartplug and setting up the device, you will define your own alias for the plug. You can have multiple devices on the same network so you can also control each from these scripts
##### To use, from the home folder, type

##### ./scripts.sh "Your Device Id" on
##### OR
##### ./scripts.sh "Your Device Id" off

##### If your device ID has spaces in it's definition, be sure to wrap in quotes

#### Configuration
##### You will also need to provide your KASA home account credentials in the config/properties file in the userid and password fields

#### You can also comment on/off the environment for local testing. RUnning in test mode will serve up fake fixture files to mock the api calls
