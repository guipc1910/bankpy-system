import sqlite3

conxao = sqlite3.connect("banco_bank.db")
cursor = conxao.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS contas_bancarias(
               id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
               senha TEXT NOT NULL,
                saldo FLOAT NOT NULL)""")

cursor.execute("""CREATE TABLE IF NOT EXISTS transacoes(
               id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
               id_conta INTEGER NOT NULL,
               tipo TEXT NOT NULL,
               valor FLOAT NOT NULL)""")

def cadastro():
    op = 0
    while True:
        print("""[ 1 ] cadastrar
[ 2 ] entrar 
[ 3 ] sair""")
        op = int(input('qual é a sua opção? '))
        if op == 1:
            nome = str(input('qual é seu nome para conta? '))
            senha = str(input('qual é sua senha? '))
            saldo = 0

            cursor.execute("""INSERT INTO contas_bancarias(nome, senha, saldo) VALUES
    (?, ?, ?)""", (nome, senha, saldo))
            conxao.commit()
            id_usuario = cursor.lastrowid
            return (id_usuario, nome, senha, saldo)
        elif op == 2:
            nome = str(input('qual o nome da conta? '))
            senha = str(input('qual é a senha da conta? '))
            
            cursor.execute("""SELECT * FROM contas_bancarias WHERE nome = ? AND senha = ?""", 
                           (nome, senha))
            conta = cursor.fetchone()

            if conta:
                print('login feito!')
                id_usuario = conta[0]
                saldo = conta[3]
                return id_usuario,nome, senha, saldo
            else:
                print('login invalido')
        elif op == 3:
            print('saindo do bankpy! ')
            return None, None, None, None
    
id_usuario, nome, senha, saldo = cadastro()

if id_usuario is None:
    print('programa encerrado')
    exit()

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

                    cursor.execute("""UPDATE contas_bancarias
                    SET saldo = ?
                    WHERE id = ?""",(saldo, id_usuario))
                    conxao.commit()

                    cursor.execute("""INSERT INTO transacoes(id_conta, tipo, valor) VALUES(?, ?, ?)""",(id_usuario,"deposito", d1))
                    conxao.commit()

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

                    cursor.execute("""  UPDATE contas_bancarias
                                   SET saldo = ?
                                   WHERE id = ?""",
                                   (saldo, id_usuario))
                    conxao.commit()

                    cursor.execute("""INSERT INTO transacoes(id_conta, tipo, valor) VALUES (?, ?, ?)
                                   """,(id_usuario,"saque",s3))
                    conxao.commit()

                    print('saque realizado. novo saldo {}'.format(saldo))
                else:
                    print('erro o valor não pode ser correspodido')
            else:
                print('saldo invalido')
        else:
            print('a senha está errada')
    elif opcao == 4:
        cursor.execute("""SELECT tipo, valor FROM transacoes 
                    WHERE id_conta = ?""", (id_usuario,))
        dados = cursor.fetchall()

        print('EXTRATO'.center(30))
        for tipo, valor in dados:
            if tipo == "deposito":
                print(f"[DEPOSITO]+{valor}")
            else:
                print(f"[SAQUE]-{valor}")
    elif opcao == 5:
        print('saindo do bankpy!')
    else:
        print('opção invalida')
