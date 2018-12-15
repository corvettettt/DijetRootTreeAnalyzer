def LineFu(x1,y1,x2,y2):
   k = (y2-y1)/(x2-x1)
   a = -k*x2+y2
   def Fu(x):
     return k*x+a
   return Fu

def CurveFu(x1,y1):
  def Fu(x):
    for i in range(len(x1)-1):
      if x1[i]<=x and x<=x1[i+1]:
	Func=LineFu(x1[i],y1[i],x1[i+1],y1[i+1])
	return Func(x)
  return Fu
  
def FindPoint(x1,y1,x2,y2):
   f1=CurveFu(x1,y1)
   f2=CurveFu(x2,y2)
   accu = 0.5
   li = []
   for i in range(int((-max(min(x1),min(x2))+min(max(x1),max(x2)))/accu)):
     li.append(max(min(x1),min(x2))+i*accu)
   for i in range(len(li)-1):
     Y2_2=f2(li[i+1])
     Y1_2=f1(li[i+1])
     Y2=f2(li[i])
     Y1=f1(li[i])
     if (Y2_2-Y1_2)*(Y2-Y1) <0 :
        print (li[i+1]+li[i])/2
	print f2(li[i+1]), f2(li[i])
     if (Y2-Y1)	== 0:
        print li[i]

if __name__=='__main__':
   x=[1,2,3,4,5,6,7,8]
   y1=[4,2,4,2,4,2,4,2]
   y2=[2,4,2,4,2,4,2,4]
   FindPoint(x,y1,x,y2)
#   f=CurveFu(x,y1)
#   print f(3)  
