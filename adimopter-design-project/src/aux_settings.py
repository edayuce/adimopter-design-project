#!/usr/bin/env python

from h2rMultiWii import MultiWii
from command_values import disarm_cmd
import time

board = MultiWii("/dev/ttyUSB0")

def toggle_angle_mode(toggle_value = 1000):
    board.sendCMD(16, MultiWii.SET_RAW_RC, disarm_cmd + [toggle_value, 1500, 1500, 1500])
    time.sleep(2)
    print(board.receiveDataPacket())
    print("DONE!")

def enable_angle_mode():
    toggle_angle_mode(1900)

def disable_angle_mode():
    toggle_angle_mode(1000)

def main():
    board = MultiWii("/dev/ttyUSB0")
    print("Aux spamliyorruz babbba")
    time.sleep(1)
    #board.sendCMD(0, MultiWii.BOXIDS, [])
    for i in range(10):
        board.sendCMD(16, MultiWii.SET_RAW_RC, [1500 for i in range(8)])
        time.sleep(2)
    #board.sendCMD(0, MultiWii.BOX, [])
    #time.sleep(1)
        print(board.receiveDataPacket())
        print(board.box)
        print(board.boxids)
        board.sendCMD(16, MultiWii.SET_RAW_RC, [1500, 1500, 1000, 1000, 2060, 1500, 1500, 1500])
        print(board.receiveDataPacket())
        time.sleep(2)
    #board.sendCMD(16, MultiWii.SET_RAW_RC, [1500, 1500, 2000, 1000, 1500, 1500, 1500, 1500])
    #time.sleep(1)
    #board.sendCMD(16, MultiWii.SET_RAW_RC, [1500, 1500, 2000, 1000, 1500, 1500, 1500, 1500])
    #time.sleep(2)
    #board.sendCMD(16, MultiWii.SET_RAW_RC, [1500, 1500, 1000, 1000, 1500, 1500, 1500, 1500])
    print("Done!")
    
if __name__ == "__main__":
    #main()
    #toggle_angle_mode(1850)
    #exit(0)
    user_input = input("1 = Enable Angle Mode, 2 = Disable Angle Mode: ")
    user_input = str(user_input)
    if user_input == "1":
        enable_angle_mode()
    elif user_input == "2":
        disable_angle_mode()
    else:
        toggle_angle_mode(int(user_input))
    board.close()
