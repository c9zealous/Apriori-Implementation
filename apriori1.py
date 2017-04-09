import sys
from itertools import combinations
import pandas as pd
file_name=sys.argv[1]
min_support=float(sys.argv[2])
min_confidence=float(sys.argv[3])


def rulegeneration(frequencyset,ap4):
	for key in ap4:
		k=1
		while(k<len(frequencyset)):
			for cols in combinations(list(key),k):
				t=str(cols).split()
				if len(t)<=1:
					cols=str(cols).replace('(','')
					cols=str(cols).replace(')','')
					cols=str(cols).replace(',','')
					cols=str(cols).replace('\'','')
				confidence=frequencyset[key]/frequencyset[cols]
				if confidence!=1:
					if (confidence>=min_confidence):
						rules[cols]=confidence
			k+=1

def aprioriloop(apriori,l,transactions):
	ap1={}
	for cols in combinations(apriori,l):
		count1=0
		for j in range(len(transactions)):
			if set(cols).issubset(transactions[j]):
				count1+=1
			ap1[cols]=count1
	return ap1

apriori={}
frequencyset={}

rules={}

count=0
transactions=[]
with open(file_name) as f:
	for line in f:
		transactions.append(line.split())

for i in range(0,len(transactions)):
	for j in range(0,len(transactions[i])):
		if transactions[i][j] not in apriori:
			apriori[transactions[i][j]]=1
		else:
			apriori[transactions[i][j]]+=1

min_support*=len(transactions)
for key,val in apriori.copy().items():
	if val<min_support:
		del apriori[key]
frequencyset=apriori

l=2
ap2=[]
final=[]
final1=[]
while apriori:
	ap2=aprioriloop(apriori,l,transactions)
	for key,val in ap2.copy().items():
		if val<min_support:
			del ap2[key]
	frequencyset.update(ap2)
	
	l=l+1
	if not ap2:
		break
	else:
		final=ap2

rulegeneration(frequencyset,final)
df=pd.DataFrame([[item,val] for item,val in rules.items()],columns=['Item','Confidence'])
print(df)
