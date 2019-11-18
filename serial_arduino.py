

import matplotlib.pyplot as plt
import serial  # importacao do modulo serial
import json

leitura = [1,2,3,4,5,6,7,8,7,6,5,4,]
fig, ax = plt.subplots()
ser = serial.Serial('/dev/ttyUSB0', 9600)  # abre porta serial COM6

contador = 0
eixo_x = 50

while True:
  while (ser.inWaiting() == 0):
    pass

  dados = int(float(ser.readline()))  # firmware deve ter um delay de pelo menos 100ms entre cada envio
  print dados
  ax.clear()
  ax.set_xlim([0, eixo_x])  # faixa do eixo horizontal
  ax.set_ylim([0, 50])  # faixa do eixo vertical

  leitura.append(dados)

  try:
    with open('dados.json', 'w') as fp:
      json.dump(leitura, fp)
  except:
    print("Ocorreu um erro na hora de montar o arquivo JSON.")

  ax.plot(leitura)
  plt.pause(.000001)
  contador = contador + 1

  if (contador > eixo_x):
    leitura.pop(0)

ser.close()