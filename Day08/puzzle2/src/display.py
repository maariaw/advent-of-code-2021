class Display:
    def __init__(self, patterns, outputs):
        self.patterns = patterns
        self.outputs = [set(digit) for digit in outputs]
        self.signatures = {}
        # self.segments = {
        #     Segment.A : "",
        #     Segment.B : "",
        #     Segment.C : "",
        #     Segment.D : "",
        #     Segment.E : "",
        #     Segment.F : "",
        #     Segment.G : ""
        # }

    def get_decoded_output(self):
        self.assign_signatures()
        return self.decode_output()

    def assign_signatures(self):
        self.assign_one_four_seven_and_eight()
        self.assign_zero_six_and_nine()
        self.assign_two_three_and_five()

    def decode_output(self):
        number = ""
        for digit in self.outputs:
            for i in range(10):
                if self.signatures[i] == digit:
                    number += str(i)
        return int(number)

    def assign_one_four_seven_and_eight(self):
        self.signatures[1] = self.get_pattern_by_size(2)
        self.signatures[4] = self.get_pattern_by_size(4)
        self.signatures[7] = self.get_pattern_by_size(3)
        self.signatures[8] = self.get_pattern_by_size(7)
        # print("One is ", self.signatures[1])
        # print("Four is ", self.signatures[4])
        # print("Seven is ", self.signatures[7])
        # print("Eight is ", self.signatures[8])

    def assign_zero_six_and_nine(self):
        candidates = self.get_candidates_by_size(6)
        for candidate in candidates:
            if self.signatures[4].issubset(candidate):
                self.signatures[9] = candidate
            elif self.signatures[7].issubset(candidate):
                self.signatures[0] = candidate
            else:
                self.signatures[6] = candidate
        # print("Zero is ", self.signatures[0])
        # print("Six is ", self.signatures[6])
        # print("Nine is ", self.signatures[9])

    def assign_two_three_and_five(self):
        candidates = self.get_candidates_by_size(5)
        for candidate in candidates:
            if self.signatures[1].issubset(candidate):
                self.signatures[3] = candidate
            elif len(self.signatures[4] - candidate) == 1:
                self.signatures[5] = candidate
            else:
                self.signatures[2] = candidate
        # print("Three is ", self.signatures[3])
        # print("Five is ", self.signatures[5])
        # print("Two is ", self.signatures[2])

    def get_candidates_by_size(self, size):
        candidates = [
            set(pattern)
            for pattern in self.patterns
            if len(pattern) == size
        ]
        return candidates

    def get_pattern_by_size(self, size):
        pattern = next(
            pattern
            for pattern in self.patterns
            if len(pattern) == size
        )
        return set(pattern)

#     def assign_segments(self):
#         self.segments[Segment.A] = self.get_signal_by_difference(7, 1)
#         self.segments[Segment.B] = self.get_signal_by_difference(9, 3)
#         self.segments[Segment.C] = self.get_signal_by_difference(1, 5)
#         self.segments[Segment.D] = self.get_signal_by_difference(6, 0)
#         self.segments[Segment.E] = self.get_signal_by_difference(0, 9)
#         self.segments[Segment.F] = self.get_signal_by_difference(1, 2)
#         top_and_bottom = self.signatures[9] - self.signatures[4]
#         for char in top_and_bottom - self.signatures[7]:
#             self.segments[Segment.G] = char
#         for segment in Segment:
#             print(f"{segment} is {self.segments[segment]} ")

#     def get_signal_by_difference(self, original_signature, removed_signature):
#         difference = self.signatures[original_signature] \
#                      - self.signatures[removed_signature]
#         return difference.pop()

# from enum import Enum

# class Segment(Enum):
#     A = 1
#     B = 2
#     C = 3
#     D = 4
#     E = 5
#     F = 6
#     G = 7
