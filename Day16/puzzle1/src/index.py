from inputreader import InputReader
from decoder import Decoder

def main():
    path = "/home/mawahlst/Documents/Projects/AdventOfCode/Day16/input.txt"
    reader = InputReader(path)
    # packet_data = reader.get_one_line_string()
    packet_data = "A0016C880162017C3686B18A3D4780" # 31
    # packet_data = "620080001611562C8802118E34" # 12
    # packet_data = "C0015000016115A2E0802F182340" # 23
    # packet_data = "8A004A801A8002F478" # 16
    packets = Decoder(packet_data).get_packets()
    count = 1
    sum = 0
    for packet in packets:
        count += 1
        sum += int(packet["version"])
        print(packet)
    
    print(f"""
    The sum of version numbers is {sum}
    """)

if __name__ == "__main__":
    main()
