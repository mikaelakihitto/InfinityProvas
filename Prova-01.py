# Faça um programa em python que determine em duas variáveis (senha e email) 
#e que contenha uma senha e um email cadastrados antecipadamente, em seguida 
#solicite ao usuário uma senha e um email e utilize o laço de repetição juntamente 
#com a estrutura de condição para verificar se o email e a senha digitado pelo usuário é igual
# ao email e senha cadastrados antecipadamente. E enquanto a senha e o email que o usuário digitou não for igual ao email e senha cadastrados ele continue em um loop.

email = 'email@email.com'
senha = '1234'

usuarioemail = input('Digite seu email')
usuariosenha = input('Digite sua senha')
while email != usuarioemail or senha != usuariosenha:
    print('Senha ou email invalidos!')
    usuarioemail = input('Digite seu email')
    usuariosenha = input('Digite sua senha')
print('login com sucesso')