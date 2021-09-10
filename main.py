import subprocess, requests, time, os

guyshwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
r = requests.get('url here')

try:
    if guyshwid in r.text:
        pass
    else:
        print('[ERROR] HWID Not in database')
        print(f'HWID: {guyshwid}') 
        time.sleep(5)
        os._exit()
except:
    print('[ERROR] Failed to connect to database')
    time.sleep(5) 
    os._exit() 
    
os.system('title HWID Authentication')

print('Welcome')
input()

#developed by j3nx

#developed by j3nx

#developed by j3nx

#developed by j3nx

#developed by j3nx

#developed by j3nx

#developed by j3nx

#developed by j3nx

#developed by j3nx

#developed by j3nx

#developed by j3nx

#developed by j3nx

