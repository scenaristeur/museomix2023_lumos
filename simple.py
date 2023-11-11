import io,sys,os,subprocess
from tkFileDialog import askopenfilename
global process
name= askopenfilename(filetypes=[("Video Files","*.h264")])
subprocess.call(['vlc',name,'--play-and-exit'])