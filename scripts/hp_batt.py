import os
import subprocess
from time import sleep


PATH = "/home/sergio/.local/"
OUTPUT_NAME = "output.txt"
def main():
    batery_level = 100;
    with open(OUTPUT_NAME, "w+") as output:
        subprocess.run([PATH + "headsetcontrol", "-b"], stdout=output);
    
    with open(OUTPUT_NAME, "r") as output:
        for line in output.readlines():
            if "%" in line:
                batery_level = line.removeprefix("Battery: ")
                batery_level = batery_level.replace("%", "")

    print(batery_level, end="")

    if int(batery_level) < 20:
        os.system("beep -f 800 -l 100")
        os.system("beep -f 800 -l 100")

if __name__ == "__main__":
    main()