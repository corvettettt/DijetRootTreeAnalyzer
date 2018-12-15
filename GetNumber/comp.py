class event(object):
  def __init__(self,eta1,eta2,deltaeta,pt1,pt2,run,event,mjj):
    self.eta1 = eta1
    self.eta2 = eta2
    self.delta = deltaeta
    self.event = event
    self.run = run
    self.mjj = mjj
    self.pt2 = pt2
    self.pt1 = pt1

fin1 = open('Mine.txt')
fin2 = open('GMagda.txt')
Mag  = []
Min  = []
for i in fin1.readlines():
  Min.append([float(i.split('\t')[0]),float(i.split('\t')[1])])
for i in fin2.readlines():
  Mag.append([float(i.split('\t')[0]),float(i.split('\t')[1])])

diff = []
print 'Min'
for i in Min:
  if not i in Mag:
    print i
    diff.append(i)

print diff
print 'Mag'
for i in Mag:
  if not i in Min:
    print i

for i in fin1.readlines():
  if [int(i.split('\t')[0]),int(i.split('\t')[1])] in diff:
    print i
