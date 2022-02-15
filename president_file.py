first_name = input ("Enter a first name: ")
found_flag = False
infile = open("USPres.txt", 'r')
for line in infile:
    if line.startswith(first_name + ' '):
        print (line.rstrip ())
        found_flag = True
if not found_flag:
    print ("No president had the first name, first_name + '.' ")