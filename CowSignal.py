l = []
with open("cowsignal.in","U") as f:
  r = f.readlines()

string1 = ""
string2 = ""
string3 = ""
n = 0

while r[0][n] != " " and n<len(r[0])-1:
  string1 = string1+r[0][n]
  n+=1

if r[0][n] == " " and n<len(r[0])-1:
  n+=1 
  while r[0][n]!=" " and n<len(r[0])-1:
    string2 = string2+r[0][n]
    n+=1 

if r[0][n] == " " and n<len(r[0])-1:
  n+=1 
  while r[0][n]!=" " and n<len(r[0])-1:
    string3 = string3+r[0][n]
    n+=1 

l.append(int(string1))
l.append(int(string2))
l.append(int(string3))


M = l[0]
N = l[1]
K = l[2]


ml = []

line = ""
i = 1 
c = 0
f = 0
counter = 0

while i<=M:
  line = (line+r[i])
  line = line.strip("\n")
  print line
  for char in line:
    ml.append(char.strip("\r"))

  nl = list(ml)
  
  print ml 
  
  for char2 in range(len(nl)):
    while counter<K-1:
      ml.insert(char2*K,nl[char2])
      counter+=1 
    counter =0
  
  stringf = ""
  for var in ml:
    stringf = stringf + var
  
  with open("cowsignal.out","a") as w:
    while f<K:
      w.write(stringf+"\n")
      f+=1
  
  f = 0
  ml = []
  stringf = ""
  line = ""
  i+=1

