#1796. Second Largest Digit in a String
#realted topics
#hash table


s = "dfa12321afd"
#s = "abc1111"

def secondHigest(s):
    lst = []
    for i in set(s):
        if i.isdigit():
            lst.append(int(i))
    try:
        lst.remove(max(lst))
        maximum = max(lst)
        return maximum
    except:
        return -1

print(secondHigest(s))


def secondHighest(self, s: str) -> int:
        first = sec = -1
        for c in s:
            if c.isdigit():
                d = ord(c) - ord('0')
                if first < d:
                    sec, first = first, d
                elif sec < d and d < first:
                    sec = d
        return sec