#!/bin/bash
# Bash script that takes in a URL, sends a request to that URL
curl -s GET "$1" | grep 200
