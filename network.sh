docker network create -d macvlan \
   --subnet=10.20.4.0/22 \
   --ip-range=10.20.7.0/25 \
   --gateway=10.20.4.1 \
   -o parent=enp37s0 games

#docker network create -d macvlan \
#   --subnet=10.20.4.0/22 \
#   --ip-range=10.20.4.64/26 \
#   --gateway=10.20.4.1 \
#   -o parent=enp37s0.10 games

### Instructions on adding a bridge for the MACVLAN network ###

# ip link add games-bridge link enp37s0 type macvlan mode bridge
# ip addr add 192.168.1.11/32 dev games-bridge 
# ip link set games-bridge up
# ip route add 192.168.1.128/25 dev games-bridge 

# ip link remove games-bridge
