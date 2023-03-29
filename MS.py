import pandas as pd 
import matplotlib.pyplot as plt 
import getpass 
from google.colab import drive 
drive.mount('/content/drive') 
path = "/content/MS - Sheet1.csv" 
MS = pd.read_csv(path, index_col = 0) 
print("WELCOME TO:\nMS") 
pwd=getpass.getpass("PassWord") 
if pwd=="****":
    print("Hi, WELCOME") 
    while True:
        print("A.ADDITION")  
        print("B.MODIFICATION") 
        print("C.DELETE") 
        print("\t\tGRAPHICAL PRESENTATION") 
        print("D.HISTOGRAM") 
        print("E.BAR GRAPH") 
        print("F.LINE GRAPH") 
        print("G.EXIT") 
        Lh=input("enter a choice") 
        if Lh =='A':
            while True:        # THIS TO ADD A NEW RECORD WITH VALIDATIONS   CO=input(' NEW CODE : ')  
                if CO.isnumeric():
                    CO =int(CO) 
                    break 
  
            while True:
                NM=input(' NAME : ') 
                if not NM == "":
                    break 
  
  
            while True:
                PR=input(' PRICE(INR) : ') 
                if PR.isnumeric():
                    PR =int(PR) 
                    break 
            while True:
                VR=input(' VARIENT(GB) :') 
                if VR.isnumeric():
                    VR =int(VR) 
                    break
            while True:
                PR=input(' PROCESSOR :')
                if PR.isalpha():
                    PR = string(PR)
                    break
            while True:  
                SS=input(' SCREEN(INCHES) : ') 
                if SS.isnumeric(): 
                    SS =float(SS) 
                    break 
             
            while True: 
                RR=input(' RESOLUTION(Hz) :') 
                if RR.isnumeric(): 
                    RR =int(RR) 
                    break 
  
            MS.loc[CO,:]=[NM,PR,VR,PR,SS,RR] 
            print(MS)  
            print() 
            MS.to_csv(path)           # WRITE THE NEW CHANGES TO CSV
            
            elif Lh =='B':              # MODIFY THE EXISTING CODES  
                changes = "" 
                ncode=int(input("code to modify")) 
                Menulist = MS.columns.tolist() 
                Lh1 = int(input("1.Name \n2.Price \n3.VARIENT \n4.SCREEN(INCHES) \n5.Processor \n6.Resolution(Hz)\n"))  if Lh1 ==2 or Lh1 ==3 or Lh1 ==6: 
                changes = int(input("New Value")) 
            elif Lh1 == 4:
                changes = float(input("New Value"))  
                
            elif Lh1 == 1 or ch1 == 5:
                changes = input("New Value") 
                MS.at[ncode,Menulist[Lh1-1]] = changes 
                print(MS) 
                MS.to_csv(path)               # WRITE THE NEW RECORD TO CSV  
                
            elif Lh =='C':                 # TO DELETE EXISTING CODES FROM MS   print(MS) 
                ncode=int(input("Code to delete")) 
                MS = MS.drop(ncode)            # USE THE DROP TO DELETE  print(MS) 
                MS.to_csv(path)                 # THIS IS TO WRITE THE NEW RECORD TO THE CSV   elif Lh =='D': # SHOW THE REQUIRED INFORMATION ON GRAPHS   plt.figure() # HISTOGRAM 
                MS.plot.hist(x='Screen(inches)',y='Varient(GB)' ,edgecolor="green" ,bins = 5, rot = 90)  plt.xlabel('Varient(GB)',fontsize = 19, labelpad = 15, color = 'blue') 
                plt.ylabel('screen(inches)',fontsize = 19, labelpad = 15, color = 'red') 
                plt.title('COMPARISON OF SCREEN(INCHES) AND THE VARIENT') 
                plt.show()  
            elif Lh =='E':           # BAR GRAPH  
                plt.figure()  
                MS.plot.bar(x='Price(INR)',y='Varient(GB)',rot = 80) 
                plt.xlabel('Price(INR)',fontsize = 18, labelpad = 15, color = 'green') 
                plt.ylabel('Varient(GB)',fontsize = 18, labelpad = 15, color = 'orange') 
                plt.title('PRICE IN COMPARISON OF VARIENT') 
                plt.show()
  
            elif Lh =='F':          # LINE GRAPH 
                plt.figure() 
                MS.plot.line(x = 'Name',y = 'Resolution(Hz)', rot = 90,color = 'orange')  plt.title('COMPARISON OF NAME TO RESOLUTION(Hz)') 
                plt.show() 
                
            elif Lh =='G':           # TAG LINE WHILE EXITING MS  
                print("Catch us later :))") 
                print(" TO Mobile Stuff (MS)") 
                break 
  
            else: 
                print(" ------- ")
else:
    print("No entry wrong password")        # IF WRONG PASSWORD INPUT NO ENTRY THEN
    