'''
Created by Yang
'''

myfile = open(r"C:\Users\widndows7\Desktop\myresult\test.txt","r+")

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
print res[2]
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
        h = l + 4
        p = h + 4
        print(res[p])
        ans.append([getnum(res, l), getnum(res, h), getnum(res, p)])
        print(ans)
    
print ans
        
#print(res[l_line], res[h_line], res[p_line])


file2 = open(r"C:\Users\widndows7\Desktop\myresult\myresult.txt","r+")

file2.write("LATENCY\n")
for i in range(len(ans)):
    if i%8 == 0:
        file2.write("\n")
    file2.write("%s\n" %(ans[i][0]))

file2.write("\n")
file2.write("CACHE_HIT_RATIO\n")
  
for i in range(len(ans)):
    if i%8 == 0:
        file2.write("\n")
    file2.write("%s\n" %(ans[i][1]))

file2.write("\n")
file2.write("PATH_STRETCH\n")

for i in range(len(ans)):
    if i%8 == 0:
        file2.write("\n")
    file2.write("%s\n" %(ans[i][2]))


myfile.close()