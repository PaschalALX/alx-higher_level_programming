#!/bin/bash
# gets content-length of a web page
curl -s -I $1 | grep Allow: | cut -d ' ' -f 2-
