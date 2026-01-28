from space_network_lib import SpaceNetwork, Packet
from satellites import Satellite
from attempt_transmission import attempt_transmission, BrokenConnectionError
network_1 = SpaceNetwork(3)

set1 = Satellite("Set1", 100)
set2 = Satellite("Set2", 200)
packet1 = Packet("you are a chiter", set1, set2)
try:
    attempt_transmission(packet1,network_1)
except BrokenConnectionError:
    print("failed Transmission")