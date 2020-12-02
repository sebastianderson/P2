import numpy as np
import os
import subprocess
#In this first exercise you can parse the BBB.avi file and can seee the video
#and audio file codec and the resolutions of the video.
#command
cmd = [ 'ffprobe', '-v', 'error', '-select_streams', 'v:0', '-show_entries', 'stream=codec_name', '-of', 'csv=s=x:p=0', 'BBB.avi' ]
#save output
Video_codec = subprocess.Popen( cmd, stdout=subprocess.PIPE ).communicate()[0]
cmd = [ 'ffprobe', '-v', 'error', '-select_streams', 'a:0', '-show_entries', 'stream=codec_name', '-of', 'csv=s=x:p=0', 'BBB.avi' ]
Audio_codec = subprocess.Popen( cmd, stdout=subprocess.PIPE ).communicate()[0]
cmd = [ 'ffprobe', '-v', 'error', '-select_streams', 'v:0', '-show_entries', 'stream=width,height', '-of', 'csv=s=x:p=0', 'BBB.avi' ]
WidthxHeight = subprocess.Popen( cmd, stdout=subprocess.PIPE ).communicate()[0]
#print output
print("Video Code: {}".format(Audio_codec))
print("Audio Code: {}".format(Audio_codec))
print("Width x Height: {}".format(WidthxHeight))
