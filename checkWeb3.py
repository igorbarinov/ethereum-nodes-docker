#!usr/bin/python3 -u
# -*- encoding: utf-8 -*-
# please install: apt-get install -y python3-pip, pip3 install web3

from web3 import Web3, RPCProvider, IPCProvider

### Parameters ##################
web3            = Web3(RPCProvider(host='127.0.0.1', port='8545')) # Paritytest:8545, (gethtest:8543)
remoteTestnet	= '0xf734e65a97c7e5ca5e5255d91f236751a6649d0b'  # our gethtest node: 0xf734e65a97c7e5ca5e5255d91f236751a6649d0b
remote		= remoteTestnet
amountInEther   = 0.000111111
gas             = 21000
gasPrice        = 20000000000
value           = web3.toWei(amountInEther,'ether')
#################################

if web3.version.network == 1: network = 'LIVE(Homestead)'
if web3.version.network == 2: network = 'TESNET(morden)'

print ('\n#######  Node info ############## <-- Please edit with your needs!')
print ('Network		: '+ str(web3.version.network) +' --> '+network)
print ('NodeVersion	: '+ str(web3.version.node))
print ('Block		: '+ str(web3.eth.blockNumber))
print ('Syncing? 	: '+ str(web3.eth.syncing))
print ('Peers		: '+ str(web3.net.peerCount))
print ('All my accounts	: '+ str(web3.eth.accounts))

print ('LocalAddr0 = '+web3.eth.accounts[0]+'     balance = '+ str(web3.eth.getBalance(web3.eth.accounts[0])) +'    --> '+str(web3.fromWei(web3.eth.getBalance(web3.eth.accounts[0]),'ether'))+' Ether')
print ('RemoteAddr = '+remote+'     balance = '+ str(web3.eth.getBalance(remote)) +'    --> '+str(web3.fromWei(web3.eth.getBalance(remote),'ether'))+' Ether')


# Send ether
q= input ('\n--> Send tx of '+str(amountInEther)+' Ether from localAddr0:'+str(web3.eth.accounts[0])+' to remoteAddr:'+str(remote)+' on network '+network+' ? [y/N]')

if q == 'Y' or q=='y':
  tx = web3.eth.sendTransaction({'from':web3.eth.accounts[0], 'to':remote, 'value': value})
  print(tx)

