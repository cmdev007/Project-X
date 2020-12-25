import os
a=os.popen("konsole -e cryfs basedir mountdir").read()
print (a)
