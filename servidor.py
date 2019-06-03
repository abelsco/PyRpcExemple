from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler


# Restringe em uma pasta particular
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2', )

# Cria o servidor
with SimpleXMLRPCServer(('localhost', 8000),
                        requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    # Para metodos existentes

    # Registra a função elevado(pow)
    server.register_function(pow)

    # Para metodos criados
    # Cria a função soma
    def soma(x, y):
        return x + y

    server.register_function(soma, 'soma')

    # Para classes criadas
    # Cria a classe Operador com metodos de multiplicação e divisão
    # todos os metodos serão importados
    class Operador:
        def mult(self, x, y):
            return x * y
        def div(self, x, y):
            return x / y

    server.register_instance(Operador())

    # Roda o servidor em loop
    server.serve_forever()