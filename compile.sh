#!/bin/bash

set -e

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
if [[ -z $1 ]] ; then
    echo "Usage: $0 <input-file> [ <output-file> ]"
    exit -1
fi

FILENAME=$1
OUTFILE=${2:-"${1%.*}.pdf"}

python3 "$DIR/src/main.py" "$FILENAME" | pandoc -o "$OUTFILE"