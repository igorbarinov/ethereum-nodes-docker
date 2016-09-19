#!usr/bin/python
# -*- encoding: utf-8 -*-
# please install: apt-get install python3-pip, pip3 install web3

from web3 import Web3, RPCProvider, IPCProvider

### Parameters ##################
remoteLivenet   = ''  #
remoteTestnet	= '0xf734e65a97c7e5ca5e5255d91f236751a6649d0b'  # our gethtest node: 0xf734e65a97c7e5ca5e5255d91f236751a6649d0b
remote		= remoteTestnet 	# <-- Please choose the target
amountInEther   = 0.000111111
web3 		= Web3(RPCProvider(host='127.0.0.1', port='8545')) # Paritytest:8545, gethtest:8543
#################################

account0 	= web3.eth.accounts[0]
balance 	= web3.eth.getBalance(web3.eth.accounts[0])
balanceRemote	= web3.eth.getBalance(remote)
value           = hex(web3.toWei(amountInEther,'ether'))

if web3.version.network == 1: network = 'LIVE(Homestead)'
if web3.version.network == 2: network = 'TESNET(morden)'

print ('\n#######  Node info ############## <-- Please edit with your needs!')
print ('Network		: '+ str(web3.version.network) +' --> '+network)
print ('NodeVersion	: '+ str(web3.version.node))
print ('Block		: '+ str(web3.eth.blockNumber))
print ('Syncing? 	: '+ str(web3.eth.syncing))
print ('Peers		: '+ str(web3.net.peerCount))
print ('All my accounts	: '+ str(web3.eth.accounts))
print ('Balance account0: '+ str(account0)+' = '+ str(balance) +'	--> '+str(web3.fromWei(balance,'ether'))+' Ether')
print ('Balance remoteAd: '+remote+' = '+ str(balanceRemote) +'	--> '+str(web3.fromWei(balanceRemote,'ether'))+' Ether')

# Send ether
q= input ('\n--> Send tx of '+str(amountInEther)+' Ether to address '+str(remote)+' on network '+network+' ? [y/N]')

if q == 'Y' or q=='y': 
  web3.eth.sendTransaction({'from':account0, 'to':remote, 'value': value})
  print('done!\n')

