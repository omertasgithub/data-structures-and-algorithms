#04. Unique Morse Code Words
#realted topics


import string

words = ["gin", "zen", "gig", "msg"]



def uniqueMorseRepresentations(words):
    
    a = string.ascii_lowercase
    morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    
    dic = {}
    for i,j in zip(a,morse):
        dic[i]=j
    
    all_lst = []
    for i in words:
        lst = []
        for j in i:
            lst.append(dic[j])
        all_lst.append("".join(lst))
    return len(set(all_lst))


print(uniqueMorseRepresentations(words))

def uniqueMorseRepresentations2(words):
        d = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
             "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        return len({''.join(d[ord(i) - ord('a')] for i in w) for w in words})

print(uniqueMorseRepresentations2(words))
