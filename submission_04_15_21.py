class Solution():
    def romanToInt(self, s):
        rom = list(s)
        key = {"I": 1,
               "V": 5,
               "X": 10,
               "L": 50,
               "C": 100,
               "D": 500,
               "M": 1000}
        t = 0
        while len(rom) > 2:
            first = key.get(rom[0])
            next = key.get(rom[1])
            nextnext = key.get(rom[2])
            # all greater
            if next <= first and nextnext <= next:
                t += first + next
                del rom[0:2]
            # second pair is <
            elif next <= first and nextnext > next:
                t += first + (nextnext - next)
                del rom[0:3]
            #first pair is <
            elif next > first and nextnext <= next:
                t += (next - first)
                del rom[0:2]
        if len(rom) == 0:
            return t
        elif len(rom) == 1:
            return t + key.get(rom[0])
        elif len(rom) == 2:
            if key.get(rom[1]) > key.get(rom[0]):
                return t + (key.get(rom[1]) - key.get(rom[0]))
            else:
                return t + (key.get(rom[1]) + key.get(rom[0]))