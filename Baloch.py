#coding=utf-8

import os, sys, platform

os.system('xdg-open https://chat.whatsapp.com/Juq2WOIp9sHK652BnFx6s3')

try:

    if sys.argv[1]=='update':

        os.system('rm -rf ZEESHAN64.cpython-311.so ZEESHAN32.cpython-311.so')

except:

    pass

os.system('rm -rf ZEESHAN64.cpython-311.so ZEESHAN32.cpython-311.so')

os.system('git pull')

bit = platform.architecture()[0]

if bit == '64bit':

    if not os.path.isfile('KRS64.cpython-311.so'):

        os.system('curl https://raw.githubusercontent.com/TEAM-ZEESHAN/DATA/main/ZEESHAN64.cpython-311.so > ZEESHAN64.cpython-311.so') 

        os.system("chmod 777 ZEESHAN64*")

        import KRS64

    else:

        import KRS64

elif bit == '32bit':

    if not os.path.isfile('KRS32.cpython-311.so'):

        os.system('curl https://raw.githubusercontent.com/TEAM-ZEESHAN/DATA/main/ZEESHAN32.cpython-311.so > ZEESHAN32.cpython-311.so')

        os.system("chmod 777 ZEESHAN32*")

        import KRS32

    else:

        import KRS32

