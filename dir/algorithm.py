#Algorithm

import numpy as np
import random



random.seed(42)

output = []

for i in range(1):

  temp = []

  FCN = ['FCN', random.randint(2, 105), random.randint(1, 110)]
  FNC = ['FNC',random.randint(3, 106), random.randint(1, 120)]
  FNN = ['FNN',random.randint(4, 107), random.randint(1, 130)]
  CFN = ['CFN',random.randint(5, 108), random.randint(1, 140)]
  CNF = ['CNF',random.randint(6, 109), random.randint(1, 150)]
  CNN = ['CNN',random.randint(7, 125), random.randint(1, 160)]
  NFC = ['NFC',random.randint(8, 152), random.randint(1, 170)]
  NFN = ['NFN',random.randint(9, 122), random.randint(1, 180)]
  NCF = ['NCF',random.randint(10, 133), random.randint(1, 190)]
  NCN = ['NCN',random.randint(11, 144), random.randint(1, 101)]
  NNF = ['NNF',random.randint(12, 155), random.randint(1, 102)]
  NNC = ['NNC',random.randint(13, 166), random.randint(1, 103)]
  NNN = ['NNN',random.randint(14, 199), random.randint(1, 104)]

  temp = [FCN, FNC, FNN, CFN, CNF, CNN, NFC, NFN, NCF, NCN, NNF, NNC, NNN]

  output.append(temp)

print(output)

# Possible sol algorithm (TOY ONE is enough) 
# IN PROGRESS 

def alg_mat(tree):
  #algorithm
  #backward induction
  output = []
  for i in range(len(tree)):
    output = tree[i]
    #choice wife in the third line

    #choose between FNC and FNN
    if (output[1][1]>output[2][1]):
      FN=output[1]
    else:
      FN=output[2]
    print('FN:',FN)

    #choose between CNF and CNN
    if (output[4][1]>output[5][1]):
      CN=output[4]
    else:
      CN=output[5]
    print('CN:',CN)

    #choose between NFC and NFN
    if (output[6][1]>output[7][1]):
      NF=output[6]
    else:
      NF=output[7]
    print('NF:',NF)


    #choose between NCF and NCN
    if (output[8][1]>output[9][1]):
      NC=output[8]
    else:
      NC=output[9]
    print('NC:',NC)


    #choose between NNF, NNC and NNN
    if (output[10][1]>output[11][1]):
      if (output[10][1]>output[12][1]):
        NN=output[10]
      else:
        NN=output[12]
    else:
      if (output[11][1]>output[12][1]):
        NN=output[11]
      else:
        NN=output[12]
      print('NN:',NN)

      
    #choice Husband in the second line

    #choose between FCN and FN
    if (output[0][2]>FN[2]):
      F=output[0]
    else:
      F=FN
    print('F:',F)


    #choose between CFN and CN
    if (output[3][2]>CN[2]):
      C=output[3]
    else:
      C=CN
    print('C:',C)


    #choose between NF, NC and NN
    if (NF[2]>NC[2]):
      if(NF[2]>NN[2]):
        N=NF
      else:
        N=NN
    else:
      if(NC[2]>NN[2]):
        N=NC
      else:
        N=NN
    print('N:',N)


    #choice wife in first line and solution

    #coose between F, C and N
    if(F[1]>C[1]):
      if(F[1]>N[1]):
        solution=F
      else:
        solution=N
    else:
      if(C[1]>N[1]):
        solution=C
      else:
        solution=N

    print('Solution: ', solution)
    output = []