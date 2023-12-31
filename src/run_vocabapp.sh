#!/bin/bash

echo "Requirements and virtual environment will load..."
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r ./requirements.txt
echo "Now we're ready to go!"
python3 ./main.py 
deactivate