import time
from soundplayer import SoundPlayer
from ws4py.client.threadedclient import WebSocketClient
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

pinDit = 19
pinDah = 26
GPIO.setup(pinDit, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(pinDah, GPIO.IN, pull_up_down=GPIO.PUD_UP)

unit = 18

def dit():
    SoundPlayer.playTone(500, 0.18, 0.05, False, 0)
def dah():
    SoundPlayer.playTone(500, 0.54, 0.05, False, 0)

morseBuffer = []

class MorseClient(WebSocketClient):
    def opened(self):
        #self.send('------')
        pass

    def closed(self, code, reason=None):
        print "Closed down", code, reason

    def received_message(self, message):
        #morseBuffer.append('/')
        morseBuffer.extend(list(str(message)))
        print(str(morseBuffer))

try:
    ws = MorseClient('ws://[SERVER-IP]:[PORT]/')
    ws.connect()

    sendBuffer = []

    ditClicked = False
    dahClicked = False
    timer = 0
    playing = 0
    timeBetweenClicks = 0

    while True:
        if timer % 5 == 0:
            # Button input
            if GPIO.input(pinDit) == True:
                ditClicked = True

            if GPIO.input(pinDah) == True:
                dahClicked = True

            if  GPIO.input(pinDit) == False and ditClicked == True:
                ditClicked = False
                #print('Dit')
                sendBuffer.append('.')
                timeBetweenClicks = 0

            if  GPIO.input(pinDah) == False and dahClicked == True:
                dahClicked = False
                #print('Dah')
                sendBuffer.append('-')
                timeBetweenClicks = 0

        if timeBetweenClicks >= 45:
            if sendBuffer:
                if sendBuffer[-1] != '*' and sendBuffer[-1] != '/':
                    sendBuffer.append('*')
                    print("LETTER")    

        if timeBetweenClicks >= 210:
            if sendBuffer:
                if sendBuffer[-1] == '*':
                    sendBuffer[-1] = '/'
                    ws.send(''.join(sendBuffer))
                    print(''.join(sendBuffer))
                    sendBuffer = []
                    print("WORD")
            timeBetweenClicks = 0  

        if timer % 5 == 0 and playing < 0:
            if morseBuffer:
                if morseBuffer[0] == '-':
                    del morseBuffer[0]
                    dah()
                    playing = (3*unit)+unit
                elif morseBuffer[0] == '.':
                    del morseBuffer[0]
                    dit()
                    playing = unit+unit
                elif morseBuffer[0] == '*':
                    del morseBuffer[0]
                    playing = 3*unit
                elif morseBuffer[0] == '/':
                    del morseBuffer[0]
                    playing = 7*unit

        timer += 1
        playing -= 1
        timeBetweenClicks += 1
        time.sleep(0.01)
except KeyboardInterrupt:
    ws.close()
    GPIO.cleanup()





"""
print "done"

morse_string_off = '.... .- .-.. .-.. --- / - ..- / ... - .- -.-. .... ..-'
morse_string = raw_input("Give meh da morse code, camrat:")

for x in morse_string:
    if x == '.':
        dit()
    elif x == '-':
        dah()
    elif x == ' ':
        time.sleep(0.45)
    elif x == '/':
        time.sleep(0.9)

"""