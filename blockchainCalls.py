from web3 import Web3
import requests


def wei_to_ether(amount):
    return float(amount) / 1000000000000000000


class avax_contract:
    def __init__(self, address):
        self.address = address
        self.abi = requests.get("https://api.snowtrace.io/api?module=contract&action=getabi&address=" + address).json()["result"]
        self.contract = chain.eth.contract(Web3.toChecksumAddress(address), abi=self.abi)

    def call(self, function, inputs):
        return self.contract.functions[function](inputs).call()


ANKR = 'https://rpc.ankr.com/avalanche'
chain = Web3(Web3.HTTPProvider(ANKR))
VEJOE = avax_contract("0x3cabf341943bc8466245e4d6f1ae0f8d071a1456")
