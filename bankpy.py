import sqlite3

conxao = sqlite3.connect("banco_bank.db")
cursor = conxao.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS contas_bancarias(
               id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
               senha TEXT NOT NULL UNIQUE,
                saldo FLOAT NOT NULL)""")

def cadastro():
    print('CADASTRO'.center(30))
    nome = str(input('qual é seu nome para conta? ')) #pedi o nome
    senha = str(input('qual é sua senha? '))
    saldo = 0

    cursor.execute("""INSERT INTO contas_bancarias(nome, senha, saldo) VALUES
    ('nome', 'senha', 'saldo')""")

    cursor.execute("""SELECT * FROM contas_bancarias""")
    conxao.commit()
    return nome, senha, saldo

nome, senha, saldo = cadastro()

d1 = 0
s3 = 0
print('seu nome é {} e seu saldo é de {}'.format(nome, saldo)) #fala as informações  


opcao = 0
print('='*30)
print('SEJA BEM VINDO AO BANKPY'.center(30))
print('='*30)
while opcao != 5:
    print('='*30)
    print('MENU PRINCIPAL'.center(30))
    ('='*30)
    print('''      [ 1 ] ver o valor
      [ 2 ] deposito
      [ 3 ] sacar
      [ 4 ] extrato
      [ 5 ] sair''')
    opcao = int(input('qual opção '))
    if opcao == 1:
        print('seu saldo é de {}'.format(saldo))
    elif opcao == 2:
            acesso = str(input('qual é a senha? '))
            if acesso == senha:
                d1 = float(input('você que depositar quantos? '))

                if d1 > 0:
                    saldo = saldo + d1
                    print('esse é seu saldo {}'.format(saldo))
                else:
                    print('erro o valor não pode ser correspodido')
            else:
                print('a senha esta incorreta')
    elif opcao == 3:
        acesso = str(input('qual é a senha? '))
        if acesso == senha:
            s3 = float(input('quantos vc quer sacar? '))
            
            if s3 > 0:
                if saldo >= s3:
                    saldo = saldo - s3
                    print('saque realizado. novo saldo {}'.format(saldo))
                else:
                    print('erro o valor não pode ser correspodido')
            else:
                print('saldo invalido')
        else:
            print('a senha está errada')
    elif opcao == 4:
        print('EXTRATO'.center(30))
        print('o deposito foi de: +{}' .format(d1))
        print('o saque foi de: -{}' .format(s3))
        print('esse é o saldo atual: {}' .format(saldo))
    elif opcao == 5:
        print('saindo do bankpy!')
    else:
        print('opção invalida')
