"""Implementieren Sie eine Funktion currency_converter die drei Parameter annimmt: zwei Strings src und dst,
 welche die Namen der Ausgangs- und Zielwährungen repräsentieren, sowie eine Zahl rate, welche den Umrechnungskurs
 darstellt. Die Funktion currency_converter soll eine Funktion zurückgeben, welche den gewünschten Geldbetrag in der
  Ausgangswährung als einzigen Parameter annimmt, und einen String zurückgibt in der Form X SRC is Y DST. Der
  berechnete Umrechnungswert soll auf 2 Nachkommastellen gerundet werden. Beachten Sie die Assertions als Beispiele für
  die Anwendung von currency_converter."""


def currency_converter(src, dst, rate):
    def res_func(x):
        res = str(x) + " " + src + " is " + str(round(x*rate, 2)) + " " + dst
        return res
    return res_func

# DO NOT SUBMIT THE LINES BELOW!
assert currency_converter("EUR", "CHF", 1.1)(5) == "5 EUR is 5.5 CHF"
chf_to_jpy = currency_converter("CHF", "JPY", 123)
assert chf_to_jpy(1) == "1 CHF is 123 JPY"
assert chf_to_jpy(2) == "2 CHF is 246 JPY"
assert currency_converter("Peanuts", "Pinecones", 0.2)(50) == "50 Peanuts is 10.0 Pinecones"
assert currency_converter("Blemflarcks", "Coins", 0.0021)(333.3) == "333.3 Blemflarcks is 0.7 Coins"
x = currency_converter("EUR", "CHF", 1.1)(5)
print(x)
