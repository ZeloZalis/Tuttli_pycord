import wikipedia
import re

wikipedia.set_lang("es")
search = "manzana"

parrafo_1 = wikipedia.summary(search, sentences=3)
parrafo_limpio = re.sub(r'\[\d+\]|\[\d+\]\[.*?\]|\[http.*?\]', '', parrafo_1)

print(parrafo_limpio)