# Installation

### 1. Install the dependencies
```
sudo apt-get install sox libsox-fmt-mp3 -y
sudo pip install ws4py
```

### 2. Edit the file "/home/pi/.asoundrc"
```
pcm.!default {
type hw
card 0
}

ctl.!default {
type hw
card 0
}
```

## Links
http://www.python-exemplarisch.ch/drucken.php?inhalt_mitte=raspi/de/sound.inc.php
https://github.com/Lawouach/WebSocket-for-Python


