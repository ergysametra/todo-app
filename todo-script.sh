#!/bin/bash
# export DATA_URI
export DATA_URI SECRET_KEY
echo "Database URI: $DATABES_URI" 

# install apt dependencies
sudo apt update
sudo apt install python3 python3-venv python3-pip -y

# create virtual environment
python3 -m venv venv

# activate virtual environment
source venv/bin/activate

# install pip requirements
pip3 install -r requirements.txt

# run tests
python3 -m pytest \
   --cov=application \
   --cov-report term-missing \
   --cov-report xml:coverage.xml \
   --junitxml=junit_report.xml
   
# run create.py to create schema
if  [ $CREATE_SCHEMA == "true" ]
then 
    echo "Creating schema..."
    python3 create.py
    echo "Schema created!"
fi

#run the app
#python3 app.py