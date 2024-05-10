#!/bin/bash
#Takes in a URL & send a request to it
curl -s "$1" | wc -c
