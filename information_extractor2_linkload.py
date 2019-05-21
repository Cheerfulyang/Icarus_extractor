'''
Created by Yang
'''

myfile = open(r"C:\Users\widndows7\Desktop\myresult\0512_yotube.txt","r+")

stopword = ":q"

file_content = "\n"

#print("please input content [input ' Enter + :q' to save and quit]")


res = myfile.readlines()
res2 = []

#info = "name: LCD"
info = "name: SPRC"

left = 0
right = 0
s1=list(res)
'''
print(len(s1))
print len(res)
print s1
'''
ans = []

def getnum(res, l):
    start = 0;
    end = 0
    for i in range(len(res[l])):
        if res[l][i] == ":":
            start = i+2
        if res[l][i] == "\n":
            end = i
    print res[l][start:end]
    #ret = float(res[l][start:end])
    ret = res[l][start:end]
    return ret

for line in range(len(res)):
    if info in res[line]:
        print("line %d" %(line))
        l = line + 7
        h = l + 2
        p = h + 7
        print(res[p])
        ans.append([getnum(res, l), getnum(res, h), getnum(res, p)])
        print(ans)
    
print ans
        
#print(res[l_line], res[h_line], res[p_line])


file2 = open(r"C:\Users\widndows7\Desktop\myresult\myresult.txt","r+")
file2.write("latency\n")
for i in range(len(ans)):
    if i%8 == 0:
        file2.write("\n")
    file2.write("%s\n" %(ans[i][0]))

file2.write("\n")
file2.write("\n")
file2.write("linkload\n")
for i in range(len(ans)):
    if i%8 == 0:
        file2.write("\n")
    file2.write("%s\n" %(ans[i][1]))

file2.write("\n")
file2.write("\n")
file2.write("hitrate\n")
for i in range(len(ans)):
    if i%8 == 0:
        file2.write("\n")
    file2.write("%s\n" %(ans[i][2]))



'''
for line in iter(raw_input, stopword):
    file_content = file_content + line + " "
'''    
#myfile.write("%s" % file_content)
myfile.close()