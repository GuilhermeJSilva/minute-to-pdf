#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
FILENAME=$1

python "$DIR/src/main.py" "$FILENAME" | pandoc -o $2