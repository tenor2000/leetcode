
def generate(numRows):
    """
    type: int
    rtype: List[List[int]]
    """
    if numRows == 0:
        return []
    if numRows == 1:
        return [[1]]
    
    result = [[1],[1,1]]
    
    for row in range(2, numRows):
        result.append([1]) 
        for i in range(1,len(result[row-1])):
            temp = result[row-1][i]+ result[row-1][i-1]
            result[row].append(temp)
        result[row].append(1)
        
    return result