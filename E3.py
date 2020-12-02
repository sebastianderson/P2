import numpy as np
import os
import subprocess

def resize(filename,size,output):
    #function to resize any file to the size you asked.
    if size == 720:
        #command
        cmd = [ 'ffmpeg', '-i', filename, '-s', 'hd720', '-c:v', 'libx264', '-crf', '23', '-c:a', 'aac', '-strict', '-2', output ]
        #to convert a list to string we use join
        separator=' '
        com=separator.join(cmd)
        #use the command
        os.system(com)
    elif size == 480:
        cmd = [ 'ffmpeg', '-i', filename, '-s', 'hd480', '-c:v', 'libx264', '-crf', '23', '-c:a', 'aac', '-strict', '-2', output ]
        separator=' '
        com=separator.join(cmd)
        os.system(com)
    elif size == 320:
        cmd = [ 'ffmpeg', '-i', filename, '-vf', ' scale=320:240,setsar=1:1', output ]
        separator=' '
        com=separator.join(cmd)
        os.system(com)
    elif size == 160:
        cmd = [ 'ffmpeg', '-i', filename, '-vf', ' scale=160:120,setsar=1:1', output ]
        separator=' '
        com=separator.join(cmd)
        os.system(com)
    else:
        print("unvalid")
#this below is to test the function I commented to use this file in the  5th exercise
#resize('BBB_OG.avi',160,'prueba.avi')
