#!/bin/sh

# usage: ./watch.sh process_name

processName=$1

isAlive=`ps -ef | grep "$processName" | grep -v grep | grep -v watch.sh | wc -l`

if [ $isAlive = 1 ]; then
    echo "Server is running."
else
    echo "Server is dead, restarting..."
fi

