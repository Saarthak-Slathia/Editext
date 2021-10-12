class String:
    string = ""

    def __init__(self, x):
        self.string = str(x)
        print(self.string)

    def uppercase(self, x):
        self.string = str(x)
        return self.string.upper()

    def uppercase(self):
        return self.string.upper()

    def lowercase(self, x):
        self.string = str(x)
        return self.string.lower()

    def lowercase(self):
        return self.string.lower()

    def capitalize(self, x):
        self.string = str(x)
        return self.string.capitalize()

    def capitalizeIt(self):
        return self.string.capitalize()

    def reverseCapitalize(self):
        firstChar = self.string[0].lower()
        return firstChar + self.string[1:].upper()

    def reverseCase(self):
        return self.string.swapcase()

    def reverseCase(self, s):
        self.string = str(s)
        return self.string.swapcase()


# Testing the String Class
myStr = String("Hello World")
up = myStr.reverseCase(23)
print(up)
