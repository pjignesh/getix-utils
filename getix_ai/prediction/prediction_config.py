import configparser
import os

PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))
ENVIRON_FILE_NAME = 'prediction_variables.ini'
ENVIRONMENT_SETTINGS_FILE_PATH = os.path.join(PROJECT_ROOT, ENVIRON_FILE_NAME).replace('\\', '/')

ENVIRONMENT_SETTINGS = configparser.ConfigParser()
ENVIRONMENT_SETTINGS.read(ENVIRONMENT_SETTINGS_FILE_PATH)

CORE_1_IP = ENVIRONMENT_SETTINGS.get('CORE_IP', 'core_1_ip')
CORE_2_IP = ENVIRONMENT_SETTINGS.get('CORE_IP', 'core_2_ip')
CORE_3_IP = ENVIRONMENT_SETTINGS.get('CORE_IP', 'core_3_ip')
CORE_4_IP = ENVIRONMENT_SETTINGS.get('CORE_IP', 'core_4_ip')
CORE_5_IP = ENVIRONMENT_SETTINGS.get('CORE_IP', 'core_5_ip')
CORE_6_IP = ENVIRONMENT_SETTINGS.get('CORE_IP', 'core_6_ip')
CORE_7_IP = ENVIRONMENT_SETTINGS.get('CORE_IP', 'core_7_ip')
CORE_8_IP = ENVIRONMENT_SETTINGS.get('CORE_IP', 'core_8_ip')

CORE_1_PORT = ENVIRONMENT_SETTINGS.get('CORE_PORTS', 'core_1_port')
CORE_2_PORT = ENVIRONMENT_SETTINGS.get('CORE_PORTS', 'core_2_port')
CORE_3_PORT = ENVIRONMENT_SETTINGS.get('CORE_PORTS', 'core_3_port')
CORE_4_PORT = ENVIRONMENT_SETTINGS.get('CORE_PORTS', 'core_4_port')
CORE_5_PORT = ENVIRONMENT_SETTINGS.get('CORE_PORTS', 'core_5_port')
CORE_6_PORT = ENVIRONMENT_SETTINGS.get('CORE_PORTS', 'core_6_port')
CORE_7_PORT = ENVIRONMENT_SETTINGS.get('CORE_PORTS', 'core_7_port')
CORE_8_PORT = ENVIRONMENT_SETTINGS.get('CORE_PORTS', 'core_8_port')