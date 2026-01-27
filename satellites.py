import space_network_lib

class Satellite(space_network_lib.SpaceEntity):
    def __init__(self, name, distance_from_earth):
        super().__init__(name, distance_from_earth)

    def receive_signal(self, packet: space_network_lib.Packet):
        print(f"[{self.name}] Received: {packet}.")
