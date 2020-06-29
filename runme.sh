#!/bin/bash

eval "$(conda shell.bash hook)"
conda activate ML_Server
echo Anaconda active vitural env

alias proj='cd $HOME/KeepGo/Flask_Project/myproject'
proj

FLASK_APP=pybo
FLASK_ENV=development
export FLASK_APP
export FLASK_ENV
flask run

echo FLASK Config Setting is Done!
