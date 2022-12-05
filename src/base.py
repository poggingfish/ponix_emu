from plisphelper import pexec, p_reset
import ponixfs
ponixfs.write("Booting ponix.\n")
x = 0 
while True:
    ponixfs.write(f"{x}" +"\n")
    x+=1