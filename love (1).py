name1=input('Enter Ur aname:')
name2=input('Enter Ur aname:')
lower_case=name.lower()
t=lower_case.count('t')
r=lower_case.count('r')
u=lower_case.count('u')
e=lower_case.count('e')

l=lower_case.count('l')
o=lower_case.count('o')
v=lower_case.count('v')
e=lower_case.count('e')

True_Sum=t+r+u+e
Love_Sum=l+o+v+e
Love_Score=int(str(True_Sum)+str(Love_Sum))
if(Love_Score<10 or Love_Score>90):
    print(f"Your Love Score is{Love_Score} %  and get coke")
elif(Love_Score>=40 and Love_Score<=50):
    print(f"Your Love Score is{Love_Score} % and alright together ")