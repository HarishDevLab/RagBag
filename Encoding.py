abc = input("Enter Characters:")
dd = []
hjh= []
encoded=''
def encode(j):
    match j:
        case 'a':
            hjh.append(1)
            
        case 'b':
            hjh.append(2)
        #add as per your wish  
for i in abc:
    dd.append(i)
print(dd)
for j,k in enumerate(dd):
    print("The position in the list has reached:",j+1)
    encode(k)
    print("The temp list has:",hjh)

for cahr in hjh:
    encoded += str(cahr)
print("The encoded string is:",encoded)


