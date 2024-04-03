'''
Time Complexity - O(n)
Space Complexity - O(n). We are using a HashSet here.
Works on Leetcode
'''
class TrieNode:
    def __init__(self):
        #create a Trie Node
        self.children = [None for i in range(256)]
        self.startsWith = []

class AutocompleteSystem:
    def __init__(self, sentences: List[str], times: List[int]):
        #Create a map and the trie, insert the sentences in trie and hmap
        self.root = TrieNode()
        self.hmap={}
        self.searchTerm = ""
        for i in range(len(sentences)):
            self.hmap[sentences[i]] = self.hmap.get(sentences[i], 0) + times[i] 
            self.insert(sentences[i])  

    def insert(self, word):
        #insert every word in the Trie. Now along with every character also sort the list by hotness
        curr = self.root
        for i in range(len(word)):
            idx = ord(word[i]) - ord(" ")
            if curr.children[idx] == None:
                curr.children[idx] = TrieNode()
            curr = curr.children[idx]
            currList = curr.startsWith
            if word not in currList:
                currList.append(word)
            currList.sort(key=lambda word:(-self.hmap[word], word))
            if len(curr.startsWith) > 3:
                curr.startsWith.pop()
            
    
    def search(self, word)->List[str]:
        #search the input in the Trie and return the top 3 recommendations with the word
        curr = self.root
        for c in word:
            idx = ord(c) - ord(" ")
            if curr.children[idx] == None:
                return []
            curr = curr.children[idx]
        return curr.startsWith
    
    
    
    def input(self, c: str) -> List[str]:
        #if input is "#" then append the input to the Trie
        if c == "#":
            prefix = self.searchTerm
            print(prefix)
            self.hmap[prefix] = self.hmap.get(prefix, 0)+1
            self.insert(prefix)
            print(self.hmap[prefix])
            self.searchTerm = ""
            return []
        pq = []
        self.searchTerm+=c
        prefix = self.searchTerm
        # probables = self.search(prefix)
        # print(f"Input{prefix} Probables:{probables}")
        # for sentence in probables:
        #     pq.append(sentence)
        #     pq.sort(key=lambda x:(-self.hmap[x], x))
        #     if len(pq) > 3:
        #         pq.pop()
        #return the list of recommendations for the input
        return self.search(prefix)
        


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.searchTerm(c)