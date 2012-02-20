#!/bin/sh
export PYTHONPATH="./"

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
TARGET=$DIR"/manage.py"

python $TARGET test_coverage mock knowledge --pythonpath="../"