#!/bin/bash

###################################################################################
# Author: Brian Manners
# Date  : June 2018
#
# This generic script is a passthrough to set up PYTHON config and then
# dispatch to the resource function along with the provided parameters
####################################################################################

# Set PYTHONPATH to current working directory
export PYTHONPATH=$PYTHONPATH:$PWD

# Run the python script end point based on the provided parameters
# $1 - Single quote device id - Will try to match the devices and execute against the relevant server... If device has spaces, surround with quotes.
# #2 - mode - on/off
#
# Example
#           ./scripts.sh "SOME DEVICE ID" on       OR       ./scripts.sh "SOME DEVICE ID" off

/usr/bin/python src/resources/deviceResource.py "$1" $2


