def displayMessage(string):
    "Hallo"
    def message():
        "Nested Function"
        print(string)
    message()
    
print(displayMessage("Show me nested function scope"))