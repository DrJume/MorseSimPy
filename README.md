# MorseSimPy
> Make your Raspberry Pi into a morse device!

## I. Installation of the client

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

### 3. Connect two buttons to the GPIO Pins
You can define your own in the Morse.py file. 
See "pinDit" for the button activating a short tone and "pinDah" for a long tone.
And the other pin of the button connects to **GROUND**

The server and the client should be on seperate devices. 
The server will be the connection for multiple clients.

## II. Installation of the server

### 1. Install NodeJS
Look up the installation instructions for it

### 2. Install the dependencies
Switch to the server directory and run:
```
npm install
```

### 3. Start the WebSocket server
```
node index.js
```

## Links
http://www.python-exemplarisch.ch/drucken.php?inhalt_mitte=raspi/de/sound.inc.php
https://github.com/Lawouach/WebSocket-for-Python


