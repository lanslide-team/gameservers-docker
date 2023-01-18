docker network create -d macvlan \
   --subnet=192.168.1.1/24 \
   --ip-range=192.168.1.128/25 \
   --gateway=192.168.1.1 \
   -o parent=enp37s0 games

### Instructions on adding a bridge for the MACVLAN network ###

# ip link add games-bridge link enp37s0 type macvlan mode bridge
# ip addr add 192.168.1.11/32 dev games-bridge 
# ip link set games-bridge up
# ip route add 192.168.1.128/25 dev games-bridge 

# ip link remove games-bridge
