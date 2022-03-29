import cv2 
import numpy as np 
import matplotlib.pyplot as plt

b=[]
c=[]
d=[]
m=0
n=0
row=0
colm=0
count=0

img_rgb = cv2.imread('testimage2.jpeg')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
temp1 = cv2.imread('plus.jpeg',0)
temp2 = cv2.imread('minus.jpeg',0)
temp3 = cv2.imread('intersections.jpeg',0)

w1,h1 = temp1.shape[::-1]
w2,h2 = temp2.shape[::-1]
w3,h3 = temp3.shape[::-1]

# Perform match operations. 
res1 = cv2.matchTemplate(img_gray,temp1,cv2.TM_CCOEFF_NORMED) 
threshold = 0.8
loc1 = np.where( res1 >= threshold)   
for pt in zip(*loc1[::-1]): 
    cv2.rectangle(img_rgb, pt, (pt[0] + w1, pt[1] + h1), (0,255,0), 2) 
    b.append(pt)

 
res2 = cv2.matchTemplate(img_gray,temp2,cv2.TM_CCOEFF_NORMED)  
threshold = 0.8
loc2 = np.where( res2 >= threshold)  
for pt1 in zip(*loc2[::-1]): 
    cv2.rectangle(img_rgb, pt1, (pt1[0] + w2, pt1[1] + h2), (0,0,255), 2) 
    c.append(pt1)


result = cv2.matchTemplate(img_gray,temp3,cv2.TM_CCOEFF_NORMED) 
threshold = 0.8
loc3 = np.where( result >= threshold)   
for pt2 in zip(*loc3[::-1]): 
    cv2.rectangle(img_rgb, pt2, (pt2[0] + w3, pt2[1] + h3), (255,0,0), 2)
    d.append(pt2)

num_of_intersections= len(d)
b.sort()
c.sort()
d.sort()

for i in range (0, num_of_intersections):
	if d[0][0]==d[i][0]:
		m+=1
n=int(num_of_intersections/m+1)
m=m+1
n=n+1
cv2.imshow('abcd',img_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()
#m is no of rows and n is no of columns

h=d[1][1]-d[0][1]
w=d[m][0]-d[0][0]

array=[]
array=[[0]*n for r in range(m)]
total=0
#for plus
for i in range(0, len(b)):
	colm=int(b[i][0]/w)
	row=int(b[i][1]/h)
	array[row][colm]=2
	total=total+1

#for minus
for i in range(0, len(c)):
	colm1=int(c[i][0]/w)
	row1=int(c[i][1]/h)
	array[row1][colm1]=-2

def pathtrace(p1,q1,p2,q2): 
	p=[-p1,-p2]
	q=[q1,q2]
	plt.plot(q,p,color='r',label='path')

def where(x,y,a,b):
	#down then up then right then left
	global count
	if a<m-1 and array[a+1][b]==2:
		count=count+1
		array[a+1][b]=-2
		pathtrace(a+0.5,b+0.5,a+1.5,b+0.5)
		where(a,b,a+1,b)
	if a>0 and array[a-1][b]==2:
		count=count+1
		array[a-1][b]=-2
		pathtrace(a+0.5,b+0.5,a-0.5,b+0.5)
		where(a,b,a-1,b)
	if b<n-1 and array[a][b+1]==2:
		count=count+1
		array[a][b+1]=-2
		pathtrace(a+0.5,b+0.5,a+0.5,b+1.5)
		where(a,b,a,b+1)
	if b>0 and array[a][b-1]==2:
		count=count+1
		array[a][b-1]=-2
		pathtrace(a+0.5,b+0.5,a+0.5,b-0.5)
		where(a,b,a,b-1)
	if a<m-1 and array[a+1][b]==0:
		array[a+1][b]=-2
		pathtrace(a+0.5,b+0.5,a+1.5,b+0.5)
		where(a,b,a+1,b)
	if a>0 and array[a-1][b]==0:
		array[a-1][b]=-2
		pathtrace(a+0.5,b+0.5,a-0.5,b+0.5)
		where(a,b,a-1,b)
	if b<n-1 and array[a][b+1]==0:
		array[a][b+1]=-2
		pathtrace(a+0.5,b+0.5,a+0.5,b+1.5)
		where(a,b,a,b+1)
	if b>0 and array[a][b-1]==0:
		array[a][b-1]=-2
		pathtrace(a+0.5,b+0.5,a+0.5,b-0.5)
		where(a,b,a,b-1)

#start from (0,0)
a=0
b=0
if array[0][0]==-2:
	print(-1)
	quit()
elif array[0][0]==2:
	count=count+1
	array[0][0]=-2
elif array[0][0]==0:
	array[0][0]=-2
#down then right
if array[1][0]==2:
	count=count+1
	array[1][0]=-2
	pathtrace(a+0.5,b+0.5,a+1.5,b+0.5)
	where(0,0,1,0)
elif array[0][1]==2:
	count=count+1
	array[0][1]=-2
	pathtrace(a+0.5,b+0.5,a+0.5,b+1.5)
	where(0,0,0,1)
elif array[1][0]==0:
	count=count+1
	array[1][0]=-2
	pathtrace(a+0.5,b+0.5,a+1.5,b+0.5)
	where(0,0,1,0)
elif array[0][1]==0:
	count=count+1
	array[0][1]=-2
	pathtrace(a+0.5,b+0.5,a+0.5,b+1.5)
	where(0,0,0,1)

print ("total",total)
print ("Collected",count)
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()