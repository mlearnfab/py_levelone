f = open("data/authors.txt", "r")

#for line in f:
    #print(line)

#f.close()



authors = []
for author in f:
    authors.append(author.strip())
print(authors)


f.close()






    