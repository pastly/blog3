.PHONY: all deps clean deploy find-broken-links

WGET_DIR:= ./wgetcrawl
PUBLISH_DIR:=../docker/publishdir
#PUBLISH_DIR:=publishdir
CRAWL_ROOT_URL:= http://127.0.0.1:8000/
RSYNC_HOST:=piggie
RSYNC_DIR:=/var/www/matt.traudt.xyz
BUILD_ARGS:=

all: | deps build

deps:
	@which hugo
	@which wget

clean:
	rm -rv $(WGET_DIR)

deploy: build
	rsync \
		-air \
		--delete \
		$(PUBLISH_DIR)/ \
		$(RSYNC_HOST):$(RSYNC_DIR)

build:
	hugo --destination $(PUBLISH_DIR) $(BUILD_ARGS)

find-broken-links:
	mkdir -pv $(WGET_DIR)
	wget \
		--recursive \
		--level inf \
		--wait 0.05 \
		--page-requisites \
		--no-host-directories \
		--directory-prefix $(WGET_DIR) \
		--output-file $(WGET_DIR)/crawl.log \
		$(CRAWL_ROOT_URL)

