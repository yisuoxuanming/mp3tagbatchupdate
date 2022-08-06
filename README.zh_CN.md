# mp3tagbatchupdate
## 说明
一些老mp3 使用 v1版本 tag，且编码不是 `utf-8`。这在 macos及APP 显示为乱码。此脚本批量更新文件夹下的 mp3 文件 tag 信息，使用`eyed3`默认的2.4.0 版本替换mp3文件的tag,把原数据转换为 `utf-8`编码。

`eyed3`在读取mp3 v1版本 tag 时默认使用`latin1`编码，tag.py改为用 chardet自动检测编码,若检测不出则默认使用`gb2312`编码。

## 使用方法
1. 安装`python3`,`eyed3`,`click`
2. tag.py 覆盖 `eyed3`自带的 tag.py (.../site-packages/eyed3/id3/tag.py)
3. 在mp3文件所在目录运行 `mp3tagbatchupdate.py` 或通过 --directory 参数传入目录。



