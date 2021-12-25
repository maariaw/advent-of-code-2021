from operation_factory import OperationFactory
from packet import Packet

class Decoder:
    def __init__(self, hex_string):
        num_of_bits = 4 * len(hex_string)
        integer = int(hex_string, 16)
        
        self.binary = f"{integer:0>{num_of_bits}b}"
        # self.binary = bin(int(hex_string, 16))[2:].zfill(num_of_bits)
        # print(self.binary)
        self.packets = []
        self.parse_packet(0, self.packets)

    def parse_packet(self, index, superpacket):
        k  = index
        # print("index = ", k)
        version_binary = self.binary[k:k+3]
        # print("version binary = ", version_binary)
        packet_version = int(version_binary, 2)
        # print("version = ", packet["version"])
        k += 3
        # print("index = ", k)
        type_binary = self.binary[k:k+3]
        # print("type binary = ", type_binary)
        packet_type = int(type_binary, 2)
        # print("type = ", packet["type"])
        k += 3
        packet = Packet(packet_version, packet_type)

        if packet_type == 4:
            # print("parsing literal value")
            number_bits = ""
            last_number = False
            while not last_number:
                number_bits += self.binary[k+1:k+5]
                # print("index = ", k)
                if self.binary[k] == "0":
                    last_number = True
                k += 5
            value = int(number_bits, 2)
            packet.set_value(value)
        else:
            subpackets = []
            length_type = self.binary[k]
            # print("length type = ", length_type)
            k += 1
            if length_type == "0":
                length_binary = self.binary[k:k+15]
                k += 15
                length = int(length_binary, 2)
                # print("length = ", length)
                end = k + length
                while k < end:
                    # print("parsing subpackets")
                    k = self.parse_packet(k, subpackets)
                # print("subpackets parsed")
            else:
                length_binary = self.binary[k:k+11]
                packet_total = int(length_binary, 2)
                # print("subpackets = ", packet_total)
                k += 11
                packet_count = 0
                while packet_count < packet_total:
                    # print("parsing subpackets")
                    k = self.parse_packet(k, subpackets)
                    packet_count += 1
                # print("subpackets parsed")
            packet.add_subpackets(subpackets)
        superpacket.append(packet)
        # print(f"""
        #     Packet {len(self.packets)}: version {packet["version"]}, type {packet["type"]}
        # """)
        return k

    def get_packets(self):
        return self.packets

    def get_total_value(self):
        return self.get_value(self.packets[0])

    def get_value(self, packet: Packet):
        if packet.type == 4:
            return packet.value
        else:
            subpacket_values = []
            for subpacket in packet.subpackets:
                subpacket_values.append(self.get_value(subpacket))
            operation = OperationFactory.get_operation(packet.type)
            return operation.calculate(subpacket_values)
