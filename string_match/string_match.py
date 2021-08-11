'''
实现一个字符集，只包含a～z这26个英文字母的Trie树
实现朴素的字符串匹配算法
'''

def bf(astring,bstring):
    '''
    朴素字符串匹配
    '''
    if len(astring) < len(bstring):
        return False
    for i in range(0,len(astring)-len(bstring)+1):
        j = 0
        while j<len(bstring):
            if astring[i+j] != bstring[j]:
                break
            j += 1
        if j == len(bstring):
            return i
    return False
    
class TrieNode:
    def __init__(self,data=None):
        self.data = data
        self.children = [None] * 26
        self.is_ending_char = False
    
    # def __repr__(self) -> str:
    #     return '{}'.format(self.data)

class Trie:
    '''
    Trie树
    '''
    def __init__(self) -> None:
        self.root = TrieNode('/')

    def insert(self,text):
        p = self.root
        for i in range(0,len(text)):
            index = ord(text[i]) - ord('a')
            if p.children[index] is None:
                new_node = TrieNode(text[i])
                p.children[index] = new_node
            p = p.children[index]
        p.is_ending_char = True
    
    def find(self,pattern):
        p = self.root
        for i in range(0,len(pattern)):
            index = ord(pattern[i]) - ord('a')
            if p.children[index] is None:
                return False
            p = p.children[index]
        if p.is_ending_char is False: #不能完全匹配
            return False
        else: #找到pattern
            return True
    
    # def __repr__(self) -> str:
    #     return '{}'.format(self.root.children)

if __name__ == '__main__':
    print('-------测试Trie------')
    a = Trie()
    a.insert('alpha')
    a.insert('beta')
    a.insert('delta')
    print(a.find('alpha'))
    print(a.find('beta'))
    print(a.find('delta'))
    print(a.find('gama'))

    print('-------测试BF------')
    b = '123'
    c = '123'
    d = '234'
    e = '34'
    f = '23'
    print(bf(b,c))
    print(bf(b,d))
    print(bf(b,e))
    print(bf(b,f))
