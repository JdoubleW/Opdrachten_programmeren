invoer = '1;test\n'
infile = open("kluizen", 'r')
linelist = infile.readlines()
for waarde in linelist:
    split_lijst = print(waarde.split(';'))
    split_invoer = print(invoer.split(';'))
    split = print(linelist.index(invoer))
    if invoer == split_lijst:
        print("Toegang verleend")

    else:
        print( "Toegang geweigerd")

