class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        index = len(digits)-1
        value = 1
        while index >= 0:
            if value == 1:
                digits[index] += 1
                if digits[index] == 10:
                    digits[index] = 0
                    index -= 1
                    continue
            value = 0
            break
        else:
            if value == 1:
                return [1]+digits
        return digits