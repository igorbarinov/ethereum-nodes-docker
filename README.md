## Ethereum nodes ##

In few commands: (thx to docker compose ;)
- run both clients (parity & geth)
- check accounts and status
- make a transaction (transfert test eth)

I use this setup for production
- data stays on host for easy version migration
- Auto unlock wallets when container is starting (please use firewall to protect your prod nodes!)
 

# 0. Prerequisit:

Ubuntu or other flavor
Docker
docker-compose

Account info:
geth
gethtest: 0x881bce7131857c9d24effdbe39ea974fd3c43e50
parity:
paritytest: 0x9e6c69b73f5808a25404edcf7eac7bf8ee935568

Password: notsecure

# 1. Setup git

    git clone https://github.com/gregbkr/ethereum-nodes && cd eth

# 2. Setup Nodes:

Run the script for create data volume to store: account&password, blockchaindata:    

    ./deploy-init.sh

If you want to use a fresh new wallet for paritytest:

    docker run --rm -it -v eth_paritytest:/root/.parity ethcore/parity -testnet account new
	#OR docker exec -it parity bash -c "/build/parity/target/release/parity --testnet --password <(echo -n notsecure) account new"
    ls /var/lib/docker/volumes/eth_paritytest/_data/testnet_keys/  <-- your test wallet is here

	docker run --rm -it -v eth_gethtest:/root/.ethereum ethereum/client-go --testnet account new
    ls /var/lib/docker/volumes/eth_gethtest/_data/testnet/keystore/  <-- your test wallet is here


And setup password:

    echo -n 'notsecure' > /var/lib/docker/volumes/eth_paritytest/_data/testnet_keys/mypass     <-- unsure that there is no space or new line in file: don't use nano, it leave a new line!!

	
# 4. Checks 

Account:

    docker exec eth_paritytest_1 /build/parity/target/release/parity --testnet account list
    docker exec eth_gethtest_1 geth --testnet account list


Use the python script to check data. If can send few ether 0.001 to this new account and try the sendTransaction fonctionnality.
	
	apt-get install python3-pip
	pip3 install --upgrade pip
	pip3 install web3

	python3 checkParityNode.py

Or classic curl

    curl -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getBalance","params":["0x0037a6b811ffeb6e072da21179d11b1406371c63", "latest"],"id":1}' http://127.0.0.1:8545

		
# help
    
	docker run -ti ethcore/parity --help
	
https://github.com/ethereum/wiki/wiki/JavaScript-API#web3versionnode
https://github.com/ethereum/wiki/wiki/JSON-RPC
