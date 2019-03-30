di = ["arya", "anish","arvind", "mazhar"]
names = ["file_", "Anish", "Aravind", "Mazhar"]
file_lines = []
k = 0
for nam1 in di:
	for i in range(1,29):
		file_lines.append(''.join([nam1, "/",names[k], str(i), '\n']))
	k = k + 1
with open("newfileids.txt", 'w')as f:
	f.writelines(file_lines)
