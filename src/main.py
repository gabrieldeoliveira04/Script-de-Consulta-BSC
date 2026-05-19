from config.settings import (
    RPC_URL,
    WALLET_ADDRESS,
    TOKEN_ADDRESS
)

from services.bsc_service import (
    BSCService
)

from utils.converters import (
    format_balance
)


service = BSCService(RPC_URL)

print("=" * 40)
print("BSC Wallet Balance Checker")
print("=" * 40)

try:

    if service.is_connected():

        print("Connected successfully")

        current_block = (
            service.get_current_block()
        )

        bnb_balance = (
            service.get_bnb_balance(
                WALLET_ADDRESS
            )
        )

        token_balance = (
            service.get_token_balance(
                WALLET_ADDRESS,
                TOKEN_ADDRESS
            )
        )

        print(
            f"Current block: {current_block}"
        )

        print(
            f"BNB Balance: {format_balance(bnb_balance)} BNB"
        )

        print(
            f"USDT Balance: {format_balance(token_balance)} USDT"
        )

    else:

        print("Connection failed")


except Exception as error:

    print(
        f"Unexpected error: {error}"
    )