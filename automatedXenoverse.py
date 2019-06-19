import win32com.client
import win32gui
import win32process
import time
hwnd = win32gui.GetForegroundWindow()
print(hwnd)

pid = 18592

shell = win32com.client.Dispatch("WScript.Shell")
shell.AppActivate(pid)
shell.AppActivate('Console2')

import ctypes
import time

SendInput = ctypes.windll.user32.SendInput

W = 0x11
A = 0x1E
S = 0x1F
D = 0x20
up = 0xC8
left = 0xCB
right = 0xCD
down = 0xD0
enter = 0x1C
X = 0x2D
esc = 0x01

# C struct redefinitions
PUL = ctypes.POINTER(ctypes.c_ulong)
class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time" ,ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                ("mi", MouseInput),
                ("hi", HardwareInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

# Actuals Functions

def PressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def ReleaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def command(comm ,tim):
    if(comm == 0xC8):
        print('up')
    if (comm == 0xCB):
        print('left')
    if (comm == 0xCD):
        print('right')
    if (comm == 0xD0):
        print('down')
    if (comm == 0x1C):
        print('enter')
    if (comm == 0x2D):
        print('x')
    PressKey(comm)
    time.sleep(tim)
    ReleaseKey(comm)
    time.sleep(0.1)

if __name__ == '__main__':




    timer = 0.2
    enter_timer = 1
    enter_timer2 = 0.5
    def vi():
        def start():
            time.sleep(5)
            for y in range(30):
                print(y)
                command(enter, enter_timer2)

            command(right ,timer)
            command(right, timer)
            command(up, timer)
            command(enter, timer)
            command(left, timer)
            command(left, timer)
            command(enter, timer)
            command(right, timer)
            command(right, timer)
            command(right, timer)
            command(enter, timer)
            command(left, timer)
            command(left, timer)
            command(down, timer)
            command(enter, timer)
            command(right, timer)
            command(down, timer)
            command(enter, timer)
            command(up, timer)
            command(left, timer)
            command(left, timer)
            command(enter, timer)
            command(left, timer)
            command(X, timer)
            for y in range(25):
                print(y)
                command(enter, enter_timer)
            command(left, enter_timer2)
            command(enter, enter_timer2)
            command(left, enter_timer2)
            command(enter, enter_timer2)

        def secondRound():
            time.sleep(5)
            for y in range(15):
                print(y)
                command(enter, enter_timer2)
            command(right, timer)
            command(right, timer)
            command(right, timer)
            command(enter, timer)
            command(left, timer)
            command(enter, timer)
            command(X ,timer)
            command(enter, timer)
            command(X, timer)
            command(enter, timer)
            for y in range(25):
                print(y)
                command(enter, enter_timer)
            command(left, timer)
            command(enter, enter_timer2)
            command(left, enter_timer2)
            command(enter, enter_timer2)
            for y in range(15):
                print(y)
                command(enter, enter_timer2)
        while(True):
            start()
            secondRound()
    def beerus():
        def start():
            time.sleep(5)
            for y in range(30):
                print("FR ini",y)
                command(enter, enter_timer2)

            command(right ,timer)
            command(right, timer)
            command(up, timer)
            command(enter, timer)
            command(left, timer)
            command(left, timer)
            command(enter, timer)
            command(right, timer)
            command(right, timer)
            command(right, timer)
            command(enter, timer)
            command(left, timer)
            command(left, timer)
            command(left, timer)
            command(left, timer)
            command(down, timer)
            command(enter, timer)
            command(right, timer)
            command(right, timer)
            command(right, timer)
            command(down, timer)
            command(enter, timer)
            command(up, timer)
            command(left, timer)
            command(left, timer)
            command(enter, timer)
            command(right, timer)
            command(X, timer)
            for y in range(30):
                print("FR end",y)
                command(enter, enter_timer)
            command(left, enter_timer2)
            command(enter, enter_timer2)
            command(left, enter_timer2)
            command(enter, enter_timer2)

        def secondRound():
            time.sleep(5)
            for y in range(15):
                print("SR ini",y)
                command(enter, enter_timer2)
            command(right, timer)
            command(enter, timer)
            command(left, timer)
            command(left, timer)
            command(left, timer)
            command(up, timer)
            command(enter, timer)
            command(right, timer)
            command(right, timer)
            command(X ,timer)
            command(enter, timer)
            command(X, timer)
            command(enter, timer)
            for y in range(30):
                print("SR Waiting",y)
                command(enter, enter_timer)
            command(left, timer)



            command(enter, enter_timer2)
            command(left, enter_timer2)
            command(enter, enter_timer2)
            for y in range(15):
                print("SR Win",y)
                command(enter, enter_timer2)
            command(esc, enter_timer2)
            command(enter, enter_timer2)
            command(left, enter_timer2)
            command(enter, enter_timer2)



        while(True):
            start()
            secondRound()


    #vi()

    beerus()





