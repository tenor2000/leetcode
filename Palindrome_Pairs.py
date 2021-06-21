def palindromePairs(words):
    """
    type: List[str]
    rtype: List[List[int]]
    """
    # initialize dictionary with backwards word keys
    d = {}
    for i, word in enumerate(words):
        d[word[::-1]] = i

    result = []

    for i, word in enumerate(words):  
        for j in range(len(word)+1):
            pre = word[:j]  # pre is the beginning of word
            post = word[j:] # post is the end of word not included in the pre
            # now check if pre is in the backward library, that the index is not the same, that the remaining letters are also a palindrome
            if pre in d and i != d[pre] and post == post[::-1]:
                result.append([i, d[pre]])
            # now check if post is in the backward library, that the index is not the same, that the remaining letters are als a palindrome
            if j > 0 and post in d and i != d[post] and pre == pre[::-1]:
                result.append([d[post], i])

    return result