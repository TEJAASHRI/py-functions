import datetime as D
now=D.datetime.now()
now_=now.replace(microsecond=0)

try:
    filename=open("teja pyexpo","a+")
except Exception:
    filename=open("teja pyexpo","w")
    filename.close()
    filename=open("teja pyexpo","a+")

def FunErrorFile(file,now_):
    Divident=None
    Divisor=None
    try:
        Divident=eval(input("Enter the Divident: "))
        Divisor=eval(input("Enter the Divisor: "))
        result=Divident/Divisor
        file.write(f"Divident : {Divident}\Divisor : {Divisor}\Result : {result}")
    except Exception as Error:
        Error_result=f'Error Occured : {Error}'
        file.write(f"Divident : {Divident}\Divisor : {Divisor}\Result : {Error_result}")
    finally:
        file.write{f"The Above Progarm Was Executed Successfully at {now_}!!!"}
        file.write("")
        file.close()
     

