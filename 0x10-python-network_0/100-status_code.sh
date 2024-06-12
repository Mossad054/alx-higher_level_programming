#!/bin/bash
# request to URL passed as an arg and displays only the status code of the response.
curl -s -o /dev/null -w "%{http_code}" "$1"
