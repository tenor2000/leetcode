def makesquare(matchsticks):
    """
    type: List[int]
    rtype: bool
    """
    matchsticks.sort(reverse = True)
    len_side = sum(matchsticks)/4

    if sum(matchsticks) % 4 != 0 or matchsticks[-1] > len_side or len(matchsticks) <= 0: 
        return False
  
    def dfs(s1, s2, s3, s4, i):
        if i == len(matchsticks):
            if s1==s2==s3==s4:
                return True
            return False
        m = matchsticks[i]
        if s1+m <= len_side and dfs(s1+m, s2, s3, s4, i+1):
            return True
        if s2+m <= len_side and dfs(s1, s2+m, s3, s4, i+1):
            return True
        if s3+m <= len_side and dfs(s1, s2, s3+m, s4, i+1):
            return True
        if s4+m <= len_side and dfs(s1, s2, s3, s4+m, i+1):
            return True
        return False
    
    return dfs(0,0,0,0,0)