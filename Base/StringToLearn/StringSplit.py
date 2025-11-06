str1 = "To Be Or Not To Be,That's A Question"
newStr = str1.split("Be")
newStr1 = str1.split("Be",1)
print(newStr)#['To ', ' Or Not To ', ",That's A Question"]
print(newStr1)#['To ', " Or Not To Be,That's A Question"]
