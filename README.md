# LaserDrones
software and design files for inter-drone laser communication research

Setup:

Wifi router (TP-link TL-WR841N) is set up to serve DHCP in 192.168.0.100+ range.

Drones may get .101 and .102 but sometimes have to ping to check or scan address range:

nmap -sn 192.168.0.0/24

Simple scripts show how to do single (by IP) commands, and to run a swarm.