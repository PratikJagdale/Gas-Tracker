from ethereum_gasprice import GaspriceController, GaspriceStrategy
from ethereum_gasprice.providers import EtherscanProvider

ETHERSCAN_API_KEY = "SUNNQGAB9FGK5AJSY72EIB9G7X3RRR2HK5"

# Pass api key to GaspriceController to initialize provider
controller = GaspriceController(
    settings={EtherscanProvider.title: ETHERSCAN_API_KEY},
)