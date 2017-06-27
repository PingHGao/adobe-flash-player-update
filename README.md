# adobe-flash-player-update
A pyhton script to automatically update your adobe flash player for Firefox, Linux 64-bit.

## Requirements
* Python2.7
* Linux 64-bit(Successfully tested on Ubuntu 14.04)
* Firefox

## Use
#### Download sources and execute
```Shell
git clone https://github.com/PingHGao/adobe-flash-player-update
cd adobe-flash-player-update
python flashplayer_update.py
```
#### It will download installer.tar.gz in folder /tmp/flashplayer and extract there. Then it will copy xxx.so to usr/lib/mozilla/plugins/ and usr/* to /usr/.
