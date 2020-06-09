def program1(input1):
    y =""
    y=input1[0:3]+input1[5]
    return(y[::-1])
def program2(input2):
    x=[]
    y=" "
    z=[]
    x=input2.split()
    for i in x:
        if i.lower() == "python":
            i+="s"
            z.append(i)
        else:
            z.append(i)
    for i in z:
        y+=i+" "
    return(y)




if __name__ == "__main__" :
    input1="python"
    result1 = program1(input1)
    print(result1)
    input2=input("enter any sentence")
    result2=program2(input2)
    print(result2)