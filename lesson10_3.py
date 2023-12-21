import random
import pyinputplus as pyip

def getstudent()-> list[list]:
    '''
    參數:學生人數-> student_nums
    參數:科目數 -> scores_nums
    '''
    with open('names.txt',mode='r',encoding='utf-8') as file:
        names:str=file.read()

    nameList:list[str]=names.split('\n')

    student_nums:int = pyip.inputInt("請輸入學生的人數(1~50):",min=1,max=50)
    scores_nums:int = pyip.inputInt("請輸入科目數(1~7):",min=1,max=7)


    students:list[list] = []

    names:list[str] = random.choices(nameList,k=student_nums)
    for name in names:
        stu:list[int|str] = []
        stu.append(name)    
        for i in range(scores_nums):
            stu.append(random.randint(40,100))
        students.append(stu)

    return students




if __name__ =='__main__':
    students:list[list]=getstudent()
    print(students)

