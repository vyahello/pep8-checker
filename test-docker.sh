#!/bin/bash

IMAGE_FULL_NAME=${IMAGE_REPO}:${IMAGE_VERSION}


test-help-command() {
:<<DOC
    Test "help" command of a tool
DOC
    echo -e "\n\n Test docker image help command"
    (docker run --rm ${IMAGE_FULL_NAME} | grep help)  \
          || (echo 'Cannot verify help command' && exit 100)
    (docker run --rm ${IMAGE_FULL_NAME} -h | grep help) \
          || (echo 'Cannot verify help command' && exit 100)
    (docker run --rm ${IMAGE_FULL_NAME} --help | grep help) \
          || (echo 'Cannot verify help command' && exit 100)
}


test-checker-command() {
:<<DOC
    Test "checker" command of a tool
DOC
    echo -e "\n\n Test docker image checker command"
    (docker run --rm ${IMAGE_FULL_NAME} | grep checker) \
          || (echo 'Cannot verify checker command' && exit 100)
}


test-image-version() {
:<<DOC
    Test "version" of a docker image
DOC
    echo -e "\n\n Test docker image version"
    (docker run --rm ${IMAGE_FULL_NAME} | grep ${IMAGE_VERSION}) \
          || (echo 'Docker image version is wrong' && exit 100)
}


cleanup() {
:<<DOC
    Cleans up environment
DOC
    docker rmi ${IMAGE_FULL_NAME}
}


main() {
:<<DOC
    Runs unit tests
DOC
    echo -e "\n\n Docker image assessment"
    test-help-command && \
    test-checker-command && \
    test-image-version && \
    cleanup
    echo -e "\n\n Docker image is ready to go"
}


main