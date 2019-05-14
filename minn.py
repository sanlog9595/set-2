Minutes=int(input())
hours=minutes//60
if(hours==0):
  Minutess=minutes
else:
  Minutess=minutes%60
print(hours,minutes)
