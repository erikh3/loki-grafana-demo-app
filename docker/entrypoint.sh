#!/bin/sh

ROOT_PATH="${ROOT_PATH:=/}"

uvicorn main:app --host 0.0.0.0 --port 8000 --root-path $ROOT_PATH --proxy-headers
