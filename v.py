#Worldlist to wordlist with only v words, then replaces v with b
with open("w.txt") as f:
	with open("vb.txt", "w") as g:
		for line in f:
			if("v" in line):
                x = line.replace("v", "b")
				g.write(x)

#Worldlist to wordlist with only b words            
with open("w.txt") as f:
    with open("b.txt", "w") as g:
		for line in f:
			if("b" in line):
				g.write(line)
                
#compare similar words in both files                
with open("vbfim.txt", "w") as f:
    file1 = set(line.strip() for line in open('vb.txt'))
    file2 = set(line.strip() for line in open('b.txt'))
    for line in file1 & file2:
        if line:
            f.write(line)
            f.write("\n")

#remove all the verbe words
with open("vbfim.txt") as f:
	with open("vbfimtraco.txt", "w") as g:
		for line in f:
			if("-" not in line):
				g.write(line)

#sort alphabetically
with open("vbfimtraco.txt") as f:
	with open("vbfimtracosort.txt", "w") as g:
		for line in sorted(f):
			g.write(line)