print("")
print("Backup and Restore AS400 objects")
print("================================")
print("")
print(" 1. Get MBRLST.MBR      GET")
print(" 2. AS400 --> Pc        GET")
print(" 3. PC -->              PUT")
print("99. Exit")
mbrList = " "
i = 0
while i == 0:
    opt = input("Enter (1-3) or 99? : ")
    if opt == "99":
        i = 1
    elif opt == "1":
        outFile = "getSrcFile.txt"
        i = 1
        type = "get"
        mbrList = "Y"
    elif opt == "2":
        outFile = "getSrcFile.txt"
        i = 1
        type = "get"
    elif opt == "3":
        i = 1
        outFile = "putSrcFile.txt"
        type = "put"
    else:
        i = 0
        print("Invalid option Selected :" + opt)
# -----------------------------------------------------
print("")
print("Userid and Passwrd")
print("==================")
print("")
print(" 1. Userid : RANJITHJ    Passwrd : Ab$xxxxxx")
print(" 2. Userid : USER0174    Passwrd : user0174")
print("99. Exit")
i = 0
while i == 0:
    opt = input("Enter (1-2) or 99? : ")

    if opt == "99":
        i = 1
    elif opt == "1":
        i = 1
        usrid = "RANJITHJ"
        paswrd = "Ab$499404"
    elif opt == "2":
        i = 2
        usrid = "USER0174"
        paswrd = "user0174"
    else:
        i = 0
        print("Invalid option Selected :" + opt)
# -----------------------------------------------------
print("")
print("Select Library to Backup or Restore")
print("====================================")
print("")
print(" 1. Library : " + usrid + "1")
print("99. Exit")
i = 0
while i == 0:
    opt = input("Enter (1) or 99? : ")
    if opt == "99":
        i = 1
    elif opt == "1":
        i = 1
        lib = usrid + "1"
    else:
        i = 0
        print("Invalid option Selected :" + opt)
# -----------------------------------------------------
print("")
print("Select Pc Sourcrfile to Backup or Restore")
print("=========================================")
print("")
print(" 1. Sourcrfile : R4NSI73TST")
print("99. Exit")
i = 0
while i == 0:
    opt = input("Enter (1) or 99? : ")
    if opt == "99":
        i = 1
    elif opt == "1":
        i = 1
        srcFile = "R4NSI73TST"
    else:
        i = 0
        print("Invalid option Selected :" + opt)

# -----------------------------------------------------
print("You have selected :")
print("Backup or Restore : " + type)
print("Userid : " + usrid)
print("paswrd : " + paswrd)
print("Library : " + lib)
print("Sourcrfile : " + srcFile)
print("")
print("")
print("Confirm Sourcrfile to Backup or Restore")
print("====================================")
print("")
i = 0
while i == 0:
    opt = input("Confirm Y/N ? : ")
    if opt == "N" or opt == "n":
        print("Process halted by user")
        i = 1
    elif opt == "Y" or opt == "y":
        i = 1
        confirm = "Y"
    else:
        i = 0
        print("Invalid option Selected :" + opt)

if confirm == "Y":
    quote = '"'
    f1 = open(outFile, "w")
    f1.write(usrid)
    f1.write("\n")
    f1.write(paswrd)
    f1.write("\n")
    f1.write("cd " + quote + "/QSYS.LIB/" + lib + ".LIB/" + srcFile + ".FILE" + quote)
    f1.write("\n")
    f1.write("lcd " + quote + "C:\\Users\\Public\\PUBLIC.PREVIOUS\\Public\\MY\\Pub400\\As400BackupRestore\\" + srcFile + quote)
    f1.write("\n")
    if mbrList == "Y":
        f1.write("get MBRLST.MBR")
    else:
        f = open("mbrlst.txt", "r")
        for line in f:
            mbrname = line[0:10]
            mbrtype = line[11:20]
            if not mbrtype.strip():
                mbrtype = "MBR"
            mbrdiscrpt = line[22:99]
            # f1.write(type +" " + mbrname.strip() + "." + mbrtype.strip())
            f1.write(type + " " + mbrname.strip() + ".MBR")
            f1.write("\n")
            # f1.write(mbrdiscrpt)
            # f1.write("\n")
        f.close
    f1.close

# if mbrList == "Y":
# from subprocess import check_output
# result = check_output("copy C:\Users\ranjithj\Documents\AS400\BackupToPc\MBRLST.MBR", shell=True).decode()
# print(result)

print("")
print(outFile + " created. . . ")
