def lb_to_kg(input1):
    output=[]
    for i in range(0,len(input1)):
        i = round((float(input1[i])*(0.453592)),2)
        output.append(i)
    return output

def string_alternative(input2):
    x=[]
    y=''
    for i in input2:
        x.append(i)
    for i in range (0,len(x)):
        if i%2 ==0:
            y+=x[i]
    return(y)

def file_prog():
    file1= open("input_file.txt","r")
    if file1.mode =="r":
        sentence = file1.read()
        words=sentence.split("\n")
        k=[]
        for i in words:
            z=[]
            z=i.split()
            for j in z:
                k.append(j)
        final_list=[]
        for i in k:
            counter1 = 0
            for j in k :
                if i == j and i not in final_list :
                    counter1+=1
            if i not in final_list:
               final_list.append(i)
            if i in final_list and counter1 !=0:
                print(i,counter1)

















if __name__ == "__main__" :
    lines = []
    while True:
        line = input("enter weight in lbs: ")
        if line:
            lines.append(line)
        else:
            break
    result1 = lb_to_kg(lines)
    print(result1)
    input2=input("enter string: ")
    result2 = string_alternative(input2)
    print(result2)
    file_prog()
