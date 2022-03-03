import os

#quiz questions

data={
    "Which of the following can contaminate an aquifer?":["Less than 1%","About 5%","About 10%","About 20%",0],
    "Which of the following can contaminate an aquifer ":["Landfills","Agricultural regions","Gas stations","All of these",3],
    "Excessive pumping in relation to recharge can cause":["The water table to decline","A cone of depression","The well to go dry","All of these",3],
    "Groundwater represents how much of the world's fresh water supply ":["About 1%","About 5%","About 20%","About 50%",2],
    "Which one of the following features is a sure sign of karst":["sinkholes","Artesian walls","Cones of depression","Speleothems",0]
}

#quiz logic
marks=0
count=1
for question in data:
    os.system("cls")
    print("----------WELCOME TO QUIZ--------------")
    print(count,end=". ")
    print(question)
    for x in range(0,len(data[question])-1):
        print(f'\t{x+1}. {data[question][x]}')
    count+=1
    answer=int(input("Enter you option: "))
    if answer-1==data[question][-1]:
        marks+=1
os.system('cls')
print("Thankyou for taking the quiz!!")
print(f"Marks={marks}/{len(data)}")
