#!/bin/bash
# Post JSON File
curl -s -H "Content-Type: application/json" -d @$2 $1
