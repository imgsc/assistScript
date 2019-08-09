'''
Listen to me 

What's your poker life？

Please put your birthday 

and you can see your life...

'''
import datetime,time

def getPoker(str):
	
	t=time.strptime(str,'%Y-%m-%d')
	y,m,d = t[0:3]
	#print (datetime.datetime(y,m,d))
	
	pokerNumber = ['Ace','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King']
	pokerColor  = ['Spades','Hearts','Diamonds','Clubs']

	birthday = datetime.date(y, m, d).isocalendar()
	year,week,day = birthday[0:3]

	birthNumber = week//4
	birthColor = week%4-1

	return y,m,d,pokerNumber[birthNumber],pokerColor[birthColor]

if __name__ == '__main__':
	str = input("Enter your birthday(yyyy-mm-dd): ")
	y,m,d,pokerNumber,pokerColor = getPoker(str)[0:5]
	print('Birthday :'+datetime.date(y, m, d).strftime('%Y-%m-%d'))
	print('Poker : the '+pokerNumber+' of '+pokerColor)
