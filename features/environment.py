import yaml
import sys
import os



def before_scenario(context,scenario):
    ## TODO ajustar load arquivo YML
    load_yaml_files(context)


def load_yaml_files(context):
    with open(os.path.join(os.getcwd(), 'support/config', 'endpoints.yml'), 'r') as file:
        context.endpoint = yaml.safe_load(file)
    
    with open(os.path.join(os.getcwd(), 'support/config', 'url.yml'), 'r') as file:
        context.url = yaml.safe_load(file)