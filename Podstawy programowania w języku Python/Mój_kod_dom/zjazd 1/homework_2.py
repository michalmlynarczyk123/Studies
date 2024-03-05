tb = 1_000_000
sek = 194
min = sek * 12
hour = min * 60

print("Jeżeli w 5 sek pobrano 194 MB, to w minutę pobrano: " + str(min) + " MB. W godzinie pobrano: " + str(hour) +
      " MB. W takim razie 13TB danych pobrano w: " + str(round((tb * 13)/ hour)) + " godziny.")


