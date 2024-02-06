#!/usr/bin/env python3
import sys
import glob
import shutil
import time
import os
import json
import string

IMG_EXTS = ['.jpeg', '.jpg', '.png']
VID_EXTS = ['.mp4']
MISC_EXTS = [
    '.dl', # holly term x data log
    '.drawio', # diagrams.net
]

def get_folder_name(meta):
    title = meta['title'].lower()
    title = title.translate(str.maketrans('', '', string.punctuation))
    title = '-'.join(title.split())
    return f'{title}'


def find_content_dnames(root):
    for name in glob.iglob(f'{root}/*/'):
        yield name

def gen_dir_map(src_iter, dest_root):
    d = {}
    for src in src_iter:
        with open(f'{src}/metadata.json', 'rt') as fd:
            slug = get_folder_name(json.load(fd))
        d[src] = f'{dest_root}/{slug}'
    return d


def main(src_root, dest_root, tup_fd):
    dir_map = gen_dir_map(find_content_dnames(src_root), dest_root)
    #print('include_rules', file=tup_fd)
    for item in dir_map.items():
        os.makedirs(item[1], exist_ok=True)
        l = []
        l += [f': {item[0]}/index.html |> cp %f %o |> {item[1]}/index.html']
        for ext in IMG_EXTS + VID_EXTS + MISC_EXTS:
            l += [f': foreach {item[0]}/*{ext} |> cp %f %o |> {item[1]}/%b']
        for s in l:
            print(s, file=tup_fd)

if __name__ == '__main__':
    src_root = sys.argv[1]
    dest_root = sys.argv[2]
    tup_fname = sys.argv[3]
    with open(tup_fname, 'wt') as fd:
        exit(main(src_root, dest_root, fd))
