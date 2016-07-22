from sys import argv

file = open("output.txt", "w")

script, filename = argv

with open(filename,'r') as f:
    for line in f:
        for word in line.split():
           file.write(word+"\n") 

f.close()
file.close()


