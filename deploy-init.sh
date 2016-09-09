
echo "1. Setup local volumes for blockchains"

docker volume create --name eth_geth
docker volume create --name eth_gethtest

docker volume create --name eth_parity
docker volume create --name eth_paritytest

echo "2. Setup accounts and passwords"

#cp -r geth-keys /var/lib/docker/volumes/eth_geth/_data
cp -r gethtest/* /var/lib/docker/volumes/eth_gethtest/_data/

#cp -r parity-keys /var/lib/docker/volumes/eth_parity/_data
cp -r paritytest/* /var/lib/docker/volumes/eth_paritytest/_data/

