from space_network_lib import SpaceNetwork, Packet
from satellites import Satellite
network_1 = SpaceNetwork()

set1 = Satellite("set1", 100)
set2 = Satellite("set2", 200)
packet1 = Packet("you are a chiter", set1, set2)
network_1.send(packet1)