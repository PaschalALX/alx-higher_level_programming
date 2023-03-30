#!/usr/bin/env bash
# gets content-length
curl -I -s $1 | grep Content-Length | cut -d ' ' -f 2
