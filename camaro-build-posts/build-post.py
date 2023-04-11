#!/usr/bin/env python3
import sys
import io
import os
import string
import glob
import json

METADATA_FNAME = 'metadata.json'
THUMB_PREFIX = os.environ['THUMB_PREFIX']
IMG_EXTS = {'.jpeg', '.jpg', '.png'}
VID_EXTS = {'.mp4'}

def log_warn(*a, **kw):
    log('WARN:', *a, **kw)

def log_err(*a, **kw):
    log('ERR:', *a, **kw)

def log(*a, **kw):
    print(*a, file=sys.stderr, **kw)

def find_all_input_files(dname):
    meta = None
    imgs = set()
    vids = set()
    for fname in glob.iglob(f'{dname}/*'):
        if os.path.basename(fname).startswith(THUMB_PREFIX):
            continue
        if os.path.basename(fname) == METADATA_FNAME:
            meta = fname
        for ext_list, out_set in [(IMG_EXTS, imgs), (VID_EXTS, vids)]:
            for ext in ext_list:
                if fname.endswith(ext):
                    out_set.add(fname)
                    break
    return meta, imgs, vids

def read_metadata(fname):
    with open(fname, 'rt') as fd:
        return json.load(fd)

def write_slug(title, date, fd):
    if title and date:
        slug = f'{date}-{title}'
    elif title:
        slug = f'date-{title}'
    elif date:
        slug = f'{date}-title'
    else:
        slug = f'date-title'
    fd.write(f'slug: {slug}\n')

def build_post_content(meta):
    f = io.StringIO('')
    title = meta['title'] if 'title' in meta and meta['title'] else None
    date = meta['date'] if 'date' in meta and meta['date'] else None
    tags = meta['tags'] if 'tags' in meta and meta['tags'] else ["camaro", "cars"]
    f.write('---\n')
    if title:
        f.write(f'title: {title}\n')
    if date:
        f.write(f'date: {date}\n')
    write_slug(title, date, f)
    f.write(f'tags: {tags}\n')
    f.write(f'draft: false\n')
    f.write('---\n')
    if 'body' in meta and meta['body']:
        f.write('<div class=post-body>\n')
        f.write(meta['body'])
        f.write('\n</div>\n')
    if 'media_groups' in meta and meta['media_groups']:
        for media_group in meta['media_groups']:
            f.write(f'<div class=post-media-group>\n')
            if 'caption' in media_group and media_group['caption']:
                caption = media_group['caption']
                f.write('<div class=post-media-group-caption>\n')
                f.write(caption)
                f.write('</div>\n')
            f.write('<div class=post-media-group-media>\n')
            for media_item in media_group['media']:
                if os.path.splitext(media_item)[-1] in IMG_EXTS:
                    f.write(f'<a href="{media_item}"><img src="{THUMB_PREFIX}{media_item}"></a>\n')
                elif os.path.splitext(media_item)[-1] in VID_EXTS:
                    f.write(f'<video src="{media_item}" controls>\n')
                else:
                    log_warn(f'Media file without known extension, ignoring: {media_item}')
            f.write('</div>\n')
            f.write('</div>\n')
    f.seek(0, 0)
    return f.read()


def main(output_fname):
    post_dname = '.'
    meta, _, _ = find_all_input_files(post_dname)
    if not meta:
        log_err(f'No {METADATA_FNAME} found in {post_dname}')
        return 1
    meta = read_metadata(meta)
    with open(output_fname, 'wt') as fd:
        fd.write(build_post_content(meta))
    return 0

if __name__ == '__main__':
    output_fname = sys.argv[1]
    exit(main(output_fname))
