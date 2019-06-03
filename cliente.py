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
                print(serv.system.listMethods())
            elif op[0] == 'soma':
                if len(op) == 3:
                    print(serv.soma(int(op[1]), int(op[2])))
                else:
                    print('soma A B')
            elif op[0] == 'elevado':
                if len(op) == 3:
                    print(serv.pow(int(op[1]), int(op[2])))
                else:
                    print('elevado A B = (A^B)')
            elif op[0] == 'mult':
                if len(op) == 3:
                    print(serv.mult(int(op[1]), int(op[2])))
                else:
                    print('mult A B')
            elif op[0] == 'div':
                if len(op) == 3:
                    print(serv.div(int(op[1]), int(op[2])))
                else:
                    print('mult A B')
            elif op[0] == 'ex':
                print('{}Saindo{}'.format('**--*' * 5, '*--**' * 5))
            else:
                print('Opção Invalida')
    else:
        print("python cliente [IP] [PORTA]")


if __name__ == "__main__":
    main(sys.argv[1:])

# main(['localhost','8000'])