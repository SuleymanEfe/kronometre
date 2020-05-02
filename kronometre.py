import time


saat = 0
dakika = 0
saniye = 0


while True:
    time.sleep(1)
    saniye += 1
    if dakika == 60:
        saat += 1
        dakika = 0
    elif saniye == 60:
        dakika += 1
        saniye = 0
    if saat > 0:
        print('\r',saat, "saat", dakika, "dakika", saniye, "saniye gecti..", end="")
    elif dakika > 0:
        print('\r',dakika, "dakika" ,saniye, "saniye gecti.." , end="")
    else:
        print('\r' ,saniye, "saniye gecti..", end = ".")


