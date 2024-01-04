import googletrans
from googletrans import Translator

#print (googletrans.LANGUAGES)


text1 = "The flying horse is fast"

text2 = "Detta är min första kanal"

text3 = "Das sind in deutsche"

transobjekt = Translator()

print (transobjekt.detect(text1))
print (transobjekt.detect(text2))
print (transobjekt.detect(text3))


text4 = transobjekt.translate(text1, src='en', dest='sv')
text5 = transobjekt.translate(text2, src='sv', dest='fr')

print ("text på svenska: ", text4.text)
print ("text på franska: ", text5.text)










