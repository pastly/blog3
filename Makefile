SHELL := $(shell which bash)
.PHONY: all \
	build \
	deploy

all: build

serve:
	cd hugo; hugo server $(HUGO_EXTRA_OPTS)

build:
	source options.env; \
	tup; \
	cd hugo; \
	hugo --destination $$HUGO_PUBLISH_DIR; \


deploy: build
	source options.env; \
	cd hugo; \
	rsync --delete -air $$HUGO_PUBLISH_DIR/ $$RSYNC_DEST

#deploy: build
#	rsync \
#		-air \
#		--delete \
#		$(PUBLISH_DIR)/ \
#		$(RSYNC_HOST):$(RSYNC_DIR)

