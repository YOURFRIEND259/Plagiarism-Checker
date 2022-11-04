f = open("text1.txt", "r")
t1= open("text1 copy.txt", "r")
t2= open("text1 copy 2.txt", "r")
t3= open("text1 copy 3.txt", "r")
main = f.read()
test1= t1.read()
test2= t2.read()
test3= t3.read()
main_words = main.split()
test1_words = test1.split()
test2_words = test2.split()
test3_words = test3.split()

def plag_check(m,t):
    pl=0
    count=0
    # while count<=len(t):
    for i in range(len(m)):
        
        if i<=(len(t)-1) and m[i]==t[i]:
            pl+=1
            count+=1
        elif i>(len(t)-1):
            break
        else:
            count+=1
            
    print("\nnumber of plagiarism:",count)
    print(pl/count*100,"%")

plag_check(main_words,test1_words)
plag_check(main_words,test2_words)
plag_check(main_words,test3_words)
