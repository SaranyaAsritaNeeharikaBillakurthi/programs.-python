##addition operator:

##a=int(input('enter a number'))
##b=int(input('enter a number'))
##print(type(a),type(b),a+b)

##a=input('enter a number')
##b=input('enter a number')
##print(type(a),type(b),a,b,a+b)

##a=int(a)
##b=int(b)
##print(type(a),type(b),a,b,a+b)

##a=float(a)
##b=float(b)
##print(type(a),type(b),a,b,a+b)

##if else:

##p=float(input('enter percrntage'))
##bl=int(input('enter number of backlogs'))
##if p>=60 and bl==0:
##	print(eligible)
##else:
##	print('not eligible')

##elif:

##m=int(input('enter a marks'))
##if m>=80:
##	print('A grade')
##elif m>=60 and m<80:
##	print('B grade')
##elif m>=40 and m<60:
##	print(' C grade')
##else:
##	print('Failed')

##mailid and password:

##mid ="thub@gmail.com"
##ipw='1234'
##umid=input('enter a mailid')
##upwd=input('enter password')
##if mid==umid and ipw==upwd:
##	print('login successfully')
##else:
##	print('wrong credentials')

##for loop:

##for i in range(10):
##	print(i)

##a=int(input('enter a starting range'))
##b=int(input('entet a ending range'))
##for i in range(a,b+1):
##	print(i)

##increment operator:

##for i in range(5,20,2):
##	print(i)

##for i in range(25,36,+1):
##	print(i)

##decrement operator:

##for i in range(9,0,-1):
##	print(i)

##for i in range(35,24,-1):
##	print(i)

#to print tables:

##s=int(input('enter a starting number'))
##e=int(input('enter a ending number'))
##b=int(input('enter a number'))
##for n in range(s,e+1):
##	print(n,'*',b,'=',n*b)

##to print any table in the given range for increment and decrement:

##s=int(input('enter a starting number'))
##e=int(input('enter a ending number'))
##b=int(input('enter a number'))
##if s<=e:
##	for n in range(s,e+1):
##		print(n,'*',b,'=',n*b)
##else:
##	for n in range(s,e-1,-1):
##		print(n,'*',b,'=',n*b)

##to print only odd number table:

##s=int(input('enter a starting number'))
##e=int(input('enter a ending number'))
##b=int(input('enter a number'))
##for n in range(s,e+1,2):
##	print(n,'*',b,'=',n*b)

##s=int(input('enter a starting number'))
##e=int(input('enter a ending number'))
##b=int(input('enter a number'))
##for n in range(s,e+1):
##	if n%2==1:
##		print(n,'*',b,'=',n*b)

##even if n%2==0

 ##to print sum of numbers:

##s=0
##for i in range(5,16):
##	s+=i
##	print(s)
##print('total sum',s)

##to print numbers in the range dovisible by 3:

##s=0
##for n in range(1,11):
##	if n%3==0:
##		print(n)

##i=0 
##for i in range(0,(i<=100),1):
##		print(i)

##for i in range(1,11):
##		i+=2
##		print(i)

##for i in range(1,11):
##		print(i)
##		i+=2

##while loop:

##to print good morning for 5 times:

##i=0
##while True:
##		print('good morning')
##		i+=1
##		if i==5:
##			break

##increment

##i=0
##while True:
##	i+=1
##	print(i)
##	if i==10:
##		break

##i=0
##while i<=10:
##	i+=1
##	print(i)

##decrement:

##i=0
##while True:
##	print(i)          INFINITE LOOP
##	i-=1

##i=10
##while True:
##	print(i)
##	i-=1
##	if i==0:
##		break

##i=10
##while i>=1:
##	print(i)
##	i-=1

##i=10
##while not(i<1):
##	print(i)
##	i-=1

##Break:  

##for i in range(1,11):
##	if i==5:
##		break
##	print(i)
##print('loop is done')

##for i in range(1,11):
##	print(i)
##	if i==5:
##		break
##print('loop is done')

##continue:

##for i in range(1,11):
##	if i==5:
##		continue
##	print(i)
##print('loop is done')

##i=0
##while i<10:
##	i+=1
##	if i%2==0:
##		continue
##	print(i)

##i=0
##while i<10:
##	i+=1
##	if i%2!=0:
##		continue
##	print(i)

##else:

##for i in range(5):
##	print(i)
##else:
##	print('done')

##mailid and password using loops:   

##mid ="thub@gmail.com"
##ipw='1234'

##for i in range(5):
##	umid=input('enter a mailid')
##	upwd=input('enter password')
##	if mid==umid and ipw==upwd:
##		print('login successfully')
##	else:
##		print('wrong credentials')

##

##mid ="thub@gmail.com"
##ipw='1234'

##for i in range(5):
##	umid=input('enter a mailid')
##	upwd=input('enter password')
##	if mid==umid and ipw==upwd:
##		print('login successfully')
##	else:
##		print('wrong credentials')
##else:
##	print('account blocked')

##

##mid ="thub@gmail.com"
##ipw='1234'

##for i in range(3):
##	umid=input('enter a mailid')
##	upwd=input('enter password')
##	if mid==umid and ipw==upwd:
##		print('login successfully')
##	else:
##		print('wrong credentials')
##else:
##	print('account blocked')
##print('all are done')


