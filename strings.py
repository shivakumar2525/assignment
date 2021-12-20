#reverse the given string

'''l="wellcome shivakumar"
print(l[::-1])


#odd postion and even postion string

string = "python programing"

string_length = len(string)

for s in range(string_length):
  if s%2==0:
    print("is even ",string[s])
  else:
    print("is odd",string[s])



#Program to merge characters of 2 strings into a single string by taking characters alternatively
a="shiva"
b="kumar"
c = a + "" + b
print(c)


my_list = ['a', 'b', 'c', 'd']
my_string = ','.join(my_list)


#sort the characters of the string and first alphabet symbols followed by numeric values

string='a2b4c6'
alpha=[]
digit=[]
for c in the string:
    if c.isalpha():
        alpha.append(c)
    else:
        digit.append(c)
result=''.join(sorted(alpha)+sorted(digit))
print(result)'''




s='a4k3b2'
output=''
for ch in s:
    if ch.isalpha():
        x=ch
    else:
        d=int(ch)
        output=output+x*d

print(output)