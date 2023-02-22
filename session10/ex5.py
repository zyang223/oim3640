# ex5 by Zide Feb 21,2023
def rotate_word(a,n):
    """Write a function called rotate_word that takes a string and an integer 
    as parameters, and returns a new string that contains the letters from the original string rotated by the given amount."""
    print(a)
    result=""
    for i in a:
            process=(ord(i)+n)%128
            result=result+chr(process)
    return result
        
        
a="IBM"
print(rotate_word(a,3))

#python challenge0
a=2**38
print(a)

#python challenge 1
"""since k-m o-q is increase by 2  so we would use the rotate word function to solve problem"""
b="g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

# print(rotate_word(b,2))
def pythonc2(b,n):
    """using chr and ord to translate the information from the website and get the right sentencesif there is y or z make it equal to a or b"""
    result=""
    for i in b:
        if i=="z":
           result=result+"b"
        if i=="y":
            result=result+"a"
        else:
            process=(ord(i)+n)%128
            result=result+chr(process)
    return result
c=(pythonc2(b,2))
print(c.split("'"))


