#!/bin/sh
export PYTHONPATH="./"

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
TARGET=$DIR"/manage.py"
PORT='8080'

python $TARGET runserver $PORT --pythonpath="../"