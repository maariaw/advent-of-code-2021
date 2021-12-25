class Packet:
    def __init__(self, version, type):
        self.version = version
        self.type = type
        self.subpackets = []
        self.value = 0
    
    def add_subpackets(self, packets):
        self.subpackets.extend(packets)
    
    def set_value(self, value):
        self.value = value

    def __str__(self):
        string = f"""
            Version: {self.version}
            Type: {self.type}
        """
        if self.subpackets:
            string += "    Packets:\n"
            for packet in self.subpackets:
                string += str(packet)
        else:
            string += f"    Value: {self.value}\n"
        return string
