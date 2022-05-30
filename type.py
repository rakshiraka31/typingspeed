from time import *
import random as rd


def mistake(partest,user):
       error = 0
       for i in range(len(partest)):
           try:
              if partest[i] != user[i]:
                     error = error + 1
              
           except Exception as e:
                  error = error + 1
       return error

def speed_time(time_s,time_e,userinput):
       time_delay = time_e - time_s
       time_R = round(time_delay,2)
       speed = len(userinput)/time_R
       return round(speed)

if __name__== '__main__':

       while True:
              ck= input("Ready to test: Yes/ No :")
              if ck =="Yes":
                     test =["a paragraph is a self-contained unit of discoursin writing",
                            "my name is Rakesh mahat.","welcome to cubetech"]
                     test1= rd.choice(test)
                     print("*****typing speed*****")
                     print(test1)
                     print()
                     print()
                     time_1 = time()
                     testinput=input("Enter : ")
                     time_2 = time()

                     print('speed :',speed_time(time_1,time_2,testinput),"w/sec")
                     print("Error :",mistake(test1,testinput))
                     
              elif ck=="No":
                     print(" okay, thank you")
                     break
              
              else:
                     print("Wrong Input")