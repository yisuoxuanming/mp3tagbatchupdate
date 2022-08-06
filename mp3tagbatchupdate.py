#! /usr/bin/env python
# encoding: utf-8
import glob
import eyed3
import sys
import os
import click


TAGS = ('album', 'album_artist', 'album_type', 'artist', \
'artist_origin', 'artist_url', 'audio_file_url', 'audio_source_url',\
 'composer', 'copyright', 'copyright_url', 'publisher', 'publisher_url', 'release_date', \
 'tagging_date', 'recording_date', 'title', 'track_num', 'disc_num')

@click.command()
@click.option('--directory', help='mp3所在目录')
@click.option('--album', help='专辑名称')
@click.option('--album_artist', help='专辑作者')
@click.option('--artist', help='艺人')
@click.option('--publisher', help='发行公司')
@click.option('--release_date', help='发行日期')
@click.option('--disc_num')
@click.option('--clear', help='清空原来的标签,不保留原标签内容', is_flag=True)
@click.option('--rename', help='根据title字段重命名文件', is_flag=True)
@click.option('--filenametotitle', help='用文件名设置title', is_flag=True)
@click.option('--dirnametoalbum', help='用目录名设置album', is_flag=True)
@click.option('--verbose', is_flag=True)
def  go(directory, album, album_artist, artist, publisher, release_date, \
    clear, rename, filenametotitle, dirnametoalbum, verbose, disc_num):

    if verbose:
        for k,v in locals().items():
            print(f'{k}: {v}')
    if directory is None:
        directory = os.getcwd()
    else:
        try:
            os.chdir(directory)
        except FileNotFoundError as e:
            print(e)
            sys.exit(1)

    mp3_filenames = glob.glob('*.[mM][pP]3')
    for f in mp3_filenames:
        print(f'Changing tag of {f}')
        mp3 = eyed3.load(f)
        tag_dict = {}
        if not mp3.tag:
            mp3.initTag()
        for i in TAGS:
            tag_dict[i] = getattr(mp3.tag, i)

        if dirnametoalbum:
            album = os.path.basename(directory)

        if filenametotitle:
            tag_dict['title'] = f[:-4] # strip '.mp3'

        if clear:
            #清空原来的标签,用新的标签覆盖
            mp3.tag.clear()
        else:
            mp3.initTag()

        if verbose:
            print(locals())
        for k, v in locals().items():
            if k in TAGS and  v:
                tag_dict[k] = v

        for k, v in tag_dict.items():
            if v:
                if verbose:
                    print(f'Setting mp3.tag.{k} to {v}')
                setattr(mp3.tag, k, v)

        mp3.tag.save()

        if rename:
            print(f'Renaming {f} to {mp3.tag.title}.mp3')
            os.rename(f, f"{mp3.tag.title}.mp3")

if __name__ == '__main__':
    go()
