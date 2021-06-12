import os 
import webbrowser 
import random

while True:
  webbrowser.open('https://memegenerator.net/img/images/72968769/wojak-troll.jpg')
  ran = random.randint(10,55)
  os.system(f"mkdir {ran}")
  def gerar():
    argm = []
    for w in range(48,123):
           for y in range(48, 123):
                for i in range(48, 123):
                    argm.append(chr(w)+chr(y)+chr(i))
    return argm


  letras = gerar()
  print(letras)