class Decoder:
    def __init__(self, hex_string):
        num_of_bits = 4 * len(hex_string)
        integer = int(hex_string, 16)
        
        self.binary = f"{integer:0>{num_of_bits}b}"
        # self.binary = bin(int(hex_string, 16))[2:].zfill(num_of_bits)
        # print(self.binary)
        self.packets = []
        self.parse_packet(0)

    def parse_packet(self, index):
        packet = {}
        k  = index
        # print("index = ", k)
        version_binary = self.binary[k:k+3]
        # print("version binary = ", version_binary)
        packet["version"] = int(version_binary, 2)
        # print("version = ", packet["version"])
        k += 3
        # print("index = ", k)
        type_binary = self.binary[k:k+3]
        # print("type binary = ", type_binary)
        packet["type"] = int(type_binary, 2)
        # print("type = ", packet["type"])
        k += 3
        if packet["type"] == 4:
            # print("parsing literal value")
            number_bits = ""
            last_number = False
            while not last_number:
                number_bits += self.binary[k+1:k+5]
                # print("index = ", k)
                if self.binary[k] == "0":
                    last_number = True
                k += 5
        else:
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
                    k = self.parse_packet(k)
                # print("subpackets parsed")
            else:
                length_binary = self.binary[k:k+11]
                packet_total = int(length_binary, 2)
                # print("subpackets = ", packet_total)
                k += 11
                packet_count = 0
                while packet_count < packet_total:
                    # print("parsing subpackets")
                    k = self.parse_packet(k)
                    packet_count += 1
                # print("subpackets parsed")
        self.packets.append(packet)
        # print(f"""
        #     Packet {len(self.packets)}: version {packet["version"]}, type {packet["type"]}
        # """)
        return k

    def get_packets(self):
        return self.packets
