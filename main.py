from solathon import Client, PublicKey
from solathon.utils import sol_to_lamport
import time

for i in range(10):
	print(Client("https://api.devnet.solana.com").request_airdrop(PublicKey("YOUR PUBLIC KEY"), sol_to_lamport(2)))
	time.sleep(10)