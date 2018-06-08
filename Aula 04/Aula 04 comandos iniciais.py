#imprime: Olá Mundo
print('Olá Mundo');  

 #imprime: 47 trata com texto devido as aspas
print('4'+'7');

#imprime: 10 - trata como Numero
print(4+6);

#imprime: 4+6
print('4+6'); 

#imprime: olá5
print('olá'+'5');

#imprime: olá 5 - A virgula coloca o espaco entre o texto e o numero
print('olá',5);

'''
Variavel
 - toda variavel é um object, 
 - usar nomes minusculos 
'''
nome = 'Aluno 1';

idade = 27; 

peso = 66.6;

'''
 Como tem variavel com numero deve-se usar a virgula
 para poder separa melhor os dados, não se usa o +

saida abaixo: Leandro 66.6 27
'''
print(nome, peso, idade);

'''
Para pegar dados do usario, comando input
o que for digita vai ser coloca dentro da variavel
ao qual o input ta sendo usada
'''
nome = input("Qual é seu nome?");
peso = input("Qual é seu Peso?");
idade = input("Qual é sua Idade?");