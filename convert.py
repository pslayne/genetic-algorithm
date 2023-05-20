#conversão binário - decimal
def dec_to_bin(dec): 
  bin = ''

  while(dec > 1):
    bin = bin + str(dec % 2)
    dec = dec // 2

  bin = bin + '1'

  return bin[::-1]

#conversão decimal - binário
def bin_to_dec(bin):
  bin = bin[::-1]  
  dec = 0

  for i in range(len(bin)):
    p = int(bin[i]) * 2 ** i
    dec = dec + p

  return dec