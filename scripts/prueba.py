from psutil import cpu_freq
from time import sleep
from libqtile.command.client import InteractiveCommandClient
import random
from threading import Thread

done = True


charsitos = ["ऄ","अ","आ","इ","ई", "उ","ऊ","ऋ","ऌ","ऍ","ऎ", "ए", "ऐ", "ऑ", "ऒ", "ओ","औ","क","ख","ग","घ","ङ", "च", "छ", "ज", "झ","ञ","ट","ठ","ड","ढ","ण", "त", "थ", "द", "ध","न","ऩ","प","फ","ब","भ", "म", "य", "र", "ऱ","ल","ळ","ऴ","व","श", "ष", "स", "ह", "ა","ბ","გ","დ","ე","ვ","ზ","თ","ი","კ","ლ","მ","ნ","ო","პ","ჟ","რ","ს","ტ","უ","ფ","ქ","ღ","ყ","შ","ჩ","ც","ძ","წ","ჭ","ხ","ჯ","ჰ","ჱ","ჲ","ჳ","ჴ","ჵ","ჶ","ჷ","ჸ","ჹ","ჺ","჻", "Ⴀ","Ⴁ","Ⴂ","Ⴃ","Ⴄ","Ⴅ","Ⴆ","Ⴇ","Ⴈ","Ⴉ","Ⴊ","Ⴋ","Ⴌ","Ⴍ","Ⴎ","Ⴏ","Ⴐ","Ⴑ","Ⴒ","Ⴓ","Ⴔ","Ⴕ","Ⴖ","Ⴗ","Ⴘ","Ⴙ","Ⴚ","Ⴛ","Ⴜ","Ⴝ","Ⴞ","Ⴟ","Ⴠ","Ⴡ","Ⴢ","Ⴣ","Ⴤ","Ⴥ",]
def hack():
    a = []
    for _ in range(0, 30):
        a.append(random.choice(charsitos))
    return "".join(a)


def main():
    global done
    c = InteractiveCommandClient()

    cpu = c.widget["cpu"]
    textbox = c.widget["textbox"]

    def update_freq():
        global done
        while(done):
            try:
                text = f"  i7-4771 {cpu_freq().current:0.2f}Ghz  "
                cpu.update(text)
                sleep(2)
            except:
                done = False

    def update_text():
        global done
        while(done):
            try:
                text = hack()
                textbox.update(text)
                sleep(0.2)
            except:
                done = False


    t1 = Thread(target=update_freq, args=())
    t2 = Thread(target=update_text, args=())

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    sleep(2)
    print("Error, trying again...")
    done = True
    main()

main()