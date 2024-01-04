import googletrans
from googletrans import Translator

#print (googletrans.LANGUAGES)


text1 = "This is my first channel"

text2 = "Detta är min första kanal"

text3 = "Das sind in deutsche"

transobjekt = Translator()

print (transobjekt.detect(text1))
print (transobjekt.detect(text2))
print (transobjekt.detect(text3))



print ("Översatt från svenska till engelska: ", transobjekt.translate(text2))

