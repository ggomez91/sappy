import pyautogui
import os
import signal
import subprocess
import time
import hydra
from win10toast import ToastNotifier
import argparse


toaster = ToastNotifier()


def login(user, password):
    print("Opening SAP...")
    proc = subprocess.Popen(["C:\Program Files (x86)\SAP\FrontEnd\SAPgui\saplogon.exe"])
    time.sleep(5)

    print("Selecting Server...")
    pyautogui.press(["home", "down", "enter"])
    time.sleep(3.5)

    print("Login...")
    pyautogui.typewrite(user)
    pyautogui.press(["tab"])
    pyautogui.typewrite(password)
    pyautogui.press(["enter"])
    time.sleep(1.5)


def tcode(tcode):
    print("Entering T-code [" + tcode + "]...")
    pyautogui.typewrite(tcode)
    pyautogui.press(["enter"])
    time.sleep(1.5)


def zhrsup():
    tcode("ZHRSUP")


def cat2():
    tcode("CAT2")

    print("Setting profile...")
    pyautogui.keyDown("shift")
    pyautogui.press(["tab"])
    pyautogui.keyUp("shift")
    pyautogui.typewrite("HEMP")
    pyautogui.press(["tab"])
    pyautogui.typewrite("2233174")
    pyautogui.press(["enter"])
    time.sleep(1)

    print("Entering timesheet...")
    pyautogui.press(["f5"])


@hydra.main(config_path="config.yaml", strict=False)
def my_app(cfg):
    print(cfg.pretty())

    user = cfg.sap.user
    password = cfg.sap.password
    tcode = cfg.sap.tcode

    if tcode != None and tcode not in ["ZHRSUP", "CAT2"]:
        raise Exception("Unsupported Tcode: " + tcode)

    login(user, password)
    if tcode == "ZHRSUP":
        zhrsup()
    if tcode == "CAT2":
        cat2()

    toaster.show_toast("Sappy", "Sappy automation complete!")


if __name__ == "__main__":
    my_app()
