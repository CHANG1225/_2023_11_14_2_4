import pyinputplus as pypi

def getBMI(hight:float,weight:float)->tuple[float,str]:
    bmi = weight / (hight/100)**2
    message=''

    if bmi >=35:
        message='「您重度肥胖」'

    elif bmi >=30 and bmi <35:
        message='「您中度肥胖」'

    elif bmi >=27 and bmi <30:
        message='「您輕度肥胖」'

    elif bmi >=24 and bmi <27:    
        message='「您的體重過重」'

    elif bmi >=18.5 and bmi<24:
        message='「您的體重屬正常範圍」'

    else:
        message='「您的體重過輕」'
    return(bmi,message)


while True:
    weight = pypi.inputFloat('請輸入體重,單位為(公斤):',min=0)
    print(weight)
    hight = pypi.inputFloat('請輸入身高,單位為(公分):',min=0)
    print(hight)

    bmi,message =getBMI(hight=hight,weight=weight)
    print(f'您的bmi是{bmi:.2f},{message}')

    is_continue=pyip.inputYesNo('請問還要繼續嗎?(y,n)')
    if is_continue != 'yes':
        break

print('結束')