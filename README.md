# weatherapi

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Build Status](https://travis-ci.com/username/repo.svg?branch=main)](https://travis-ci.com/username/repo)

Short description or summary of the project.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Installation with miniconda

1. Clone the repository: `git clone <repository URL>`
  - conda create --name weatherapi python==3.10 -y
  - conda activate weatherapi
  - pip install poetry==1.4.2
  - poetry config virtualenvs.create false
  - poetry install
2. The las command install the dependencies for use this application: -> `poetry install`


## Use environment variables for configuration
from command line under your environment activated use `conda activate weatherapi`
- configure URL
export URL="http://api.openweathermap.org/data/2.5/weather"
This url will be used or use any for default configuration.
use unset URL for default configuration and will work with "http://api.openweathermap.org/data/2.5/weather"
- configure TTL for use the cache or default is 120 seconds
export TTL=60

## Usage

This project will run if you use next command

`uvicorn weatherapi.app:app`


## Run tests with coverage
- Run tests with coverage
`pytest --cov`

## build instance with docker commands only if you want to use containers instead.
docker build -t "weatherapi:dockerfile" .
	and 
docker run -p 8000:8000 weatherapi:V1.0.0
### Install docker and dependencies if you want to use containers instead.
instalar Docker en tu sistema Linux Raspberry Pi con el kernel 5.4.79-v7+
sudo apt update
sudo apt upgrade
sudo apt install apt-transport-https ca-certificates curl software-properties-common

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

echo "deb [arch=armhf signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/raspbian buster stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt update

sudo apt install docker-ce docker-ce-cli containerd.io

docker --version

## We have some data for use with test and also have like general information. This will be only for reference.
```
GET /weather?city=$City&country=$Country&
Response: {
  "location_name": "Bogota, CO",
  "temperature": "17 °C",
  "wind": Gentle breeze, 3.6 m/s, west-northwest",
  "cloudiness": "Scattered clouds",
  "pressure": "1027 hpa",
  "humidity": "63%",
  "sunrise": "06:07",
  "sunset": "18:00",
  "geo_coordinates": "[4.61, -74.08]",
  "requested_time": "2018-01-09 11:57:00"
  "forecast": {...}
}
```

## Testing application from Postman application or thunder client in visual studio code
use GET and like and exemple requests will be sent:
- http://localhost:8000/weather?country=co&city=medellin

Query parameters:
    - country: medellin
    - city: co

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

## Contact

For any questions or inquiries, please reach out to [william.cuesta].