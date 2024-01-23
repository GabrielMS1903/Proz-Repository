while (True):   #Usando boolean para o programa sempre rodar
  caracteres = input("Bem-vindo ao contador Proz! Digite 0  para começar ou 1 para sair do sistema.")
  if(caracteres == "1"):
    print("Você saiu do sistema")
    break #Esse break será necessário para finalizar o programa quando o user sair do sistema
  elif(caracteres == "0"):
   caracteres = input("Escreva a sua palavra , por gentileza")
   print(f"A quantidade de caracteres é: " , len(caracteres))  
  else:  #um break abaixo acima desse else não é necessário, senão o user não terá a opção de sair do sistema quando quiser.
    print(input("Retornaremos ao começo. Digite qualquer tecla")) #Esse input será usado apenas para o user retornar ao começo caso não aperte nem 1 ou 0

    #Sintam-se livres para fazer qualquer mudanças e lançar os seus commit.  https://github.com/GabrielMS1903/Proz-Repository  a branch com alteraçôes é a grupo