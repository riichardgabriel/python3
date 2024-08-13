print('Bem vindo ao sistema malvadão ')
numero = input('Digite um número: ')

print('''                    
                                      
   (                  (               
 ( )\          )      )\ )  (      )  
 )((_)  (     (      (()/(  )\  ( /(  
((_)_   )\    )\  '   ((_))((_) )(_)) 
 | _ ) ((_) _((_))    _| |  (_)((_)_  
 | _ \/ _ \| '  \() / _` |  | |/ _` | 
 |___/\___/|_|_|_|  \__,_|  |_|\__,_| 
                                      ''')

numero = '25'
nome = 'Paulo'
idade = 22
endereco = 'rua dos bobo'
numero = 0
telefone = '19 99999-9999'


#print('\nCaro Sr. ' + nome + 'com a idade' + str(idade) + 'residente na' + endereco + ', nº ' + str(numero) + 'e telefone ' + telefone)

print('\nCaro  Sr. {} com a idade {} residente na {}, nº{} e telefone {}' .format(nome, idade, endereco,  numero, telefone))

if idade > 17:
    print('Você é maior de 18 anos de idade')
elif idade<10:
    print('Você é menor que 10 anos')
else:
    print('você NÃO é maior de 18 anos e NÃO é menor de 10 anos')

vogal = ['a', 'e', 'i', 'o', 'u']

if 'i' in 'aeiou':
    print('é vogal')
else:
    print('NÃO é vogal')

for i in range(1,6):
    print(str(i) + '- O Palmeiras NÃO tem mundial')

for letra in 'Santos na Série B':
    print(letra)

'''
01 - Atividade
- Solicitar um número ao usuário
- O sistema deve percorrer do 0 até o número escolhido
- Se o número for menor ou igual a 0 peça que o usuário digite novamente até receber um número valido
- Nesse laço se o número for PAR deve ficar em AZUL e se for IMPAR deve ficar vermelho
'''


#   ///////////////////////////////////////////////---------------////////////////////////////////////////


def print_colored(text, color):
    colors = {
        'green': '\033[92m',  
        'red': '\033[91m',    
        'reset': '\033[0m'    
    }
    return colors.get(color, colors['reset']) + text + colors['reset']

# Solicitar um número ao usuário
while True:
    try:
        numero = int(input('Digite um número: '))
        if numero > 0:
            break
        else:
            print('Por favor, digite um número maior que 0.')
    except ValueError:
        print('Entrada inválida. Digite um número inteiro.')

# Percorrer do 0 até o número escolhido
for i in range(numero + 1):
    color = 'green' if i % 2 == 0 else 'red'
    print(print_colored(str(i), color))



#   ///////////////////////////////////////////////---------------////////////////////////////////////////

# 01- atividade
# - solicitar um numero ao usuario
# - se o numero for menor ou igual a 0 peça que o usuario digite novamente um numero valido
# - deve percorrer de 0 até o numero escolhido
# - no laço se o numero for PAR deve ficar em AZUL e se for IMPAR deve ficar em VERMELHO

# 02 - atividade:

# - solicitar ao 
# -
# -
# -
# -
