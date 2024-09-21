import yaml
import sys
import os



def before_scenario(context,scenario):
    ## TODO ajustar load arquivo YML
    load_yaml_files(context)


def load_yaml_files(context):
    DIR = os.getcwd()
    #dir = os.path.dirname(os.path.abspath(__file__))
    print("ALOOOOOOO")
    print(str(DIR))
    with open(DIR+'/support/endpoints.yml', 'r') as file:
       context = yaml.safe_load(file)