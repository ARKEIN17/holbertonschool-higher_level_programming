#!/bin/bash
# Script get size
curl -sI "$1" | grep -i Content-Length | cut -d ":" -f2 | cut -d " " -f2
