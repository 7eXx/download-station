from jinja2 import Environment, FileSystemLoader
from dotenv import dotenv_values
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--prod', help='Process template using production environment', required=False)

args = vars(parser.parse_args())

env_variables = []

if args['prod'] is None:
    print('Building using standard env')
    env_variables = {**dotenv_values(".env")}
else:
    print('Building using production')
    env_variables = {
        **dotenv_values(".env"),
        **dotenv_values(".env.prod")
    }

env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('docker-compose.yml.j2')

output_parsed = template.render(env_variables)

with open("docker-compose.yml", "w") as fh:
    fh.write(output_parsed)

