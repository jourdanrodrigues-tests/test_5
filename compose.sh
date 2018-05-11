#!/usr/bin/env bash

CURRENT_DIR=$(dirname ${0})

if [ "${1}" == 'dev' ]; then
  shift
  COMMAND="docker-compose -f docker-compose.dev.yml ${@}"
else
  COMMAND="docker-compose ${@}"
fi

if [ "${1}" != 'build' ] && [ "${1}" != 'up' ]; then
  COMMAND="${COMMAND} --rm"
fi

${COMMAND}
