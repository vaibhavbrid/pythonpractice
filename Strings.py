class Strings:
    def IsPalin(self, testStr):
        if testStr[::-1] == testStr:
            return True
        else:
            return False

    def StringWithMaxChars(self, testStr):
        if testStr is None:
            print("Please enter a string")
            return None
        if int(len(testStr)) < int(3):
            print("Please enter a longer string")
            return None
        """Use a dictionary"""
        charsMap = {}
        for char in testStr:
            if char in charsMap:
                charsMap[char] += 1
            else:
                charsMap[char] = 1
        maxCharVal = 0
        maxCharItem = None
        """Look up dictionary for items with highest values"""
        for i,v in charsMap.items():
            if v > maxCharVal:
                maxCharVal = v
                maxCharItem = i
        if maxCharVal == 1:
            print("No max chars found")
            return None
        return maxCharItem

    def FindVowelsInString(self, testStr):
        vowelsList = ['a', 'e', 'i', 'o', 'u']
        if testStr is None:
            print("Please enter a string")
            return None
        vowelsFoundCounter = 0
        for char in testStr:
            try:
                index = vowelsList.index(char)
                if index is not None:
                    vowelsFoundCounter += 1
            except ValueError as valException:
                continue
        return vowelsFoundCounter

    def AreBracketsBalanced(self, testStr):
        if testStr is None:
            return None
        isBalanced = True
        bracketsList = []
        pushList = ['(', '{', '[']
        popList = [')', '}', ']']
        bracketsDict = {'(': ')', '{': '}', '[': ']'}
        for char in testStr:
            if self.__IsCharInList(char, pushList) is False and self.__IsCharInList(char, popList) is False:
                print("Only brackets allowed in input")
                return None
            else:
                if self.__IsCharInList(char, pushList) is True:
                    bracketsList.append(char)
                if self.__IsCharInList(char, popList) is True:
                    if len(bracketsList) > 0:
                        if char != bracketsDict[bracketsList.pop()]:
                            isBalanced = False
        if len(bracketsList) > 0:
            isBalanced = False
        return isBalanced

    def __IsCharInList(self, char, list):
        isCharInList = True
        try:
            foundIndex = list.index(char)
        except:
            isCharInList = False
        return isCharInList






