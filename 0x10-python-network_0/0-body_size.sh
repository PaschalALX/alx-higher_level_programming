#!/bin/bash
# gets content-length of a web page
curl -I -s $1 | grep Content-Length | cut -d ' ' -f 2
