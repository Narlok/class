import os

def readessentials(filename):
    file=open(filename,"r")
    data=file.read()
    file.close()
    data=str(data)
    terms=data.splitlines()
    return terms

def rename(terms,i):   #Removes / since fucks with renaming
    names=[]
    for i in range(i,i-2,-1):
        if "/" in terms[i]:
            temp=list(terms[i])
            for i,x in enumerate(temp):
                if x is "/":
                    temp[i]="div"
            names.append(''.join(temp))
        else:
            names.append(terms[i])

    os.system("mv " + names[1]+".ini " + names[0] + ".ini") #Renames to know which output is which
    os.system("./class "+ names[0] + ".ini")



def editfile(filename,filename2, terms,l1,l2,l3):
    file=open(filename,"r")
    data=file.read()
    file.close()
    data=str(data)
    lines=data.splitlines()
    for i,x in enumerate(terms):

        if i>=1:
            lines[int(l1)-1]=lines[int(l1)-1][:-((len(terms[i-1]))+2)] + "+" + x + ";"
            lines[int(l2)-1]=lines[int(l2)-1][:-((len(terms[i-1]))+2)] + "+" + x + ";"
#            print(lines[int(l2)-1])
            lines[int(l3)-1]=lines[int(l3)-1][:-((len(terms[i-1]))+2)] + "+" + x + ";"
#            print(lines[int(l3)-1])
            file=open(filename2,"w+")
            for line in lines:
                file.write(line +"\n")
            file.close()
            os.system("make")
            #os.system("mv " + terms[i-1]+".ini " + x + ".ini") #Renames to know which output is which
            #os.system("./class "+ x + ".ini")
            rename(terms,i)
            #print(terms[i-1]+".ini "+x+".ini")

        else:  #Set same initial conditions for line 1
            lines[int(l1)-1]+=terms[i]+"+"
            lines[int(l2)-1]+=terms[i]+"+"
            lines[int(l3)-1]+=terms[i]+"+"
            os.system("mv explanatory.ini " + terms[i]+".ini")

    os.system("mv " + terms[len(terms)-1] +".ini explanatory.ini")  #Return to original state


terms=readessentials("edit.dat")
editfile("source/perturb_orig.c","source/perturbations.c",terms,"5164","5167","5576")
