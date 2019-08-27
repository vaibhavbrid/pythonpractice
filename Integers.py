class Integers:
    def DivisionWithoutMultDivideMod(self, dividend, divisor):
        if((dividend == 0 | divisor == 0)):
            return None

        quotientCtr = 0
        while(divisor <= dividend):
            dividend = dividend - divisor
            quotientCtr += 1

        return quotientCtr


    def FindLongestSubSequenceInIntegers(self, arr):
        if len(arr) is 0:
            return None

        arrSet = set()

        arrLen = len(arr)

        for i in range(arrLen):
            arrSet.add(arr[i])

        longestSubSeqCt = 0
        i=0
        while i < arrLen:
            if arr[i]-1 not in arrSet:
                longestSubSeqTempCt = 0

                j = arr[i];
                while j in arrSet:
                    j += 1
                    longestSubSeqTempCt += 1
                    if longestSubSeqTempCt > longestSubSeqCt:
                        longestSubSeqCt = longestSubSeqTempCt
                    if j not in arrSet:
                        i += 1
            else:
                i += 1

        return longestSubSeqCt

    def FindContiguousIntegersForSum(self, arr, sum):
        if len(arr) <= 0:
            return None

        for i in arr:
            temparr = []
            temparr.append(i)
            j = arr.index(i) + 1
            tempSum = i
            while tempSum <= sum and j <= len(arr):
                tempSum += arr[j]
                temparr.append(arr[j])
                j += 1
                if tempSum == sum:
                    return temparr








