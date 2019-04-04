class Solution(object):

    #faster solution is to use bit manipulation (DUH)
    def hammingDistance(self, x, y):
        """
        type x: int
        type y: int
        rtype: int
        """
        #delcare list variables
        listX, listY = [], [];
        hammingDistanceCount, diff, xLength, yLength = 0, 0, 0, 0;

        #convert from decimal to binary. output has prefix '0b'
        listX += bin(x);
        listY += bin(y);

        #remove '0b' from beginning of list
        listX = listX[2:];
        listY = listY[2:];

        #get length of lists
        xLength = len(listX);
        yLength = len(listY);

        #get difference between length of lists
        diff = abs(xLength - yLength);

        #check which number is bigger, x or y
        if(xLength >= yLength):
            #iterate backwards through list using list index; xLength-1 because list indices start from 0
            for i in range(xLength-1,-1,-1):
                if((i-diff) >= 0):
                    if(listX[i] != listY[i-diff]):
                        hammingDistanceCount += 1;
                elif(int(listX[i]) == 1):
                    hammingDistanceCount += 1;
        else:
            for i in range(yLength-1,-1,-1):
                if((i-diff) >= 0):
                    if(listY[i] != listX[i-diff]): 
                        hammingDistanceCount += 1;
                elif(int(listY[i]) == 1):
                        hammingDistanceCount += 1;

        return hammingDistanceCount;

    def singleNumber(self, nums):
        


#Solution().hammingDistance(1,4);