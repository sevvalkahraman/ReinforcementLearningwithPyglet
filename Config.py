# Import libraries
import configparser

# Creating config object
config = configparser.ConfigParser()
config.read('config.ini')

class EnvironmentConfig():
    SIZE_X = int(config['ENVIRONMENT_VARIABLES']['SIZE_X'])
    SIZE_Y = int(config['ENVIRONMENT_VARIABLES']['SIZE_Y'])
    BOX_SIZE = int(config['ENVIRONMENT_VARIABLES']['BOX_SIZE'])
    FINISH_CHAR = config['ENVIRONMENT_VARIABLES']['FINISH_CHAR']
    WALL_CHAR = config['ENVIRONMENT_VARIABLES']['WALL_CHAR']
    PLAYER_CHAR= config['ENVIRONMENT_VARIABLES']['PLAYER_CHAR']
    FIRE_CHAR = config['ENVIRONMENT_VARIABLES']['FIRE_CHAR']
    FILENAME = config['ENVIRONMENT_VARIABLES']['FILENAME']
    BACKGROUND_IMAGE = config['ENVIRONMENT_VARIABLES']['BACKGROUND_IMAGE']
    FIRE_IMAGE = config['ENVIRONMENT_VARIABLES']['FIRE_IMAGE']
    WALL_IMAGE = config['ENVIRONMENT_VARIABLES']['WALL_IMAGE']
    FINISH_IMAGE = config['ENVIRONMENT_VARIABLES']['FINISH_IMAGE']
    PLAYER_IMAGE = config['ENVIRONMENT_VARIABLES']['PLAYER_IMAGE']

class RLConfig():
    ALPHA = float(config['RL_PARAMETRES']['ALPHA'])
    DISCOUNTFACTOR = float(config['RL_PARAMETRES']['DISCOUNTFACTOR'])
    EPSILON = float(config['RL_PARAMETRES']['EPSILON'])