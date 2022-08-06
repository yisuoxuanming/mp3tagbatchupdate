# mp3tagbatchupdate
## 说明
一些mp3 的 ID3tag使用中文且编码不是 `utf-8`。这在 macos及APP 显示为乱码。此脚本批量更新文件夹下的 mp3 文件 tag 信息，使用`eyed3`默认的2.4.0 版本替换mp3文件的ID3 tag。


## 使用方法
1. 安装`python3`,`eyed3`,`click`
3. 在mp3文件所在目录运行 `mp3tagbatchupdate.py` 或通过 --directory 参数传入目录。



