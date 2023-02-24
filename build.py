from jinja2 import Environment, FileSystemLoader
from dotenv import dotenv_values
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--prod', help='Process template using production environment', required=False)

args = vars(parser.parse_args())

env_variables = []
building_env = 'dev'
output_dir = 'output'

if args['prod'] is None:
    print('Building using standard env')
    env_variables = {
        **dotenv_values(".env"),
        **dotenv_values(".env.local")
    }
    building_env = 'dev'
else:
    print('Building using production')
    env_variables = {
        **dotenv_values(".env"),
        **dotenv_values(".env.prod")
    }
    building_env = 'prod'

output_file = f'output/docker-compose.yml'

if not os.path.exists(output_dir):
    os.mkdir(output_dir)

env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('docker-compose.yml.j2')

output_parsed = template.render(env_variables)

with open(output_file, "w") as fh:
    fh.write(output_parsed)

