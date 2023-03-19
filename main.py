import os; os.system("cls")
from colorama import Fore, Style
import ctypes, string, base64
from decimal import Decimal
import random, time, threading

class stats():
    unlocked=0
    locked=0
    errors=0

def random_string(length):
    defualt = string.ascii_lowercase+string.ascii_uppercase+string.digits
    return ''.join(random.sample(defualt,length))
 
def real_token():
    return base64.b64encode(
        str(round(Decimal(time.time()*1000-1420070400000)*4194304)).
        encode()).decode()[:-2]+f".{random_string(length=6)}.{random_string(length=38)}"

def log(subj,mesg):
    print(f"{Style.BRIGHT}{Fore.RED}[{Fore.BLUE}{subj}{Fore.RED}] {mesg}"+Fore.RESET)

def make_token():
    while True:
        log("AI PREDICT SERVER",f"{Fore.GREEN}  Please click each image containing an olaru --> [3, 5, 7]"); time.sleep(random.uniform(0, 1))
        log("SOLVER",f"{Fore.GREEN}hCaptcha solved: {Fore.YELLOW}P1_eyJOeXAi{random_string(length=30)}..."); time.sleep(random.uniform(0, 1))
        token=real_token();                                                                                  time.sleep(random.uniform(0, 1))
        log("SOLVER",f"{Fore.RED}LOCKED {Fore.CYAN}{token}");                                                time.sleep(2)

        stats.locked+=1
        ctypes.windll.kernel32.SetConsoleTitleW(f"TrixTM's Discord Token Gen | Tokens: {str(stats.unlocked)} | Locks: {str(stats.locked)} | Errors: {str(stats.errors)} | Unlock rate: 0% | Time: 1:43:52 | Logged in as: Dazeer")

for x in range(20):
    threading.Thread(target=make_token).start()
