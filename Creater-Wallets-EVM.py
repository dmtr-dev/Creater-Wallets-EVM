from eth_account import Account
from ctypes import windll
import os

os.system('cls')
windll.kernel32.SetConsoleTitleW('Creater Wallets EVM | by https://t.me/dmtrcrypto')
print("TG Channel - https://t.me/dmtrcrypto\n\n")


def create_wallets(amount, num_words=12):
    Account.enable_unaudited_hdwallet_features()
    wallets_info = 'address : mnemonic : private_key\n\n\n'

    for _ in range(amount):
        account, mnemonic = Account.create_with_mnemonic(num_words=num_words)
        wallets_info += f'{account.address}:{mnemonic}:{account.key.hex()}\n\n'

    with open('wallets_seed.txt', 'a') as f:
        f.write(wallets_info)

    print('\nКошельки сохранены в файл   wallets_seed.txt')

amount = int(input("\nКоличество кошельков: "))
create_wallets(amount)


input("\nPress Enter to exit...")