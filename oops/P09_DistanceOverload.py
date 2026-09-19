class Distance:
    def __init__(self, ft, inc): self.ft, self.inc = ft, inc
    def __add__(self, other):
        tot_in = self.inc + other.inc
        return Distance(self.ft + other.ft + (tot_in // 12), tot_in % 12)
d1 = Distance(5, 8)
d2 = Distance(4, 6)
d3 = d1 + d2
print(f"{d3.ft} ft, {d3.inc} in")
