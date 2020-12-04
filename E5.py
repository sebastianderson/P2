import numpy as np
import os
import subprocess
import E3
import E4

# file to interact with the previous exercises
filename = "BBB_OG.avi"
output1 = "BBBnew.avi"
output2 = "BBBnew.mp4"
print("To resize BBB video enter: 1, To change the codec to h264 enter 2")
i = input()
if i == "1":
    print("In what size do you want to resize you video?720/480/320/160")
    # save the input in the terminal
    i2 = input()
    if i2 == "720" or i2 == "480" or i2 == "320" or i2 == "160":
        E3.resize(filename, int(i2), output1)
        print("The file has been saved in :{} ".format(output1))
elif i == "2":
    E4.transcodeh264(filename, output2)
    print("The file has been saved in :{} ".format(output2))
else:
    print("unvalid")
