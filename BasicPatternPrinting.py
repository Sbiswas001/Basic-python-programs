#Basic Pattern Printing  in Python (with while loop)

#1.Pointing at top-right
print("Pointing at top-right")
i=1
while(i<=5):
  j=1
  while(j<=5):
     if(i<=j):
      print('*',end=' ')
     else:
      print(end='  ')
     j=j+ 1
  print()
  i=i+1

print()
print("="*50 +"\n")

#2.Pointing at bottom-left
print("Pointing at bottom-left")
i=1
while(i<=5):
  j=1
  while(j<=5):
     if(i>=j):
      print('*',end=' ')
     else:
      print(end='  ')
     j=j+ 1
  print()
  i=i+1

print("\n")
print("="*50 +"\n"*2)

#3.Pointing at bottom-right
print("Pointing at bottom-right")
i=1
while(i<=5):
  j=1
  while(j<=5):
     if(i+j>=6):
      print('*',end=' ')
     else:
      print(end='  ')
     j=j+ 1
  print()
  i=i+1

print("\n")
print("="*50 +"\n"*2)

#4.Pointing at top-left
print("Pointing at top-left")

i=1
while(i<=5):
  j=1
  while(j<=5):
     if(i+j<=6):
      print('*',end=' ')
     else:
      print(end='  ')
     j=j+ 1
  print()
  i=i+1

print("\n")
print("="*50 +"\n"*2)

#Combined pattern
print("Combined pattern")

i=  1 
while(i<=5):
  j=1
  while(j<=5):
    if(i<=j):
      print('*',end=' ')
    else:
      print(end='  ')
    j+= 1
  k=1
  while(k<=5):
    if(i+k>=6):
      print('*',end=' ')
    else:
      print(end='  ')
    k+= 1
  
  print()
  i+= 1 
i=  1 
while(i<=5):
  j=1
  while(j<=5):
    if(i+j<=6):
      print('*',end=' ')
    else:
      print(end='  ')
    j+= 1
  k=1
  while(k<=5):
    if(i>=k):
      print('*',end=' ')
    else:
      print(end='  ')
    k+= 1
  
  print()
  i+= 1
