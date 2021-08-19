#819. Most Common Word
#related topics
#hash table


#first solution
def mostCommonWord(paragraph, banned):
    pattern = '[^A-Za-z0-9]+'
    paragraph = re.sub(pattern, ' ', paragraph.lower()).split(' ')
        

    dic = {}

    for i in paragraph:
        if i not in dic:
            dic[i]=1
        else:
            dic[i]+=1
        if i in banned:
            dic[i]-=1
    return max(dic.items(), key=lambda x:(x[1],x[0]))[0]



def mostCommonWord(self, p, banned):
        ban = set(banned)
        words = re.findall(r'\w+', p.lower())
        return collections.Counter(w for w in words if w not in ban).most_common(1)[0][0]