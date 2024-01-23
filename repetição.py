while (True):
  caracteres = input("Bem-vindo ao contador Proz! Digite 0  para começar ou 1 para sair do sistema.")
  if(caracteres == "1"):
    print("Você saiu do sistema")
    break
  elif(caracteres == "0"):
   caracteres = input("Escreva a sua palavra , por gentileza")
   print(f"A quantidade de caracteres é: " , len(caracteres))
  else:
    print(input("Retornaremos ao começo."))