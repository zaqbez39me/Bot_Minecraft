import random
import time
import os
import win32com.client as comclt
wsh = comclt.Dispatch("WScript.Shell")


def follow(thefile):
    thefile.seek(0, os.SEEK_END)
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line


def log(text: str, name_file: str):
    with open(name_file, 'a') as file:
            file.write(text)


if __name__ == '__main__':
    logfile = open("C:/Users/korol_20el/AppData/Roaming/Kaboom/modpacks/1.7.10/modpacks/skyfactory/logs/latest.log", "r")
    loglines = follow(logfile)
    for line in loglines:
        print(line, end='')
        if "Решите пример: " in line:
            u = line[line.index("Решите пример: ") + len("Решите пример: "):]
            u = u[:len(u) - 1]
            time.sleep(2.8 + random.randint(1, 10) / 10)
            wsh.AppActivate("Minecraft 1.7.10")
            wsh.SendKeys("T")
            time.sleep(0.05)
            wsh.SendKeys(int(eval(u)))
            wsh.SendKeys("{ENTER}", 0)
