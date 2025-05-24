import random2 as random

option = ['snake','water','gun']
matrix=[
    [2,1,0], #snake
    [0,2,1], #water
    [1,0,2] #gun
]
user = input("choose snake,water or gun: ")
comp=random.choice(option)
print("Computer chose:",comp)
user_index=option.index(user)
comp_index=option.index(comp)
result_code=matrix[user_index][comp_index]
if result_code==2:
    print("Result: Draw")
elif result_code ==1:
    print("Result: You win!!")
else:
    print("Result: Computer wins!!")