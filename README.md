
# Download Station
This repository contains some useful tools for download: 
   - [x] Plex
   - [x] Transmission
   - [x] Pyload
   - [x] Amule
   - [x] Filebrowser
   - [x] Heimdall
   - [ ] XdccDownload

All these tools are implemented as docker containers.

## Pre-check
Fill the **.env** file with custom variables or create e new **.env.prod**.  
Install python virtual env
```
$ python3 -m venv venv
```
Activate virutal env created
```
$ source venv/bin/activate
```
Install all dependencies
```
$ pip3 install -r requirements
```

## Usage
This project use python to build the template for the docker compose file.
```
$ python build.py
```
or
```
$ python build.py --prod PROD
```

## Deploy the generated output
To deploy the generated docker compose file use the rsync command:
```
$ ssh synology@192.168.0.100 mkdir -p ~/download-station
$ rsync output/docker-compose.yml synology@192.168.0.100:~/download-station/docker-compose.yml
```

### Deploy docker compose 
To deploy the docker compose file generated use the command:
```
$ docker compose --project-directory ./ --file output/docker-compose.yml up -d
```
To stop
```
$ docker compose --project-directory ./ --file output/docker-compose down -v
```

## Plex
Create a torrent transmission service using the variables in dot env file.  

Access your server at: <your-ip>:32400/web

## Transmission
Create a torrent transmission service using the variables in dot env file.

## Pyload
Edit environmental variables in env file or create a new local one.
Default credentials are:
- username: admin
- password: password

## Amule
Edit environmental variables in env file or create a new local one.
Make sure to create the local folders for:
- config
- incomplete
- complete

Default behavior of emule is to not run this service.

## Filebrower

## Heimdall
Import configuration files from **docker/heimdall/HeimdallExport.json**
