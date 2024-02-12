#!/bin/bash

date >> ~/geoips1.log

cd /home/user1/cms

#activate python venv
source venv/bin/activate 

# sudo systemctl disable nftables.service
sudo systemctl stop nftables.service

./venv/bin/python ./geofilter.py >> ~/geoips1.log 2>&1
./venv/bin/python ./combinednft.py >> ~/geoips1.log 2>&1

#restart firewall
# sudo systemctl enable nftables.service
sudo systemctl start nftables.service >> ~/geoips1.log 2>&1

deactivate