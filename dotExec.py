from licensing.models import *
from licensing.methods import Key, Helpers
from subprocess import *

RSAPubKey = "<RSAKeyValue><Modulus>8tN/s/xeVqkg/ssHXggfsDYpt/dlVq2kXkKLZnN+vxLZQ8Wr0YQfnTInCpys3t1gQ6ZJoAJ+hSvsywrD7TKaD8OlOD+EycV/tYQLF9NE58osjkrNSPe0I9R4L8n9WRXkdmfmAnB5Mc21FULUrKbhXPmV2A82GA4bSgrhSLGD504DAVqevqkm/wuBpWvKdBiCkJVebgELxgMCuxLvFMT3AsqC2TLs9XQXtS1qSoRd3396IoreEE86+D2bgPiKXSYRJ2UGZSmOqm6arSDXn0ILQ4zfxFtTkyT1QYn2VbrsICAmanRLwyX8w1IsYNE/fVe1snH0edh1N+L+8KayLbZ8RQ==</Modulus><Exponent>AQAB</Exponent></RSAKeyValue>"
auth = "WyI5MjU2MSIsImFGRitKOFc1Tjlmd1l4MGhIWnVXdEorTXg5VnBMV2x0WGlRN1RhMGkiXQ=="


def AuthKey():
    key = str(input("Auth KEY: "))
    result = Key.activate(token=auth,
                          rsa_pub_key=RSAPubKey,
                          product_id=7462,
                          key=key,
                          machine_code=Helpers.GetMachineCode())

    if result[0] == None or not Helpers.IsOnRightMachine(result[0]):
        print("Key Invalida".format(result[1]))
        AuthKey()


    else:
        print("Key Valida...")
        pass

AuthKey()

time.sleep(2)

import time
import os
import pyautogui
import pyautogui as pyautogui
import pydirectinput
import autoit
from python_imagesearch.imagesearch import imagesearch_loop, imagesearch
from pynput.keyboard import Key, Controller

clear = lambda: os.system("cls")

pyautogui.FAILSAFE = False
TIMELAPSE = 1

acceptButtonImg = './content/sample1.png'
acceptedButtonImg = './content/sample-accepted.png'
championSelectionImg_flash = './content/flash-icon.png'
championSelectionImg_emote = './content/emote-icon.png'
playButtonImg = './content/play-button.png'

keyb = Controller()
mouse = Controller()

clear()

print(" _______          _________ _        _______  ______  _________")
print("(  ____ \|\     /|\__   __/( (    /|(  ___  )(  ___ \ \__   __/")
print("| (    \/| )   ( |   ) (   |  \  ( || (   ) || (   ) )   ) (   ")
print("| (_____ | (___) |   | |   |   \ | || |   | || (__/ /    | |   ")
print("(_____  )|  ___  |   | |   | (\ \) || |   | ||  __ (     | |   ")
print("      ) || (   ) |   | |   | | \   || |   | || (  \ \    | |   ")
print("/\____) || )   ( |___) (___| )  \  || (___) || )___) )___) (___")
print("\_______)|/     \|\_______/|/    )_)(_______)|/ \___/ \_______/")


time.sleep(10)

keyb.press(Key.cmd)
keyb.press('r')
keyb.release(Key.cmd)
keyb.release('r')

print("Iniciando...")

time.sleep(2)


def newTab():
    cords1 = pyautogui.locateCenterOnScreen('./content/winr.png') or pyautogui.locateCenterOnScreen('./content/winb.png')
    pyautogui.click(cords1)
newTab()

keyb.type('C:\Riot Games\League of Legends\LeagueClient.exe') #Caminho do lol

keyb.press(Key.enter)
keyb.release(Key.enter)

print("Localizando Servidor...") ##Abrindo LoL

time.sleep(2)

print("Localizando Servidor...")
print("Localizando Servidor...")
print("Localizando Servidor...")

time.sleep(10)

while True:
    if pyautogui.locateOnScreen('./content/username.png'):
        pyautogui.click(pyautogui.locateOnScreen('./content/username.png'))
        break

print("Logando...")

file = open('./login/username.txt',"r")
keyb.type(file.read())

time.sleep(1)

def newTab():
    cords4 = pyautogui.locateCenterOnScreen('./content/pass.png')
    pyautogui.click(cords4)
newTab()

file = open('./login/password.txt',"r")
keyb.type(file.read())

time.sleep(0.5)

keyb.press(Key.enter)
keyb.release(Key.enter)

time.sleep(10)

while True:
    playb = pyautogui.locateCenterOnScreen('./content/play1.png')
    if playb:
        pyautogui.click(playb)
        break
    else:
        break

print("Logando...")

while True:
    if pyautogui.locateOnScreen('./content/email.png'):
        pyautogui.click(pyautogui.locateOnScreen('./content/x2.png'))
        break
    if not pyautogui.locateOnScreen('./content/email.png'):
        break

print("connecting..")
time.sleep(1)

while True:
    clash = pyautogui.locateCenterOnScreen('./content/clash.png')
    gotit = pyautogui.locateCenterOnScreen('./content/gotit.png')
    if clash:
        pyautogui.click(gotit)
        break
    if not clash:
        break

print("connecting....")
time.sleep(1)

while True:
    welcome = pyautogui.locateCenterOnScreen('./content/welcome.png')
    tft = pyautogui.locateCenterOnScreen('./content/tft.png')
    if welcome:
        pyautogui.click(tft)
        break
    if not welcome:
        break

print("connecting.....")
time.sleep(1)

while True:
    galaxies = pyautogui.locateCenterOnScreen('./content/galaxies.png')
    x1 = pyautogui.locateCenterOnScreen('./content/x.png')
    if galaxies:
        pyautogui.click(x1)
        break
    if not galaxies:
        break

print("connecting......")
time.sleep(1)

while True:
    lvlup = pyautogui.locateCenterOnScreen('./content/missions.png') or pyautogui.locateCenterOnScreen('./content/bok.png') or pyautogui.locateCenterOnScreen('./content/daily.png')
    if lvlup:
        time.sleep(5)
        pyautogui.click(637, 387)
        time.sleep(2)
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/lvlup.png'))
        # time.sleep(1)
        # autoit.mouse_click("left", 641, 636)
        break
    if not lvlup:
        break

print("connecting......")
time.sleep(1)

while True:
    if pyautogui.locateOnScreen('./content/play.png'):
        pyautogui.click(pyautogui.locateOnScreen('./content/play.png'))
        break

print("connecting.......")
time.sleep(2)

while True:
    if pyautogui.locateOnScreen('./content/coop.png') or pyautogui.locateOnScreen('./content/coop1.png') or pyautogui.locateOnScreen('./content/coop2.png'):
        pyautogui.click(pyautogui.locateOnScreen('./content/coop.png') or pyautogui.locateOnScreen('./content/coop1.png') or pyautogui.locateOnScreen('./content/coop2.png'))
        break

time.sleep(0.5)

def newTab():
    cords7 = pyautogui.locateCenterOnScreen('./content/intro.png')
    pyautogui.click(cords7)
newTab()

time.sleep(2)

def newTab():
    cords8 = pyautogui.locateCenterOnScreen('./content/confirm.png')
    pyautogui.click(cords8)
newTab()

clear()
print("Criando Lobby")


pyautogui.moveTo(0, 0)

while True:
    if pyautogui.locateOnScreen('./content/findm.png'):
        pyautogui.click(pyautogui.locateOnScreen('./content/findm.png'))
        break

print("Entrando em Fila")

                                                                #QUEUE

while True:
    if pyautogui.locateCenterOnScreen('./content/sample1.png'):
        pyautogui.click('./content/sample1.png')
        print("Jogo aceito!")
        pyautogui.moveTo(0, 0)

    if pyautogui.locateCenterOnScreen('./content/cancel.png'):
        print("Partida recusada")
    if pyautogui.locateCenterOnScreen('./content/choose.png'):
        print("Seleção de campeões!")
        break

while True:
    champ = pyautogui.locateCenterOnScreen('./content/tristana.png') or pyautogui.locateCenterOnScreen('./content/ez.png') or pyautogui.locateCenterOnScreen('./content/morgana.png') or pyautogui.locateCenterOnScreen('./content/mf.png') or pyautogui.locateCenterOnScreen('./content/ahri.png') or pyautogui.locateCenterOnScreen('./content/lux.png') or pyautogui.locateCenterOnScreen('./content/master.png') or pyautogui.locateCenterOnScreen('./content/darius.png')
    if champ:
        pyautogui.click(champ)
        break

time.sleep(1)

while True:
    if pyautogui.locateCenterOnScreen('./content/lock.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/lock.png'))
        break

clear()

print(" _______          _________ _        _______  ______  _________")
print("(  ____ \|\     /|\__   __/( (    /|(  ___  )(  ___ \ \__   __/")
print("| (    \/| )   ( |   ) (   |  \  ( || (   ) || (   ) )   ) (   ")
print("| (_____ | (___) |   | |   |   \ | || |   | || (__/ /    | |   ")
print("(_____  )|  ___  |   | |   | (\ \) || |   | ||  __ (     | |   ")
print("      ) || (   ) |   | |   | | \   || |   | || (  \ \    | |   ")
print("/\____) || )   ( |___) (___| )  \  || (___) || )___) )___) (___")
print("\_______)|/     \|\_______/|/    )_)(_______)|/ \___/ \_______/")

print("Esperando por jogadores")

time.sleep(10)

while True:
    if pyautogui.locateCenterOnScreen('./content/t1.png'):
        break

print("Jogo Iniciado")

time.sleep(2)

pydirectinput.press('p')

print("Comprando Itens")

time.sleep(2)
autoit.mouse_click("right", 277, 170)
time.sleep(1)
autoit.mouse_click("right", 522, 178)
autoit.mouse_click("right", 522, 178)

time.sleep(1)

pydirectinput.press('esc')

def newTab():
    pydirectinput.moveTo(539, 354)
newTab()

print("Jogando...")

while True:                            #JOGANDO
    pydirectinput.keyDown('f2')
    time.sleep(1)
    autoit.mouse_click("right", 539, 354)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 471, 306)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 481, 443)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 539, 354)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 539, 354)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 471, 306)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 481, 443)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 539, 354)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 539, 354)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 471, 306)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 481, 443)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 539, 354)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 539, 354)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 471, 306)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 481, 443)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 539, 354)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 539, 354)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 471, 306)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 481, 443)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 539, 354)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 539, 354)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 471, 306)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 481, 443)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 539, 354)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 539, 354)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 471, 306)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 481, 443)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 539, 354)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 539, 354)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 471, 306)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 481, 443)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 539, 354)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 539, 354)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 471, 306)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 481, 443)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 539, 354)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 539, 354)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 471, 306)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 481, 443)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 539, 354)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 539, 354)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 471, 306)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 481, 443)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 539, 354)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 539, 354)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 471, 306)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 481, 443)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 539, 354)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 539, 354)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 471, 306)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 481, 443)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 539, 354)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 539, 354)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 471, 306)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 481, 443)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 539, 354)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 539, 354)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 471, 306)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 481, 443)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 539, 354)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 539, 354)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 471, 306)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 481, 443)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 539, 354)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 539, 354)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 471, 306)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 481, 443)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 539, 354)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 539, 354)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 471, 306)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 481, 443)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 539, 354)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 539, 354)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 471, 306)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 481, 443)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 539, 354)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 539, 354)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 471, 306)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 481, 443)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 539, 354)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 539, 354)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 471, 306)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 481, 443)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 539, 354)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 539, 354)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 471, 306)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 481, 443)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 539, 354)
    pydirectinput.keyUp("f2")
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    ##################################################################
    pydirectinput.keyDown('f3')
    time.sleep(1)
    autoit.mouse_click("right", 539, 354)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 471, 306)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 481, 443)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 539, 354)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 539, 354)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 471, 306)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 481, 443)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 539, 354)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 539, 354)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 471, 306)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 481, 443)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 539, 354)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 539, 354)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 471, 306)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 481, 443)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 539, 354)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 539, 354)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 471, 306)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 481, 443)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 539, 354)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 539, 354)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 471, 306)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 481, 443)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 539, 354)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 539, 354)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 471, 306)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 481, 443)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 539, 354)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 539, 354)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 471, 306)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 481, 443)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 539, 354)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 539, 354)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 471, 306)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 481, 443)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 539, 354)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 539, 354)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 471, 306)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 481, 443)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 539, 354)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 539, 354)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 471, 306)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 481, 443)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 539, 354)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 539, 354)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 471, 306)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 481, 443)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 539, 354)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 539, 354)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 471, 306)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 481, 443)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 539, 354)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 539, 354)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 471, 306)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 481, 443)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 539, 354)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 539, 354)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 471, 306)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 481, 443)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 539, 354)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 539, 354)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 471, 306)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 481, 443)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 539, 354)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 539, 354)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 471, 306)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 481, 443)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 539, 354)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 539, 354)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 471, 306)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 481, 443)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 539, 354)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 539, 354)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 471, 306)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 481, 443)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 539, 354)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 539, 354)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 471, 306)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 481, 443)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 539, 354)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 539, 354)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 471, 306)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 481, 443)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 539, 354)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 539, 354)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 471, 306)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 481, 443)
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break
    autoit.mouse_click("right", 539, 354)
    pydirectinput.keyUp("f3")
    if pyautogui.locateCenterOnScreen('./content/win1.png'):
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
        break

print("Jogo finalizado")

time.sleep(60)

while True:
    if pyautogui.locateOnScreen('./content/email.png'):
        pyautogui.click(pyautogui.locateOnScreen('./content/x2.png'))
        break
    if not pyautogui.locateOnScreen('./content/email.png'):
        break



#after game
while True:
    lvlup = pyautogui.locateCenterOnScreen('./content/missions.png') or pyautogui.locateCenterOnScreen('./content/bok.png') or pyautogui.locateCenterOnScreen('./content/daily.png')
    if lvlup:
        time.sleep(5)
        pyautogui.click(637, 366)
        time.sleep(2)
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/lvlup.png'))
        # time.sleep(1)
        # autoit.mouse_click("left", 641, 636)
        break
    if not lvlup:
        break

while True:
    lvlup1 = pyautogui.locateCenterOnScreen('./content/lvlup1.png')
    if lvlup1:
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/lvlup.png'))
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/lvlup.png'))
        time.sleep(2)
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/lvlup.png'))
        time.sleep(1)
        pyautogui.click(pyautogui.locateCenterOnScreen('./content/lvlup.png'))
        time.sleep(1)
        break
    if not lvlup1:
        break

# while True:
# daily = pyautogui.locateCenterOnScreen('.content/bok.png')
# if daily:
# autoit.mouse_click("left", 634, 364)
# time.sleep(1)
# autoit.mouse_click("left", 636, 596)
# break
# if not daily:
# break

while True:
    missions = pyautogui.locateCenterOnScreen('./content/missions.png')
    if missions:
        pyautogui.click(637, 598)
        time.sleep(1)
        break
    if not missions:
        break

while True:
    if pyautogui.locateOnScreen('./content/againp.png'):
        pyautogui.click(pyautogui.locateOnScreen('./content/againp.png'))
        break

pyautogui.moveTo(0, 0)


#RECOMEÇA

while True:

    clear()

    print(" _______          _________ _        _______  ______  _________")
    print("(  ____ \|\     /|\__   __/( (    /|(  ___  )(  ___ \ \__   __/")
    print("| (    \/| )   ( |   ) (   |  \  ( || (   ) || (   ) )   ) (   ")
    print("| (_____ | (___) |   | |   |   \ | || |   | || (__/ /    | |   ")
    print("(_____  )|  ___  |   | |   | (\ \) || |   | ||  __ (     | |   ")
    print("      ) || (   ) |   | |   | | \   || |   | || (  \ \    | |   ")
    print("/\____) || )   ( |___) (___| )  \  || (___) || )___) )___) (___")
    print("\_______)|/     \|\_______/|/    )_)(_______)|/ \___/ \_______/")

    time.sleep(5)


    def newTab():
        cords9 = pyautogui.locateCenterOnScreen('./content/findm.png')
        pyautogui.click(cords9)
    newTab()

    print("Na Fila...")

    while True:
        if pyautogui.locateCenterOnScreen('./content/sample1.png'):
            pyautogui.click('./content/sample1.png')
            print("Jogo aceito!")
            pyautogui.moveTo(0, 0)

        if pyautogui.locateCenterOnScreen('./content/cancel.png'):
            print("Partida recusada")
        if pyautogui.locateCenterOnScreen('./content/choose.png'):
            ("Seleção de campeões!")
            break

    while True:
        champ = pyautogui.locateCenterOnScreen('./content/tristana.png') or pyautogui.locateCenterOnScreen('./content/ez.png') or pyautogui.locateCenterOnScreen('./content/morgana.png') or pyautogui.locateCenterOnScreen('./content/mf.png') or pyautogui.locateCenterOnScreen('./content/ahri.png') or pyautogui.locateCenterOnScreen('./content/lux.png') or pyautogui.locateCenterOnScreen('./content/master.png') or pyautogui.locateCenterOnScreen('./content/darius.png')
        if champ:
            pyautogui.click(champ)
            break

    time.sleep(1)

    while True:
        if pyautogui.locateCenterOnScreen('./content/lock.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/lock.png'))
            break

    clear()

    print(" _______          _________ _        _______  ______  _________")
    print("(  ____ \|\     /|\__   __/( (    /|(  ___  )(  ___ \ \__   __/")
    print("| (    \/| )   ( |   ) (   |  \  ( || (   ) || (   ) )   ) (   ")
    print("| (_____ | (___) |   | |   |   \ | || |   | || (__/ /    | |   ")
    print("(_____  )|  ___  |   | |   | (\ \) || |   | ||  __ (     | |   ")
    print("      ) || (   ) |   | |   | | \   || |   | || (  \ \    | |   ")
    print("/\____) || )   ( |___) (___| )  \  || (___) || )___) )___) (___")
    print("\_______)|/     \|\_______/|/    )_)(_______)|/ \___/ \_______/")

    print("Esperando por jogadores")

    time.sleep(3)

    print("Localizando servidores...")

    time.sleep(10)

    while True:
        if pyautogui.locateCenterOnScreen('./content/t1.png'):
            break

    print("Jogo Iniciado")

    time.sleep(2)

    pydirectinput.press('p')

    print("Comprando Itens")

    time.sleep(2)
    autoit.mouse_click("right", 277, 170)
    time.sleep(1)
    autoit.mouse_click("right", 522, 178)
    autoit.mouse_click("right", 522, 178)

    time.sleep(1)

    pydirectinput.press('esc')

    def newTab():
        pydirectinput.moveTo(539, 354)
    newTab()

    print("Jogando...")

    while True:  # JOGANDO
        pydirectinput.keyDown('f2')
        time.sleep(1)
        autoit.mouse_click("right", 539, 354)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 471, 306)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 481, 443)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 539, 354)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 539, 354)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 471, 306)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 481, 443)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 539, 354)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 539, 354)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 471, 306)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 481, 443)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 539, 354)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 539, 354)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 471, 306)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 481, 443)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 539, 354)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 539, 354)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 471, 306)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 481, 443)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 539, 354)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 539, 354)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 471, 306)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 481, 443)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 539, 354)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 539, 354)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 471, 306)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 481, 443)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 539, 354)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 539, 354)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 471, 306)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 481, 443)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 539, 354)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 539, 354)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 471, 306)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 481, 443)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 539, 354)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 539, 354)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 471, 306)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 481, 443)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 539, 354)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 539, 354)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 471, 306)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 481, 443)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 539, 354)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 539, 354)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 471, 306)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 481, 443)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 539, 354)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 539, 354)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 471, 306)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 481, 443)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 539, 354)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 539, 354)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 471, 306)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 481, 443)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 539, 354)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 539, 354)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 471, 306)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 481, 443)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 539, 354)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 539, 354)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 471, 306)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 481, 443)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 539, 354)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 539, 354)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 471, 306)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 481, 443)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 539, 354)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 539, 354)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 471, 306)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 481, 443)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 539, 354)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 539, 354)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 471, 306)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 481, 443)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 539, 354)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 539, 354)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 471, 306)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 481, 443)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 539, 354)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 539, 354)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 471, 306)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 481, 443)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 539, 354)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 539, 354)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 471, 306)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 481, 443)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 539, 354)
        pydirectinput.keyUp("f2")
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        #############################################################
        pydirectinput.keyDown('f3')
        time.sleep(1)
        autoit.mouse_click("right", 539, 354)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 471, 306)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 481, 443)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 539, 354)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 539, 354)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 471, 306)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 481, 443)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 539, 354)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 539, 354)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 471, 306)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 481, 443)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 539, 354)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 539, 354)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 471, 306)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 481, 443)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 539, 354)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 539, 354)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 471, 306)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 481, 443)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 539, 354)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 539, 354)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 471, 306)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 481, 443)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 539, 354)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 539, 354)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 471, 306)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 481, 443)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 539, 354)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 539, 354)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 471, 306)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 481, 443)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 539, 354)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 539, 354)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 471, 306)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 481, 443)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 539, 354)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 539, 354)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 471, 306)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 481, 443)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 539, 354)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 539, 354)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 471, 306)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 481, 443)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 539, 354)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 539, 354)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 471, 306)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 481, 443)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 539, 354)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 539, 354)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 471, 306)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 481, 443)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 539, 354)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 539, 354)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 471, 306)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 481, 443)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 539, 354)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 539, 354)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 471, 306)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 481, 443)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 539, 354)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 539, 354)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 471, 306)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 481, 443)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 539, 354)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 539, 354)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 471, 306)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 481, 443)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 539, 354)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 539, 354)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 471, 306)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 481, 443)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 539, 354)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 539, 354)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 471, 306)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 481, 443)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 539, 354)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 539, 354)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 471, 306)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 481, 443)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 539, 354)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 539, 354)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 471, 306)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 481, 443)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 539, 354)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 539, 354)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 471, 306)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 481, 443)
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break
        autoit.mouse_click("right", 539, 354)
        pydirectinput.keyUp("f3")
        if pyautogui.locateCenterOnScreen('./content/win1.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/win1.png'))
            break

    print("Jogo Finalizado!")

    time.sleep(60)

    while True:
        if pyautogui.locateOnScreen('./content/email.png'):
            pyautogui.click(pyautogui.locateOnScreen('./content/x2.png'))
            break
        if not pyautogui.locateOnScreen('./content/email.png'):
            break

    # after game
    while True:
        lvlup = pyautogui.locateCenterOnScreen('./content/missions.png') or pyautogui.locateCenterOnScreen(
            './content/bok.png') or pyautogui.locateCenterOnScreen('./content/daily.png')
        if lvlup:
            time.sleep(5)
            pyautogui.click(637, 366)
            time.sleep(2)
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/lvlup.png'))
            # time.sleep(1)
            # autoit.mouse_click("left", 641, 636)
            break
        if not lvlup:
            break

    while True:
        lvlup1 = pyautogui.locateCenterOnScreen('./content/lvlup1.png')
        if lvlup1:
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/lvlup.png'))
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/lvlup.png'))
            time.sleep(2)
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/lvlup.png'))
            time.sleep(1)
            pyautogui.click(pyautogui.locateCenterOnScreen('./content/lvlup.png'))
            time.sleep(1)
            break
        if not lvlup1:
            break

    # while True:
    # daily = pyautogui.locateCenterOnScreen('.content/bok.png')
    # if daily:
    # autoit.mouse_click("left", 634, 364)
    # time.sleep(1)
    # autoit.mouse_click("left", 636, 596)
    # break
    # if not daily:
    # break

    while True:
        missions = pyautogui.locateCenterOnScreen('./content/missions.png')
        if missions:
            pyautogui.click(637, 598)
            time.sleep(1)
            break
        if not missions:
            break

    while True:
        if pyautogui.locateOnScreen('./content/againp.png'):
            pyautogui.click(pyautogui.locateOnScreen('./content/againp.png'))
            break

    pyautogui.moveTo(0, 0)
