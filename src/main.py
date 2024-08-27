from frota import *
import pickle

def operar_carro(carro: Carro):
    print('1- Ligar motor')
    print('2- Desligar motor')
    print('3- Acelerar')

    op = 0
    while op not in (1, 2, 3):
        op = int(input("Digite as opcoes[1-3]: "))

    if op == 1:
        carro.ligar()
    elif op == 2:
        carro.desligar()
    elif op == 3:
        v = float(input("Informe a velocidade: "))
        t = float(input("Informe o tempo: "))
        carro.acelerar(v, t)

if __name__ == "__main__":

    '''    try:
        with open('carros.pkl', 'rb') as arquivo:
            carros = pickle.load(arquivo)
    except Exception as e:
        print(e)'''

    print('Cadastre o primeiro carro')
    nm_modelo = input('Digite o modelo: ')
    nm_marca = input('Digite a marca: ')
    nm_cor = input('Digite a cor: ')
    litros = float(input('Digite quantos litros tem no tanque? '))
    consumo_medio = float(input('Qual o consumo medio? '))

    carro1 = Carro(nm_modelo, nm_marca, nm_cor, 0, False, litros, consumo_medio)

    print('Cadastre o segundo carro')
    nm_modelo = input('Digite o modelo: ')
    nm_marca = input('Digite a marca: ')
    nm_cor = input('Digite a cor: ')
    litros = float(input('Digite quantos litros tem no tanque? '))
    consumo_medio = float(input('Qual o consumo medio? '))

    carro2 = Carro(nm_modelo, nm_marca, nm_cor, 0, False, litros, consumo_medio)

    carros = {}
    carros[id(carro1)] = carro1
    carros[id(carro2)] = carro2

    '''
    Controlando o carro até ele atingir 600 Km ou zerar o tanque
    '''
    try:
        with open('carros.pk1', 'wb') as arquivo:
            pickle.dump(carros, arquivo)
    except Exception as e:
        print(e)


    while carro1.get_odometro() < 600 and carro2.get_odometro() < 600 and (carro1.get_tanque() > 0 or carro2.get_tanque() > 0):
        try:
            op = 0
            while op not in(1, 2):
                op = int(input("Carro [1,2]?"))

            if op == 1:
                operar_carro(carro1)
            else:
                operar_carro(carro2)

            print('Informações atuais dos carros')
            print(carro1.__str__())
            print(carro2)
        except Exception as e:
            print("Erro!")
            print(e)

    carro1.desligar()
    carro2.desligar()
    print(carro1)
    print(carro2)
    if carro1.get_odometro() >= 600 or carro1.get_tanque() < 0:
        print(f"o carro {carro1.modelo} terminou primeiro o destino/acabou primeiro com a gasolina")
        print(carro1)
    else:
        print(f"o carro {carro2.modelo} terminou primeiro o destino/acabou primeiro com a gasolina")
        print(carro2)