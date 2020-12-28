# """1. Viết chương trình vẽ hình tam giác đặc bằng số – Bài 1"""
# n = 5
# for i in range(1, n+5, 2):
#     for j in range(i, n+1):
#         print(j*(str(i)))

# class People:
# 	name: str
# 	old: int
# 	birthday: str
# 	dspp = []
# 	def enterPeople(self):
# 		for i in range(2):
# 			self.name = input('Enter your name: ')
# 			self.old = int(input('Enter your old: '))
# 			self.birthday = input('Enter your birthday (dd/mm/yy): ')
# 			self.dspp.append([self.name, self.old, self.birthday])
# 	def printPeople(self):
# 		for i in range(len(self.dspp)):
# 			print('Name: {}'.format(self.dspp[i][0]))
# 			print('Old: {}'.format(self.dspp[i][1]))
# 			print('Birthday: {}'.format(self.dspp[i][2]))
	
# if __name__=='__main__':
# 	p = People()
# 	p.enterPeople()
# 	p.printPeople()

l = [str(x+1) for x in range(1427)]
print((" ").join(l))
