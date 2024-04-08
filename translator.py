#first we get the text from the user and store it in variable ins
ins=input("Insert text: ")
#then, we send variable ins through a very brief series of 5 vowel changes.
#note, this cipher will not change capital letters. this is by design, as it allows some leeway to an experienced user.
ins=ins.replace("a","v") #replace all uses of a
ins=ins.replace("e","v") #replace all uses of e
ins=ins.replace("i","v") #replace all uses of i
ins=ins.replace("o","v") #replace all uses of o
ins=ins.replace("u","v") #replace all uses of u
#to the recipient, assuming they are versed in this cipher, the text is readable upon delivery. no decoding is needed, nor is it possible.
#now, we print the result. change to return for a function if necessary.
print(ins)
#the program will now quit, as it has completed it's purpose.
quit()
