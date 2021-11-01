#!/bin/bash

change_to_project_dir() {
  local SCRIPT_LOCATION=$(cd `dirname $0` && pwd)
  local PROJECT_LOCATION="$SCRIPT_LOCATION/.."
  cd $PROJECT_LOCATION
}

# can be overriden, example: "IMAGE_NAME=my_custom_name ./build.sh"
IMAGE_NAME=${IMAGE_NAME:-'logger-demo-app-local'}

# change working dir to project root
change_to_project_dir

docker build -f docker/Dockerfile -t ${IMAGE_NAME} .
