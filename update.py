import requests
import json 
import os
import time
while True:
    url = "https://api.github.com/repos/darverdevs/PluginInstallerRepo/git/trees/main"
    r = requests.get(url).json()
    files = r['tree']
    i = 1
    a = ''
    with open('names.txt', 'w') as f:
        f.write('')
        f.close()
    with open('names.txt', "a") as f:
        for file in files:
            if file['type'] == 'blob':
                split = file['path'].split('.')
                num = i%2
                if num == 0:
                    if split[1] == "jar":
                        form = str(i) + ". " + split[0]
                        lasta = a
                        newa = a +form + "\t"
                        a = newa
                        f.write(a + "\n")
                        a = ''
                        i+=1
                    else:
                        continue
                else:
                    if split[1] == "jar":
                        form = str(i) + ". " + split[0]
                        lasta = a
                        newa = a +form + "\t"
                        a = newa
                        i+=1
    print("Updated at", time.time())
    time.sleep(1600)