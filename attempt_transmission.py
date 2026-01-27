import satellites
import time
import space_network_lib
class BrokenConnectionError(space_network_lib.CommsError):
    pass
def attempt_transmission(packet:space_network_lib.Packet, network:space_network_lib.SpaceNetwork):
    flag = 0
    while flag == 0:
        try:
            network.send(packet)
            flag = 1
        except space_network_lib.TemporalInterferenceError:
            print("Interference, waiting ...")
            time.sleep(2)
        except space_network_lib.DataCorruptedError:
            print("Data corrupted, retrying...")
        except space_network_lib.LinkTerminatedError:
            print("lost Link")
            raise BrokenConnectionError
        except space_network_lib.OutOfRangeError:
            print("Target out of range" )
            raise BrokenConnectionError