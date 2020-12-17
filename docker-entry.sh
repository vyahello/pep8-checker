#!/bin/bash


helper() {
:<<DOC
    Shows 'help' message
DOC
    cat <<HELP
    This program allows to launch pep8-checker application via docker image.
    Please use next command:
      - 'help' to see tool help
         docker run ${IMAGE_REPO}:${IMAGE_VERSION} --help
      - 'checker' to run pep8-checker web application
         docker run -it -p {local-port}:5050 ${IMAGE_REPO}:${IMAGE_VERSION} checker
HELP
}


checker() {
:<<DOC
    Entrypoint to launch 'pep8-checker' web application
DOC
    python -m checker
}


main() {
:<<DOC
    Launches 'main' tools executor
DOC
    if (
        [[ "$1" == "-h" ]] ||
        [[ "$1" == "--help" ]] ||
        [[ "$1" == "help" ]] ||
        [[ $# -eq 0 ]]
    ); then
        helper
        exit 0
    fi
    local cmd=$1; shift
    eval "${cmd} $@"
}


main $@
