def romanToInt(s):
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
            print(rom, "all greater", t)
        # second pair is <
        elif next <= first and nextnext > next:
            t += first + (nextnext - next)
            del rom[0:3]
            print(rom, "second pair", t)
        #first pair is <
        elif next > first and nextnext <= next:
            t += (next - first)
            del rom[0:2]
            print(rom, "first pair", t)
    if len(rom) == 0:
        return t
    elif len(rom) == 1:
        return t + key.get(rom[0])
    elif len(rom) == 2:
        if key.get(rom[1]) > key.get(rom[0]):
            return t + (key.get(rom[1]) - key.get(rom[0]))
        else:
            return t + (key.get(rom[1]) + key.get(rom[0]))

# all aligned
# 3 2 1

#second pair needs attn
# 3 1 2
# 2 1 3

#first pair needs attn
# 2 3 1
# 1 3 2

#n/a, in roman numerals this will never happen
# 1 2 3

print(romanToInt("CCCI"))
#2594