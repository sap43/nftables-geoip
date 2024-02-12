# combined ipv4 ipv6 geoip blocking rules generation :-)
# ip address management from a pandas dataframe.
#data taken from file that was downloaded and saved using the geofilter.py script. 
# check for overlap code removed for now. Get back to it if desired later. Not expecting any overlap though. Silly fukcing idea

from ipaddress import IPv4Address, ip_address, summarize_address_range, ip_network

# abc=IPv4Address('223.255.244.0')
# print(abc+1024)

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

# below works but using inplace=True can lead to issues sometimes. Hence deprecated
# india dataframe formed. Now create new df with just ip and counts
# df5=df4.copy(deep=True)
# df5.drop('D3',axis=1,inplace=True)
# df5.drop('D2',axis=1,inplace=True)
# df5.drop('D1',axis=1,inplace=True)
# print(df5)

# better is below
list=['D3','D2','D1','Country','type']
df6=df4.drop(list,axis=1)
# print(df6)

# access every row. Change type of ip to ipv4. Add. Save new range in new column. Save file after removing all unnecessary columns
for a in df6.index:
    df6['ip'][a]=IPv4Address(df6['ip'][a])
    # print(type(df6['ip'][a]))
    # print(type(df6['ip'][a]))
    df6['count'][a]=int(df6['count'][a])

# both BOUND INCLUDE
df6['ip2']=df6['ip']+df6['count']-1
# CONFIRM WHETHER these ips are replacing or inserting. :-) THEY ARENT, as long as there is no row with serial number 0 and 1
#  allocated to IN in original file

# print('MEOWWWW {}'.format(df6.loc[62104]))

df7=df6.drop('count',axis=1)
df7['cidr']=''
for a in df7.index:
# for a in range(1,len(df7.index),1):
    df7['cidr'][a]=summarize_address_range(df7['ip'][a],df7['ip2'][a])







for a in df7.index:
    for el in df7['cidr'][a]:
        df7['cidr'][a]=str(el)
        df7['cidr'][a]=ip_network(df7['cidr'][a])


# df7.loc[0]=[IPv4Address('10.190.0.9'),IPv4Address('10.190.0.9'),ip_network('10.190.0.9/32')]
# df7.loc[1]=[IPv4Address('192.168.0.90'),IPv4Address('192.168.0.90'),ip_network('192.168.0.90/32')]
df7.loc[0]=[IPv4Address('127.0.0.1'),IPv4Address('127.0.0.1'),ip_network('127.0.0.1/32')]



df7.sort_values('ip')
df7.to_csv('fr1.csv')
# f=open('fr1.csv',"w")
# f.write(df6)
# f.close()

# convert to nft format???? NO need to save to csv earlier then. Lol

file1=open('geoip.nft','w')


# LAST COMMA NOT NEEDED

str2='set geoip4 {\ntype ipv4_addr;\nflags interval;\nelements = {\n'
# str2='set geoip4 {\ntype ipv4_addr;\nflags interval;\nelements = {\n'
file1.write(str2)

# asd=df7.shape[0]
# print('AhHSHSHHS {}'.format(asd))
for a in df7.index:
    # print(a)
    # print(len(df7.index))
    if a==len(df7.index):
        str1='{}'.format(df7['cidr'][a])
        
        # str1='{}-{}'.format(df7['ip'][a],df7['ip2'][a])
        # print(str1)
        file1.write(str1)

    else:
        str1='{},\n'.format(df7['cidr'][a])
        # str1='{}-{},\n'.format(df7['ip'][a],df7['ip2'][a])
        # print(str1)
        file1.write(str1)
# print('MEOW'.format(len(a)))
str3='};\n}'
file1.write(str3)
file1.close()
print('DONE!')


file2=open('geoip.nft','r')
print('OLAAAA')
data=file2.read()
print(len(data))
print(data[len(data)-3])
data=data.replace(",\n}\n}","\n}\n}")

# data[len(data)-2]=' '
file3=open('/etc/geoip3.nft','w')
file3.write(data)
file2.close()
# file3.close()

# now lets save geoip3.nft :-)
# file4=open('geoip3.nft','w')
# file4.close()





# print(len(str(file2)))
# print(str(file2))
# print(str(file2)[15:])
# print(str(file2)[55:])

# andy1=file2.seek(55,0)
# print(andy1)
# print(type(andy1))
# print(file2(andy1))

# print(andy1.readline().decode('utf-8'))
# import os

# print(len(str(file2)))













# df411=pd.DataFrame(columns=['D1','ip','ip2'])
# df411=df410.copy()

# list=['']


# df761=df411.drop(,axis=1)




# LATER!!!!!!!!!!
# Convert to cidr notation so we can check for overlap. 
# f4=open('fr1.csv','r')
# df411=pd.read_csv(f4,header=None,names=['D1','ip','ip2'])
# print('columns are {}'.format(df411.columns))
# df8=df761.copy()
# df8=df411.copy()
# df91=df8.drop(0,axis=0)
# df9=df91.drop('D1',axis=1)
# print(df9)
# df9['cidr']=''
# for a in range(1,len(df9.index),1):
    # df9['cidr'][a]=summarize_address_range(df9['ip'][a],df9['ip2'][a])

# print('OLAAA \n {}'.format(df9))
# for a in range(1,len(df9.index),1):
    # for el in df9['cidr'][a]:
        # df9['cidr'][a]=str(el)
        # df9['cidr'][a]=ip_network(df9['cidr'][a])


# print(type(df8['cidr']))
# df8.set_index=False
# check for overlap!!! Already sorted by ip earlier, so just check for overlap. Simple. 

# print(len(df8.index))
# print(df8.loc[:1])
# print(df8[0:1])

# for a in df8.index:
    # for b in list1:
    # if(a==len(df8.index)):
        # pass
    # else:
        # nal=df8['cidr'][a].overlaps(df8['cidr'][a+1])
# print(nal)

# print(type(df8['cidr'][0]))

# list1=df8['cidr'].tolist()
# print(list1)
# print(len(list1))









# print(type(df6["ip"][11598]))
# df6["ip"][11598]=IPv4Address(df6["ip"][11598])
# print(type(df6["ip"][11598]))
# print(df6.columns)
# df6["ip"].apply(IPv4Address)
# print(type(df6["ip"][62082]))
# df6['ip2']=IPv4Address(df6['ip'])
# df6["ip"].astype(IPv4Address)






# ip address management from a pandas dataframe.
#data taken from file that was downloaded and saved using the geofilter.py script. 
# check for overlap code removed for now. Get back to it if desired later. Not expecting any overlap though. Silly fukcing idea

from ipaddress import IPv6Address, ip_address, summarize_address_range, ip_network

# abc=IPv6Address('223.255.244.0')
# print(abc+1024)

import pandas as pd
# from csv import reader
# df=pd.DataFrame(list(reader(str1[val1:-1])))

f31=open('frules.csv','r')
data1=pd.read_csv(f31,header=None)
# new=data["name"].str.split

print('type of data is {}'.format(type(data1)))
# print('OMG@'.format(data[0:0]))
# data[0:0]='hello'
# print('OMG@'.format(data[0:0]))
print('type of data 0 to 1 is {}'.format(type(data1[0:1])))
print(data1[1:2])

print(data1.columns)
print(type(data1.columns))
data1.columns=['hello']
print(data1.columns)
datafinal1=pd.DataFrame(columns=['D1','Country','type','ip','count','D2','D3'])
datafinal1[['D1','Country','type','ip','count','D2','D3']]=data1['hello'].str.split('|',expand=True)
# print(datafinal[2:10])
df31=datafinal1[datafinal1["Country"]=="IN"]
df41=df31[df31["type"]=="ipv6"]

# below works but using inplace=True can lead to issues sometimes. Hence deprecated
# india dataframe formed. Now create new df with just ip and counts
# df5=df4.copy(deep=True)
# df5.drop('D3',axis=1,inplace=True)
# df5.drop('D2',axis=1,inplace=True)
# df5.drop('D1',axis=1,inplace=True)
# print(df5)

# better is below
list1=['D3','D2','D1','Country','type']
df61=df41.drop(list1,axis=1)
# print(df6)

# access every row. Change type of ip to ipv4. Add. Save new range in new column. Save file after removing all unnecessary columns
for a1 in df61.index:
    df61['ip'][a1]=IPv6Address(df61['ip'][a1])
    # print(type(df6['ip'][a]))
    # print(type(df6['ip'][a]))
    df61['count'][a1]=int(df61['count'][a1])

# both BOUND INCLUDE
df61['ip2']=df61['ip']+df61['count']-1
# CONFIRM WHETHER these ips are replacing or inserting. :-) THEY ARENT, as long as there is no row with serial number 0 and 1
#  allocated to IN in original file

# BELOW IS ERROR
# print('MEOWWWW {}'.format(df6.loc[62104]))

df71=df61.drop('count',axis=1)
df71['cidr']=''
for a in df71.index:
# for a in range(1,len(df7.index),1):
    df71['cidr'][a]=summarize_address_range(df71['ip'][a],df71['ip2'][a])







for a in df71.index:
    for el in df71['cidr'][a]:
        df71['cidr'][a]=str(el)
        df71['cidr'][a]=ip_network(df71['cidr'][a])

# ONLY when i find internal ipv6 addresses :-)
# df7.loc[0]=[IPv6Address('192.168.0.1'),IPv6Address('192.168.0.1'),ip_network('192.168.0.1/32')]
# df7.loc[1]=[IPv6Address('192.168.0.90'),IPv6Address('192.168.0.90'),ip_network('192.168.0.90/32')]

df71.sort_values('ip')
df71.to_csv('fr1v6.csv')

# f=open('fr1.csv',"w")
# f.write(df6)
# f.close()

# convert to nft format???? NO need to save to csv earlier then. Lol

file11=open('geoipv6.nft','w')


# LAST COMMA NOT NEEDED

str21='\nset geoip6 {\ntype ipv6_addr;\nflags interval;\nelements = {\n'
# str2='set geoip4 {\ntype ipv4_addr;\nflags interval;\nelements = {\n'
file11.write(str21)

# asd=df7.shape[0]
# print('AhHSHSHHS {}'.format(asd))
for a in df71.index:
    # print(a)
    # print(len(df7.index))
    if a==len(df71.index):
        str11='{}'.format(df71['cidr'][a])
        
        # str1='{}-{}'.format(df7['ip'][a],df7['ip2'][a])
        # print(str1)
        file11.write(str11)

    else:
        str11='{},\n'.format(df71['cidr'][a])
        # str1='{}-{},\n'.format(df7['ip'][a],df7['ip2'][a])
        # print(str1)
        file11.write(str11)
# print('MEOW'.format(len(a)))
str31='};\n}'
file11.write(str31)
file11.close()
print('DONE!')


file21=open('geoipv6.nft','r')
print('OLAAAA')
data123=file21.read()
print(len(data123))
print(data123[len(data123)-3])
data123=data123.replace(",\n}\n}","\n}\n}")

# data[len(data)-2]=' '
# file3=open('geoip3.nft','w')
file3.write(data123)
file21.close()
file3.close()

