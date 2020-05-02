import time


saat = 0
dakika = 0
saniye = 0


while True:
    time.sleep(0.1)
    saniye += 1
    if dakika == 60:
        saat += 1
        dakika = 0
    elif saniye == 60:
        dakika += 1
        saniye = 0

    print(saat, "saat", dakika, "dakika", saniye, "saniye gecti..")
