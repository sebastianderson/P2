import numpy as np
import os
import subprocess


def transcodeh264(filename, output):
    # function to transcode any video to h264
    # command
    cmd = ["ffmpeg", "-i", filename, "-vcodec", "h264", output]
    # join list into string
    separator = " "
    com = separator.join(cmd)
    os.system(com)


# this below is to test the function I commented to use this file in the  5th exercise
# transcodeh264('BBB_OG.avi','prueba2.mp4')
