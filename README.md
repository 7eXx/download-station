
# Download Station
This repository contains some useful tools for download:  
   - [x] Transmission
   - [x] Pyload
   - [ ] Amule
   - [ ] XdccDownload

All these tools are implemented as docker containers.

## Pre-check
Fill the **.env** file with custom variables or create e new **.env.prod**

### Usage
This project use python to build the template for the docker compose file.
```
$ python compile.py
```
or
```
$ python compile.py --prod PROD
```

## Transmission
Create a torrent transmission service using the variables in dot env file.

## Pyload
Edit environmental variables in env file or create a new local one.
Default credentials are:
- username: admin
- password: password
