import os
from time import sleep

os.system ('clear')

m ='\033[31m'
h ='\033[32m'
k ='\033[33m'
b ='\033[34m'
u ='\033[35m'
c ='\033[36m'
p ='\033[37m'

bn = """
    \033[37;1m) ) ) )     \033[31;1m _____ ___  __  __ ____   ___  _
    \033[32;1m███████ ═╮  \033[31;1m|_   _/ _ \|  \/  | __ ) / _ \| |
    \033[32;1m███████ ▏ ∥   \033[31;1m| || | | | |\/| |  _ \| | | | |
    \033[32;1m███████ ═╯    \033[37;1m| || |_| | |  | | |_) | |_| | |___
    \033[32;1m◥█████◤       \033[37;1m|_| \___/|_|  |_|____/ \___/|_____|
                   \033[32;1m[ \033[33;1mKEY TERMUX BY SETA GANZ \033[32;1m]
   \033[32;1m───────────────────────────────────────────────────\n"""

def menu():
    print (bn)
    print ("  \033[32;1m[\033[33;1m!\033[32;1m] \033[37;1mPROSES!!")
    sleep(3)
    print ("  \033[32;1m[\033[33;1m!\033[32;1m] \033[37;1mMENGAMBIL FILE TERMUX...")
    sleep(3)
    try:
        os.mkdir('/data/data/com.termux/files/home/.termux')
    except:
       pass
    print ("  \033[32;1m[\033[33;1m!\033[32;1m] \033[37;1mBERHASIL")
    sleep(3)
    print ("  \033[32;1m[\033[33;1m!\033[32;1m] \033[37;1mSABAR YA PENAMBAHAN TOMBOLNYA")
    sleep(2)
    key = "extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]"
    kontol = open('/data/data/com.termux/files/home/.termux/termux.properties','w')
    kontol.write(key)
    kontol.close()
    sleep(2)
    print ("  \033[32;1m[\033[33;1m!\033[32;1m] \033[37;1mPROSES!!")
    sleep(5)
    print ("  \033[32;1m[\033[33;1m!\033[32;1m] \033[37;1mBENTAR LAGI KOK HARAP SABAR ^^")
    os.system('termux-reload-settings')
    print ("")
    print ("  \033[32;1m[\033[33;1m•\033[32;1m] \033[37;1mPROSES SELESAI JIKA GAGAL HARAP HUBUNGI AUTHOR ^^")
    print ("  \033[32;1m[\033[33;1m•\033[32;1m] \033[34;1mFACEBOOK \033[33;1m> \033[37;1mfb.com/seto.sanwa3")
    print ("  \033[32;1m[\033[33;1m•\033[32;1m] \033[35;1mINSTAGRAM \033[33;1m> \033[37;1m@szyax_")

menu()
