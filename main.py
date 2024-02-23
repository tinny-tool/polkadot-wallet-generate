from substrateinterface import Keypair
import os


def generate_wallets_and_save_to_file(number_of_wallets, file_name):
    # Check if there is a directory in the file_name path
    directory_name = os.path.dirname(file_name)

    # If there is a directory in the file_name, ensure that it exists
    if directory_name:
        os.makedirs(directory_name, exist_ok=True)

    # Open the file to write the wallet addresses and mnemonic phrases
    with open(file_name, 'a') as f:
        for _ in range(number_of_wallets):
            # Generate a new mnemonic phrase and the corresponding keypair
            keypair = Keypair.create_from_mnemonic(Keypair.generate_mnemonic())
            # Write the wallet address and mnemonic phrase to the file
            f.write(f"Address: {keypair.ss58_address}, Mnemonic: {keypair.mnemonic}\n")


# The number of wallets you want to generate
number_of_wallets_to_generate = 10
# The output file where you want to save the wallet addresses and mnemonic phrases
output_file_name = 'wallet_addresses.txt'

# Call the function to generate wallets and save them to the specified file
generate_wallets_and_save_to_file(number_of_wallets_to_generate, output_file_name)
print(f"Generated {number_of_wallets_to_generate} wallet addresses and saved them to {output_file_name}")
