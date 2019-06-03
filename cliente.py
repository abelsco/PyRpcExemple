import sys
import xmlrpc.client as cli


def main(argv):
    if len(argv) == 2:
        str = 'http://' + argv[0] + ':' + argv[1]
        serv = cli.ServerProxy(str)
        op = '', '', ''
        while op[0] != 'ex':
            op = input(
                '\n{} Insira um comando ou ? para ajuda [exit para sair] {}\n'.format('-*' * 5, '*-' * 5)
            ).strip()
            op = op.split(' ')
            if op[0] == '?':
                print('{}Lista de comandos{}'.format('*-'*10,'*-'*10))
                print('soma [A] [B] - Soma A e B e retorna')
                print('elevado [A] [B] - A^B')
                print('mult [A] [B] - Multiplica A e B e retorna')
                print('div [A] [B] - Divide A e B e retorna')
                print('ex - Encerra a calculadora')
                print('{}'.format('***'*20))
            elif op[0] == 'soma':
                if len(op) == 3:
                    print(serv.soma(float(op[1]), float(op[2])))
                else:
                    print('soma A B')
            elif op[0] == 'elevado':
                if len(op) == 3:
                    print(serv.pow(float(op[1]), float(op[2])))
                else:
                    print('elevado A B')
            elif op[0] == 'mult':
                if len(op) == 3:
                    print(serv.mult(float(op[1]), float(op[2])))
                else:
                    print('mult A B')
            elif op[0] == 'div':
                if len(op) == 3:
                    print(serv.div(float(op[1]), float(op[2])))
                else:
                    print('div A B')
            elif op[0] == 'ex':
                print('{}Saindo{}'.format('**--*' * 5, '*--**' * 5))
            else:
                print('Opção Invalida')
    else:
        print("python cliente [IP] [PORTA]")


if __name__ == "__main__":
    main(sys.argv[1:])

# main(['localhost','8000'])