from config.settings import RPC_URL
from services.bsc_service import BSCService


service = BSCService(RPC_URL)


print("=" * 40)

print("BSC Wallet Balance Checker")

print("=" * 40)


if service.is_connected():

    print("Connected successfully")

    current_block = service.get_current_block()

    print(f"Current block: {current_block}")

else:

    print("Connection failed")