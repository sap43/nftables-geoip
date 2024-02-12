# WHAT ABOUT IPV6 !!!!
# geofiltering of ip addresses at the firewall layer. Updated daily from apnic site. Save to file. Merge all subranges. Then over to the bash script
# I need both ranges and cidr notation. cidr is for overlap, ranges for ufw
# sort and then compare, to reduce the number of lookups. 

import requests
import datetime

ct=datetime.datetime.now()
print('Attempting firewall update on {}'.format(ct))

ip='https://ftp.apnic.net/stats/apnic/delegated-apnic-latest'
r=requests.get(ip)
print(r.status_code)
# print(r.text)

# save data to file
f=open('firewallranges.csv',"w")
f.write(r.text)
f.close()

# strip response of all headers and then convert to dataframe
print(type(r.text))
str1=r.text
sub='summary'
a1=len(sub)
print(a1)
print(type(a1))
ind1=str1.find(sub)
print(ind1)
# print(type(ind1))
ind2=str1.find(sub,ind1+a1)
# print(ind2)
ind3=str1.find(sub,ind2+a1)
# print(ind3)
val1=ind3+a1
# print(val1)
# print(type(val1))


f2=open('frules.csv',"w")
f2.write(str1[val1+1:-1])
# str1[val1:-1]
f2.close()

# now we manipulate, save to panda. 

import pandas as pd
# from csv import reader
# df=pd.DataFrame(list(reader(str1[val1:-1])))

f3=open('frules.csv','r')
data=pd.read_csv(f3,header=None)
# new=data["name"].str.split

print('type of data is {}'.format(type(data)))
# print('OMG@'.format(data[0:0]))
# data[0:0]='hello'
# print('OMG@'.format(data[0:0]))
print('type of data 0 to 1 is {}'.format(type(data[0:1])))
print(data[1:2])

print(data.columns)
print(type(data.columns))
data.columns=['hello']
print(data.columns)
datafinal=pd.DataFrame(columns=['D1','Country','type','ip','count','D2','D3'])
datafinal[['D1','Country','type','ip','count','D2','D3']]=data['hello'].str.split('|',expand=True)
# print(datafinal[2:10])
df3=datafinal[datafinal["Country"]=="IN"]
df4=df3[df3["type"]=="ipv4"]
# print(df4)


# CALC for determining ip ranges shouldnt assume count is a multiple of 256
# first value is inclusive I THINK. Last value is also inclusive. 
from ipaddress import IPv4Address

list=['D3','D2','D1','Country','type']
df6=df4.drop(list,axis=1)
# print(df6)

# access every row. Change type of ip to ipv4. Add. Save new range in new column. Save file after removing all unnecessary columns
for a in df6.index:
    df6['ip'][a]=IPv4Address(df6['ip'][a])
    # print(type(df6['ip'][a]))
    # print(type(df6['ip'][a]))
    df6['count'][a]=int(df6['count'][a])
    
# both bounds inclusive. Sorting helps reduce the number of lookups needed
df6['ip2']=df6['ip']+df6['count']-1
df7=df6.drop('count',axis=1)
df7.sort_values('ip')
# print(df7)
df7.to_csv('fr1.csv')


# c0.a8.00.01 
# (0xc
# 0a80001
# )




# print(data.loc)
# print(data)
