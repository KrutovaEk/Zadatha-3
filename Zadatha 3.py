with open("1.txt", encoding='utf-8') as fp:
    count_1 = 0
    for line in fp:
        count_1 += 1
# print(count_1)

with open("2.txt", encoding='utf-8') as fp:
    count_2 = 0
    for line in fp:
        count_2 += 1
# print(count_2)

with open("3.txt", encoding='utf-8') as fp:
    count_3 = 0
    for line in fp:
        count_3 += 1
# print(count_3)

a = min(count_1, count_2, count_3)
c = max(count_1, count_2, count_3)
b = (count_1+count_2+count_3)-(a+c)

# print(a)
# print(b)
# print(c)

if count_1==a:
    if count_2==b:
        mintxt=("1.txt")
        srtxt=("2.txt")
        maxtxt=("3.txt")
    else:
        mintxt=("1.txt")
        srtxt=("3.txt")
        maxtxt=("2.txt")
 
elif count_2==a:
    if count_1==b:
        mintxt=("2.txt")
        srtxt=("1.txt")
        maxtxt=("3.txt")
    else:
        mintxt=("2.txt")
        srtxt=("3.txt")
        maxtxt=("1.txt")

elif count_3==a:
    if count_1==b:
        mintxt=("3.txt")
        srtxt=("1.txt")
        maxtxt=("2.txt")
    else:
        mintxt=("3.txt")
        srtxt=("2.txt")
        maxtxt=("1.txt")

# print(mintxt, spttxt, maxtxt)

a_1=str(a)
b_1=str(b)
c_1=str(c)
with open('new.txt', 'a', encoding='utf-8') as n_f:
         n_f.write(mintxt)
         n_f.write('\n')
         n_f.write(a_1)
         n_f.write('\n') 

with open(mintxt, 'r', encoding='utf-8') as f1, open('new.txt', 'a', encoding='utf-8') as temp:
    temp.write(f1.read())
    temp.write('\n')

with open('new.txt', 'a', encoding='utf-8') as n_f:
         n_f.write(srtxt)
         n_f.write('\n')
         n_f.write(b_1)
         n_f.write('\n') 

with open(srtxt, 'r', encoding='utf-8') as f2, open('new.txt', 'a', encoding='utf-8') as temp_2:
    temp_2.write(f2.read())
    temp_2.write('\n')

with open('new.txt', 'a', encoding='utf-8') as n_f:
         n_f.write(maxtxt)
         n_f.write('\n')
         n_f.write(c_1)
         n_f.write('\n') 

with open(maxtxt, 'r', encoding='utf-8') as f3, open('new.txt', 'a', encoding='utf-8') as temp_3:
    temp_3.write(f3.read())
    
with open('new.txt', 'r', encoding='utf-8') as n_f:
     print(n_f.read())
    