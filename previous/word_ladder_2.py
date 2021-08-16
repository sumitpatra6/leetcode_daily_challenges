def findLadders(beginWord, endWord, wordList):
    from collections import defaultdict
    graph = defaultdict(set)
    for word in wordList:
        for i in range(len(word)):
            key = word[:i] + '_' + word[i+1:]
            graph[key].add(word)
    print(graph)
    def dfs(start, end, distance, visited=[]):
        if start == end:
            return distance
        for i in range(len(start)):
            key = start[:i] + '_' + start[i+1:]
            for node in graph[key]:
                if node not in visited:
                    visited.append(node)
                    r = dfs(node, end, distance + 1)
                    if r:
                        return r
        return None
        
    return dfs(beginWord, endWord, 0)


beginWord = 'hit'
endWord = 'cog'
wordList = ["hot","dot","dog","lot","log","cog"]
result = findLadders(beginWord, endWord, wordList)
print(result)
