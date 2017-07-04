#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'yinzhuoqun'

import random
from time import sleep
#3=3...10=10,j=11,Q=12,K=13,A=14,2=15,min=16,max=17
class card(object):
	def __init__(self,name,value,color):
		self.name=name
		self.value=value
		self.color=color
	def __str__(self):
		return self.name
	__repr__ = __str__
	def __iter__(self):
		return self
	def print_card(self):
		print('%s:%s,%s'%(self.name,self.value,self.color))
	def print_value(self):
		print('%s value is %s'%(self.name,self.value))
	def print_color(self):
		print('%s color is %s'%(self.name,self.color))
	def __lt__(self, other):  
		return self.value< other.value
#大小王joker
maxKING=card('KINGmax',17,'s');minKING=card('KINGmin',16,'s')
#黑桃spade
s2=card('2s',15,'s');sA=card('As',14,'s');sK=card('Ks',13,'s')
sQ=card('Qs',12,'s');sJ=card('js',11,'s');s10=card('10s',10,'s')
s9=card('9s',9,'s');s8=card('8s',8,'s');s7=card('7s',7,'s')
s6=card('6s',6,'s');s5=card('5s',5,'s');s4=card('4s',4,'s');s3=card('3s',3,'s')
#红心heart
h2=card('2h',15,'h');hA=card('Ah',14,'h');hK=card('Kh',13,'h')
hQ=card('Qh',12,'h');hJ=card('jh',11,'h');h10=card('10h',10,'h')
h9=card('9h',9,'h');h8=card('8h',8,'h');h7=card('7h',7,'h')
h6=card('6h',6,'h');h5=card('5h',5,'h');h4=card('4h',4,'h');h3=card('3h',3,'h')
#草花club
c2=card('2c',15,'c');cA=card('Ac',14,'c');cK=card('Kc',13,'c')
cQ=card('Qc',12,'c');cJ=card('jc',11,'c');c10=card('10c',10,'c')
c9=card('9c',9,'c');c8=card('8c',8,'c');c7=card('7c',7,'c')
c6=card('6c',6,'c');c5=card('5c',5,'c');c4=card('4c',4,'c');c3=card('3c',3,'c')
#方块diamond
d2=card('2d',15,'d');dA=card('Ad',14,'d');dK=card('Kd',13,'d')
dQ=card('Qd',12,'d');dJ=card('jd',11,'d');d10=card('10d',10,'d')
d9=card('9d',9,'d');d8=card('8d',8,'d');d7=card('7d',7,'d')
d6=card('6d',6,'d');d5=card('5d',5,'d');d4=card('4d',4,'d');d3=card('3d',3,'d')

#分集合
listKing=[maxKING,minKING]
listSpade=[s2,sA,sK,sQ,sJ,s10,s9,s8,s7,s6,s5,s4,s3]
listHeart=[h2,hA,hK,hQ,hJ,h10,h9,h8,h7,h6,h5,h4,h3]
listClub=[c2,cA,cK,cQ,cJ,c10,c9,c8,c7,c6,c5,c4,c3]
listDiamond=[d2,dA,dK,dQ,dJ,d10,d9,d8,d7,d6,d5,d4,d3]
#一副牌
listCards=listKing+listSpade+listHeart+listClub+listDiamond

x0=card('0b',0,'b')
x0.print_card()

for x in range(1,4):
	print(u'第%s次洗牌...'%x)
	random.shuffle(listCards)
	print(listCards)
	sleep(0.5)
zhangsan=[]#张三
lisi=[]#李四
wangwu=[]#王五
cardsAcount=len(listCards)#一副牌的数量
dealTimes=int(cardsAcount/3-1)#发牌次数
print(u'盒子里一共有%s张牌。现在开始发牌...'%cardsAcount)
for c in range(1,dealTimes+1):
	print(u'第%s轮发牌:'%c)
	p=random.choice(listCards)
	zhangsan.append(p)
	print(u'张三拿到%s'%p)
	listCards.pop(listCards.index(p))
	sleep(0.5)
	p=random.choice(listCards)
	lisi.append(p)
	print(u'李四拿到%s'%p)
	listCards.pop(listCards.index(p))
	sleep(0.5)
	p=random.choice(listCards)
	wangwu.append(p)
	print(u'王五拿到%s'%p)
	listCards.pop(listCards.index(p))
	sleep(0.5)
print(u'底牌有%s张，分别是%s'%(len(listCards),listCards))
print(u'张三的牌现在是：',zhangsan)
print(u'李四的牌现在是：',lisi)
print(u'王五的牌现在是：',wangwu)
chupai1=[]
chupai2=[]

print(u'张三摆牌中...')
zhangsan.sort()
sleep(0.5)
print(u'张三的牌现在是：',zhangsan)

print(u'李四摆牌中...')
lisi.sort()
sleep(0.5)
print(u'李四的牌现在是：',lisi)

print(u'王五摆牌中...')
wangwu.sort()
sleep(0.5)
print(u'王五的牌现在是：',wangwu)

###

print(u'---张三请出牌---')
p=zhangsan.pop(0)
chupai1=p
sleep(0.5)
print(u'张三出牌%s'%p)

print(u'张三的牌现在是：',zhangsan)
sleep(0.5)
while 1:
	print(u'---李四请出牌---')
	sleep(0.5)
	for cp in lisi:
		if cp.value>p.value:
			#print('cp:%s p:%s'%(cp.value,p.value))
			lisi.pop(lisi.index(cp))
			print(u'李四出牌%s'%cp)
			print(u'李四的牌现在是：',lisi)
			p=cp
			si=1
			break		
		else:
			print(u'李四不出牌。')
			si=0
	print(u'---王五请出牌---')
	sleep(0.5)
	for cp in wangwu:
		if cp.value>p.value:
			#print('cp:%s p:%s'%(cp.value,p.value))
			wangwu.pop(wangwu.index(cp))
			print(u'王五出牌%s'%cp)
			print(u'王五的牌现在是：',wangwu)
			p=cp
			wu=1
			break
		else:
			print(u'王五不出牌。')
			wu=0
	print(u'---张三请出牌---')
	for cp in zhangsan:
		if cp.value>p.value:
			#print('cp:%s p:%s'%(cp.value,p.value))
			zhangsan.pop(zhangsan.index(cp))
			print(u'张三出牌%s'%cp)
			print(u'张三的牌现在是：',zhangsan)
			p=cp
			san=1
			break
		else:
			print(u'张三不出牌。')
			san=0
	if si==0 and wu==0:
		for cp in zhangsan:
			#print('cp:%s p:%s'%(cp.value,p.value))
			zhangsan.pop(0)
			print(u'张三出牌%s'%cp)
			print(u'张三的牌现在是：',zhangsan)
			p=cp
			san=1
			break
	if wu==0 and san==0:
		for cp in lisi:
			#print('cp:%s p:%s'%(cp.value,p.value))
			lisi.pop(0)
			print(u'李四出牌%s'%cp)
			print(u'李四的牌现在是：',lisi)
			p=cp
			si=1
			break
	if san==0 and si==0:
		for cp in wangwu:			
			#print('cp:%s p:%s'%(cp.value,p.value))
			wangwu.pop(0)
			print(u'王五出牌%s'%cp)
			print(u'王五的牌现在是：',wangwu)
			p=cp
			wu=1
			break
	if len(zhangsan)==0 or len(lisi)==0 or len(wangwu)==0:
		break




