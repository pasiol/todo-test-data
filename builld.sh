#!/bin/sh
docker build -t pasiol/todo-generator generator/
docker push pasiol/todo-generator
docker build -t pasiol/markdone markdone/
docker push pasiol/todo-markdonec