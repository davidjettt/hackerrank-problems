def longest_common_prefix(strs):
    '''
    [flower, flow, flight] -> fl


    prefix = f
    [flower, flow, flight]
      i

    flower
     i

    start at [:1] -> gets first letter
    end at [:len(string)] -> gets entire string

    base case:
        1) if j >= len(string) -> then cant break word up anymore
        2) if i == len(strs) -> then no more words and return prefix?

    [dog, racecar, car] -> ''

    '''
    shortestWordLen = float('inf')
    for word in strs:
        shortestWordLen = min(shortestWordLen, len(word))

    def dfs(prefix, i):
        if i > shortestWordLen:
            return prefix

        prefix = strs[0][:i]
        for j in range(1, len(strs)):
            word = strs[j]
            if word[:i] != prefix:
                return prefix[:i-1]

        return dfs(prefix, i + 1)

    return dfs('', 1)
