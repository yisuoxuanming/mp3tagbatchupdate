# mp3tagbatchupdate
## Description (中文说明在 README.zh_CN.md 中)
This is for batch updating old mp3 tags in MacOS, changing V1 tag to V2(2.4.0), changing tag text encoding to `utf-8`.

`eyed3`decodes v1 tag text using `latin1` by default which is unable to decode CJK language correctly. I use `chardet` to detect text encoding, return `gb2312` if failed. Tag texts pass in by parameters overwrite original text.

## How to use
1. Install `python3`,`eyed3`,`click`,`chardet`
2. Use `tag.py` to overwrite `eyed3`'s `tag.py` (In my case : .../site-packages/eyed3/id3/tag.py)
3. run `mp3tagbatchupdate.py` in mp3 files directory or use `--directory` parameter。
