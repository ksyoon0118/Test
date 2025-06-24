import random
num1,num2,num3,num4,num5,num6=input("1부터 45까지 중 겹치지 않고 6개의 숫자를 입력하시오.단)숫자 사이에 한칸의 공백을 넣을것").split()
while True :
    n1=random.randint(1,45)
    n2=random.randint(1,45)
    n3=random.randint(1,45)
    n4=random.randint(1,45)
    n5=random.randint(1,45)
    n6=random.randint(1,45)
    bonus=random.randint(1,45)
    if(n1<n2 and n2<n3 and n3<n4 and n4<n5 and n5<n6 and n6< bonus):
        break
set1={num1,num2,num3,num4,num5,num6,n1,n2,n3,n4,n5,n6}
set2={num1,num2,num3,num4,num5,num6,n1,n2,n3,n4,n5,n6,bonus}
print("당신이 적은 번호 : ",num1,num2,num3,num4,num5,num6)
print("로또 번호 : ",n1,n2,n3,n4,n5,n6,"보너스 : ",bonus)
if len(set1)==6:
    print("1등 당첨!")
elif len(set2)==6:
    print("2등 당첨!")
elif len(set2)==7:
    print("3등 당첨!")
elif len(set2)==8:
    print("4등 당첨!")
elif len(set2)==9:
    print("5등 당첨!")
else:
    print("아쉽지만 당첨 아님!")
