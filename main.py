#   __      ___     _
#   \ \    / (_)   | |
#    \ \  / / _  __| | ___  ___
#     \ \/ / | |/ _` |/ _ \/ _ \
#      \  /  | | (_| |  __/ (_) |
#    ___\/   |_|\__,_|\___|\___/_                 _
#   |  __ \                    | |               | |
#   | |  | | _____      ___ __ | | ___   __ _  __| | ___ _ __
#   | |  | |/ _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` |/ _ \ '__|
#   | |__| | (_) \ V  V /| | | | | (_) | (_| | (_| |  __/ |
#   |_____/ \___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_|\___|_|
#
#                                             By @errorin_out
#
#   Created on  |   Discord:   |   GitHub:
#   Sep 16 2023 | @errorin_out | AFK-debug-9

import random
import requests
import time
import sys
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def download(url, file):
    response = requests.get(url, verify=False, stream=True)
    totalbytes = 0
    len_to_del = len(f" Downloading... {0:.2f} MB saved as {file!r}")
    print(f" Downloading... {0:.2f} MB saved as {file!r}", end="")
    
    if response.status_code != 200:
        return -1
    
    with open(file, 'wb') as f:
        for chunk in response.iter_content(chunk_size=(1024 * 128)):
            if not chunk:
                break
            totalbytes += len(chunk)
            sys.stdout.write('\b' * len_to_del)
            sys.stdout.flush()
            print(f" Downloading... {totalbytes/1024/1024:.2f} MB saved as {file!r}", end="")
            f.write(chunk)
    
    print("\n Saved File!")
    return 0


def getVideo(video, format):
    if format not in ("mp3", "mp4"):
        print(" Not Allowed!")
        return -1

    url = f"https://nu.ummn.nu/api/v1/init?p=y&_={random.random()}"
    url = requests.get(url)
    url = url.json()["convertURL"] 
    url += f"&v={video}&f={format}&_={random.random()}"
    count = 1
    while True:
        url = requests.get(url, verify=False).json()
        if url["redirect"] == 0:
            print(" Getting Data...")
            downloadURL = url["downloadURL"]
            while True:
                info = requests.get(url["progressURL"], verify=False).json()
                if info["progress"] == 3:
                    print(" Got Data")
                    break
                time.sleep(1)
            print(" Starting Download...")
            return download(downloadURL, f'{info["title"]}.{format}')
        time.sleep(3)
        url = url["redirectURL"]
        print(f" Got Stage {(count:=count+1)} URL")

def main():
    return_value = \
        getVideo(
            input(
                " \\ \\    / (_)   | |                                        \n"
                "  \\ \\  / / _  __| | ___  ___                               \n"
                "   \\ \\/ / | |/ _` |/ _ \\/ _ \\                              \n"
                "    \\  /  | | (_| |  __/ (_) |                             \n"
                "  ___\\/   |_|\\__,_|\\___|\\___/_                 _           \n"
                " |  __ \\                    | |               | |          \n"
                " | |  | | _____      ___ __ | | ___   __ _  __| | ___ _ __ \n"
                " | |  | |/ _ \\ \\ /\\ / / '_ \\| |/ _ \\ / _` |/ _` |/ _ \\ '__|\n"
                " | |__| | (_) \\ V  V /| | | | | (_) | (_| | (_| |  __/ |   \n"
                " |_____/ \\___/ \\_/\\_/ |_| |_|_|\\___/ \\__,_|\\__,_|\\___|_|   \n"
                "                                                           \n"
                "                                           By @errorin_out \n"
                " Type the video url (with schema): "
            ),        
            input(
                " Type the format (mp3/mp4): "
            )
        )

    exit(return_value)

if __name__ == '__main__':
    main()