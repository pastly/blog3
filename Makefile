.PHONY: all clean deps find-broken-links

WGET_DIR:= ./wgetcrawl
CRAWL_ROOT_URL:= http://127.0.0.1:8000/

all: | deps build

deps:
	@which hugo
	@which wget

clean:
	rm -rv $(WGET_DIR)

build:
	hugo

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

