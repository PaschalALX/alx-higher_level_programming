#!/bin/bash
# Write a Bash script that sends a request and returns status
curl -so /dev/null --write-out "%{http_code}\n" $1
