import sys
input_file=sys.argv[1]

length=[]

for line in open(input_file):
    if line.startswith("Name"):
        continue
    split_line=line.split()
    length.append(int(split_line[2])-int(split_line[1]))

print(length)
