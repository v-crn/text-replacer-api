_DEBUG=True
_IMAGE=text-replacer-api
_REGION=us-west1
_SERVICE=TextReplacer-API
_VERSION=1.0.0
PORT=5000

.PHONY: config
config:
	$(eval _PROJECT:=your-project)
	$(eval _REGION:=us-west1)
	$(eval _IMAGE:=text-replacer-api)
	$(eval _SERVICE:=text-replacer-api)
	$(eval _TARGET:=prd)
	$(eval _MEMORY:=128Mi)
	$(eval _MAX_INSTANCES:=1)
	$(eval _CONCURRENCY:=1)


.PHONY: env
env:
	echo API_SERVICE_NAME=${_SERVICE} > .env
	echo API_VERSION=${_VERSION} >> .env
	echo DEBUG=${_DEBUG} >> .env
	echo PORT=${PORT} >> .env
