from collections import Counter

list=[1,"asasdfw",23,"shabash",12,23,23,23,234,"asdfr",23,23,12,23,12,23]
def rept():
     count=0
     t=0
     for x in range(0,len(list)):
          t=list.count(list[x])
          if (t>count):
               count=t
               num=x
     mstf=list[num]
     print('Frequent number is  {} and repeats {} times'.format(mstf,count))

def reptwo():
    counter= Counter(list)
    num1=counter.most_common(2)[0][0]
    frq1=counter.most_common(2)[0][1]
    num2=counter.most_common(2)[1][0]
    frq2=counter.most_common(2)[1][1]
    print("Frequent  numbers are {} and {}. It occurs {} and {} times respectevily".format(num1,num2,frq1,frq2))
     

rept()
reptwo()

def only_string():
     strings=[]
     for x in list:
          if(type(x)==str):
               strings.append(x)
              
     print('The New List is {}'.format(strings))
          

only_string()
