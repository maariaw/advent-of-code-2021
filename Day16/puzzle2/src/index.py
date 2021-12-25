from inputreader import InputReader
from decoder import Decoder

def main():
    path = "/home/mawahlst/Documents/Projects/AdventOfCode/Day16/input.txt"
    reader = InputReader(path)
    packet_data = reader.get_one_line_string()
    # packet_data = "C200B40A82" # 3
    # packet_data = "04005AC33890" # 54
    # packet_data = "880086C3E88112" # 7
    # packet_data = "CE00C43D881120" # 9
    # packet_data = "D8005AC2A8F0" # 1
    # packet_data = "F600BC2D8F" # 0
    # packet_data = "9C005AC2F8F0" # 0
    # packet_data = "9C0141080250320F1802104A08" # 1
    value = Decoder(packet_data).get_total_value()
    
    print(f"""
    The total value of the packet is {value}
    """)

if __name__ == "__main__":
    main()
