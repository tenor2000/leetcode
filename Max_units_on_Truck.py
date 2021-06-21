def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        """
        type: List[List[int]], int
        rtype: int
        """
        # sort in reverse by the [1] place
        boxTypes.sort(key = lambda x: x[1], reverse=True)    
        
        result = 0
        
        for box in boxTypes:
            if truckSize == 0:
                return result
            elif box[0] >= truckSize:
                result += truckSize*box[1]
                truckSize = 0
            elif box[0] < truckSize:
                result += box[0]*box[1]
                truckSize -= box[0]
        
        return result