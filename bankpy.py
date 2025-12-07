nome = input('qual é seu nome para conta? ') #pedi o nome
saldo = 0
print('seu nome é {} e seu saldo é de {}'.format(nome, saldo)) #fala as informações  
opcão = 0
print('='*30)
print('SEJA BEM VINDO AO BANKPY'.center(30))
print('='*30)
while opcão != 5:
    print('='*30)
    print('MENU PRINCIPAI'.center(30))
    print('='*30)
    print('''      [ 1 ] ver o valor
      [ 2 ] deposito
      [ 3 ] sacar
      [ 4 ] extrado
      [ 5 ] sair''')
    opcão = int(input('qual opção '))
    if opcão == 1:
        print('seu saldo é de {}'.format(saldo))
    elif opcão == 2:
        d1 = float(input('você que depositar quantos? '))
        saldo = saldo + d1
        print('esse é seu saldo {}'.format(saldo))
    elif opcão == 3:
        s3 = float(input('quantos vc quer sacar? '))
        if saldo >= s3:
            saldo = saldo - s3
            print('novo saldo'.format(saldo))
        else:
            print('não deu para fazer o saca')
        print('esse é o seu valor novo {}'.format(saldo))
    elif opcão == 4:
        print('EXTRADO'.center(30))
    elif opcão == 5:
        print('saindo do bankpy!')
    else:
        print('opção invalida')

