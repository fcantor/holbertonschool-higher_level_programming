#!/bin/bash
# Script that sends a POST request to the URL passed and displays body of response
curl -sX POST 0.0.0.0:5000/route_6 -d "email=hr@holbertonschool.com&subject=I will always be here for PLD"
