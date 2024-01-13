"""Implementieren Sie zwei Funktionen scale_up und scale_down. Beide Funktionen nehmen einen Integer factor und
einen String image als Parameter an. image repräsentiert ein 2-dimensionales Bild bestehend aus ASCII-Symbolen.
Die Funktion scale_up soll das Bild um den angegebenen Faktor vergrössern, und scale_down soll das Bild um den
angegebenen Faktor verkleinern. Um ein Bild um einen Faktor n zu vergrössern wiederholt man einfach die einzelnen
Zeichen und Zeilen n mal. Um ein Bild um einen Faktor n zu verkleiner, behält man nur diejenigen Zeichen und Zeilen,
deren Indices durch n teilbar sind. Beachten Sie die Assertions als Beispiele für die Anwendung von scale_up und
scale_down. Korrekt implementiert, gibt jede der zwei Funktionen jeweils die Hälfte der vollen Punktzahl."""


def scale_up(factor, image):
    lyst = image.split("\n")
    res = []
    for i in lyst:
        line = factor*i
        for i in range(factor):
            res.append(line)
    return "\n".join(res)

def scale_down(factor, image):
    lyst = image.split("\n")
    res = []
    for i in lyst:
        if i%factor == 0:
            for j in i:
                if j%factor ==0:
                    res.append(j)
    print(res)
    return "\n".join(res)

# DO NOT SUBMIT THE LINES BELOW!
img1 = ("xxx\n"
        "x x\n"
        "xxx")
res =scale_up(2, img1)
print(res)

img2 = ("xxxxxx\n"
        "xxxxxx\n"
        "xx  xx\n"
        "xx  xx\n"
        "xxxxxx\n"
        "xxxxxx")

#assert scale_up(2, img1) == img2
#assert scale_down(2, img2) == img1
#
#img3 = ("123\n"
#        "345")
#
#img4 = ("111222333\n"
#        "111222333\n"
#        "111222333\n"
#        "333444555\n"
#        "333444555\n"
#        "333444555")
#
#assert scale_up(3, img3) == img4
#assert scale_down(3, img4) == img3
#
#img5 = ("12345\n"
#        "abcde\n"
#        "ABCDE")
#
#img6 = ("14")
#
#assert scale_down(3, img5) == img6