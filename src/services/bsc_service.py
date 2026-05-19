from web3 import Web3
#Importa a classe principal da biblioteca.

class BSCService:
    def __init__(self, rpc_url: str):
#executa automaticamente service = BSCService(...)

        """
        Inicializa conexão com um nó RPC da Binance Smart Chain
        """

        self.web3 = Web3(
#executa conexão
            Web3.HTTPProvider(rpc_url)
        )


    def is_connected(self):
        """
        Verifica se a conexão foi estabelecida
        """

        return self.web3.is_connected()


    def get_current_block(self):
        """
        Retorna bloco atual da blockchain
        """


        return self.web3.eth.block_number
#Criamos uma camada de serviço. para evitar de colocar a blockchain diretamente no main.py
