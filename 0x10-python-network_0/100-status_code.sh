#!/bin/bash
# gets content-length of a web page
curl -I -s $1 | grep HTTP1/1 | cut -d ' ' -f 2
