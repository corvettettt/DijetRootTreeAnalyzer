number = {}
non_proved = []
for k in range(1000000):
  a = str(k)
  b = 0
  while True and b <500:
    b += 1
    N = len(a)
    n = 0
    t = 0
    for i in a:
      t += int(i)*(10**n)+int(i)*(10**(N-n-1))
      n += 1
    ju = True
 
    for i in range(len(str(t))):
      ju = ju and str(t)[i]==str(t)[-i-1]
    if ju:
#      print str(k)+' is a huiwenshu, and it\'s '+str(t)+', excuted '+str(b)+' times'
      number[k]=[b]
      break
    a = str(t)
  if b == 500:
    print str(k)+' has not been proved'
    non_proved.append(k)
c = 0
ct = 0
for i in number:
    if number[i]>c:
      c = number[i]
      ct = i

print '\n\nthe largest is '+str(ct)+', excuted '+str(c)+'times'
print '\n\nthose has not : '+non_proved
