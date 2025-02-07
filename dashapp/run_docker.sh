#!/bin/bash
docker build -t dash:latest .
sleep  30
docker run -p 8050:8050 dash:latest