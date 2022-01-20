include makefiles/env.mk
include makefiles/formatter.mk

CONTAINER_NAME=text-replacer-api
FILE=tests
FUNC=""

.PHONY: build
build: env
	docker-compose build


.PHONY: up
up: env
	docker-compose up


.PHONY: bash
bash: env
	docker-compose run --rm ${CONTAINER_NAME} /bin/bash


.PHONY: test
test: env
	docker-compose run --rm ${CONTAINER_NAME} pytest -s ${FILE} -k ${FUNC}


.PHONY deploy:
deploy: config
	gcloud builds submit --config cloudbuild.yaml \
	--substitutions \
	^---^_PROJECT=${_PROJECT}\
	---_VERSION=${_VERSION}\
	---_SERVICE=${_SERVICE}\
	---_IMAGE=${_IMAGE}\
	---_REGION=${_REGION}\
	---_TARGET=${_TARGET}\
	---_MEMORY=${_MEMORY}\
	---_CONCURRENCY=${_CONCURRENCY}\
	---_MAX_INSTANCES=${_MAX_INSTANCES}\
	---_DEBUG=${_DEBUG}


.PHONY: clean
clean:
	docker-compose down --rmi all --volumes
