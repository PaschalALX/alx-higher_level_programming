#!/bin/bash
# Write a Bash script that sends a request and returns status
curl -s -I $1 | grep -e HTTP/* | cut -d ' ' -f 2
