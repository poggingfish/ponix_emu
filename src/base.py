from plisphelper import pexec, p_reset
import ponixfs
ponixfs.write("Booting ponix.\n")
while True:
    ponixfs.write("-> ")
    x = input()
    ponixfs.write(x+"\n")