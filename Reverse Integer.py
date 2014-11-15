class Solution:
    # @return an integer
    def reverse(self, x):
        if x == 0:
            return 0
        elif x < 0:
            x = -x
            sign = -1
        else:
            sign = 1

        numList = []
        newX = x
        while newX != 0:
            (num, newX) = (x%10, x/10) 
            x = newX
            numList.append(num)

        power = len(numList)-1
        index = 0
        reverseNum = 0
        while (index<=power):
            reverseNum += numList[index]*10**(power-index)
            index+=1
        reverseNum *= sign
        if reverseNum < -2147483648 or reverseNum > 2147483647:
            return 0
        else:
            return reverseNum