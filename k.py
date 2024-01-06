# ig: @plutofrmdak
import os, httpx, time, threading, random, string

# file open
__0O0O0O0OOO0OOOOO = open("proxies.txt", "r")
_00OO0O0O0O0OOO__ = open('codes.txt', 'a')
prox = set() # Store proxies here from "proxies.txt"

# User Interface Menu
os.system('cls' if os.name == 'nt' else 'clear')
print("♣: @plutofrmdak")
try:
    iO = input("Proxies? [y/n]: ")
    if iO == "y" or iO == "Y":
        for xY0 in __0O0O0O0OOO0OOOOO.readlines():
            prox.add(xY0.strip())
    else: prox = "127.0.0.1"
    zX = int(input('Amount: '));print()
except: input("\n[!] Restart the program, and enter a number for amount.");os._exit(0)


def _0O0O0OOO0(length): return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
def _0O0O0O0OOOO00():
    ___0O0O0O0O0O0 = httpx.post(
        'https://api.discord.gx.games/v1/direct-fulfillment', 
        headers={
            'Authority': 'api.discord.gx.games',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Content-Type': 'application/json',
            'Origin': 'https://www.opera.com',
            'Referer': 'https://www.opera.com/',
            'Sec-Ch-Ua': '"Opera GX";v="105", "Chromium";v="119", "Not?A_Brand";v="24"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Platform': '"Windows"',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'cross-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 OPR/105.0.0.0'
        }, 
        json={'partnerUserId': _0O0O0OOO0(64)},
        proxies={'http://': 'https://' +random.choice(list(prox))}
    )

    if ___0O0O0O0O0O0.status_code in [200, 201, 204]:
        _00OO0O0O0O0OOO__.write("https://discord.com/billing/partner-promotions/1180231712274387115/{}\n".format(___0O0O0O0O0O0.json()['token']))
        print("\33[32m[!] \33[37mSuccess: https://discord.com/billing/partner-promotions/1180231712274387115/{}...".format(___0O0O0O0O0O0.json()['token'][:25]))

    elif ___0O0O0O0O0O0.status_code == 429:
        print("\33[31m[!] \33[37mRate limit: {} seconds".format(___0O0O0O0O0O0.json()['retry_after']))
        time.sleep(___0O0O0O0O0O0.json()['retry_after'])

    else:
        print("\33[31m[!] \33[37mError: Status code {}".format(___0O0O0O0O0O0.status_code))

if __name__ == "__main__":
    threads = []
    
    for x in range(zX):
        zC = threading.Thread(target=_0O0O0O0OOOO00)
        zC.start()
        threads.append(zC)
        
    for yA in threads:
        yA.join()

    input("\n[!] All codes generated have been saved in \"codes.txt\", press enter to exit");os._exit(0)
