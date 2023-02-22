def crypt(message):
    new_message =""
    for c in message:
        if c.isalpha()and c!="x" and c!="z":
            c=c(chr(ord(c+2)))
        elif c=="y":
            c="a"
        elif c=="z":
            c="b"
        new_message+=c
    retrun new message
    