def isAnagram(s, t):
    s = list(s)
    t = list(t)
    s.sort()
    t.sort()
    return s == t