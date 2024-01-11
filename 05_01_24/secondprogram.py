fname = input("Enter file name: ")
word=input("Enter word to be searched:")
W = 0
with open(fname, 'r') as f:
    for line in f:
        words = line.split()
        for i in words:
            if(i==word):
                W=W+1
print("Occurrences of the word:")
print(W)