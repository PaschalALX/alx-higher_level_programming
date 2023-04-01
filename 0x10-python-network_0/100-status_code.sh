#!/bin/bash
# Write a Bash script that sends a request and returns status
curl -s -o /dev/null -w "%{http_code}\n" $1
