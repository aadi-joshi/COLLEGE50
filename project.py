import os
import re
from colorama import Fore
import stdiomask
from pyfiglet import Figlet
import sys
import codecs
from tabulate import tabulate

#ERRORS RED
#CORRECT/OUTPUT GREEN
#INSTRUCTIONS BLUE

os.system('clear')
facultysec=[21085,35248,43674,48861,93696,15943,47881,78185,95752,75764]

studrn=0
facurn=0
sss=""
stdtemp=""
logstat=False
loggedlist=[]
loginfac=False
sorf=""

def student():
    global studrn
    global sss
    global stdtemp
    sss="stu"
    stdtemp='s'+str(studrn+1).zfill(5)
    name=get_name()
    email=get_email(name)
    pass1=get_pass(name,email)
    fileio(name,email,pass1)

def faculty():
    global facurn
    global sss
    global stdtemp
    sss="fac"
    stdtemp='f'+str(facurn+1).zfill(5)
    name=get_name()
    email=get_email(name)
    pass1,subject=get_pass(name,email,True)
    fileio(name,email,pass1,subject)

def get_name():
    global sss
    while True:
        print(to_print(sss) + '\n' + to_print(sss+'lo') + ' Reg. No.: ' + stdtemp)
        try:
            if(sss=="fac"):
                name=input("\n\n\n\n\n"
                           + Fore.BLUE + "\33[F\33[F\33[F\33[FFaculty members are requested to include their honorifics"
                                                         + "\n  in their full name (Dr., Prof., Mr., Ms., Mrs., etc)" + Fore.RESET +
                           "\nEmail Address   :\nPassword        :\nConfirm Password:\33[F\33[F\33[F\33[F\33[FFull Name       : ").strip()
            else:
                name=input("\nEmail Address   :\nPassword        :\nConfirm Password:\33[F\33[F\33[FFull Name       : ").strip()
        except EOFError:
            eofdet()
        else:
            if(name==""):
                os.system('clear')
                print(Fore.RED + "Input cannot be empty.\nReprompting." + Fore.RESET)
                continue
            if(chk_det("n",name)==True):
                os.system('clear')
                return name
            else:
                os.system('clear')
                print(Fore.RED + "Name can only contain letters," + Fore.RESET)
                print(Fore.RED + "spaces and periods. Reprompting." + Fore.RESET)
                continue

def get_email(name):
    while True:
        print(to_print(sss) + '\n' + to_print(sss+'lo') + ' Reg. No.: ' + stdtemp)
        try:
            email=input("Full Name       : "+ Fore.GREEN + str(name) + Fore.RESET
                        +"\n\nPassword        :\nConfirm Password:\33[F\33[FEmail Address   : ").strip()
        except EOFError:
            eofdet()
        else:
            if(email==""):
                os.system('clear')
                print(Fore.RED + "Input cannot be empty.\nReprompting." + Fore.RESET)
                continue
            if(chk_det("e",email)==True):
                os.system('clear')
                return email
            else:
                os.system('clear')
                print(Fore.RED + "Invalid email format." + Fore.RESET)
                print(Fore.RED + "Reprompting." + Fore.RESET)
                continue

def get_pass(name,email,isfac=False):
    while True:
        print(to_print(sss) + '\n' + to_print(sss+'lo') + ' Reg. No.: ' + stdtemp)
        pass1=stdiomask.getpass(("Full Name       : "+ Fore.GREEN + str(name) + Fore.RESET
                    +"\nEmail Address   : "+ Fore.GREEN + str(email) + Fore.RESET
                    +"\n\nConfirm Password:\33[FPassword        : "),'●').strip()
        print('\33[A\33[A\33[A\33[A\33[A\33[A'+'\033[1m' + '\033[4m' + to_print(sss) + '\n' + to_print(sss+'lo') + ' Reg. No.: ' + stdtemp)
        if(pass1==""):
                os.system('clear')
                print(Fore.RED + "Input cannot be empty.\nReprompting." + Fore.RESET)
                continue
        try:
            pass2=input("Full Name       : "+ Fore.GREEN + str(name) + Fore.RESET
                        +"\nEmail Address   : "+ Fore.GREEN + str(email) + Fore.RESET
                        +"\nPassword        : " + "●"*len(pass1)
                        +"\nConfirm Password: ").strip()
        except EOFError:
            eofdet()
        else:
            if(chk_det('p',pass1) and chk_det('p',pass2)
               and len(pass1)>=5 and len(pass2)>=5):
                if((pass1==pass2)):
                    if(isfac==False):
                        os.system('clear')
                        print(Fore.GREEN + "\033[1mSubmitted.\033[0m" + Fore.RESET)
                        return pass1
                    else:
                        subject=get_sec()
                        os.system('clear')
                        print(Fore.GREEN + "\033[1mSubmitted.\033[0m" + Fore.RESET)
                        return[pass1,subject]
                else:
                    os.system('clear')
                    print(Fore.RED + "Passwords do not match" + Fore.RESET)
                    print(Fore.RED + "Reprompting." + Fore.RESET)
                    continue
            else:
                os.system('clear')
                print(Fore.RED + "Password cannot contain spaces  or commas and" + Fore.RESET)
                print(Fore.RED + " must have 5 or more characters. Reprompting." + Fore.RESET)
                continue

def get_sec():
    n=5
    print('\033[1m'+ Fore.RED
              + "\nNOTE: All faculty have been given 10 valid verification codes"
              + "\n  prior to this registration. This is for security purposes." + Fore.RESET + '\033[0m')
    while True:
        try:
            secnum=input('\033[1m' + 'Faculty Verif. No.: ' + '\033[0m').strip()
        except EOFError:
            eofdet()
        else:
            if(secnum==""):
                os.system('clear')
                print(Fore.RED + "Input cannot be empty.\nReprompting" + Fore.RESET)
                continue
            if(chk_det("f",secnum)):
                break
            else:
                n=n-1
                if(n>0):
                    print(Fore.RED + "Invalid staff verification number.\n"+str(n)+" attempts left." + Fore.RESET)
                    continue
                else:
                    os.system('clear')
                    print(Fore.RED + "Invalid verification number entered 5 times."
                          + "\nRedirecting to Login/Register Page." + Fore.RESET)
                    main()
    print('\033[1m' + '\33[FFaculty Verif. No.: ' + '\033[0m'
          + Fore.GREEN + secnum + Fore.RESET)
    try:
        subject=input('\033[1m' + 'Enter your subject: ' + '\033[0m')
    except EOFError:
        eofdet()
    else:
        return[subject]

def to_print(s):
    if(s=="stu"):
        return('\033[1m' + '\033[4m' + 'STUDENT REGISTRATION' + '\033[0m'
               + Fore.BLUE + '\033[1m' + '\nKINDLY REMEMBER YOUR REGISTRATION NUMBER' + Fore.RESET + '\033[0m')
    elif(s=="fac"):
        return('\033[1m' + '\033[4m' + 'FACULTY REGISTRATION' + '\033[0m'
               + Fore.BLUE + '\033[1m' + '\nKINDLY REMEMBER YOUR REGISTRATION NUMBER' + Fore.RESET + '\033[0m')
    elif(s=="stulo"):
        return("Student")
    elif(s=="faclo"):
        return("Faculty")
    else:
        raise ValueError

def chk_det(tocheck,temp):
    if(tocheck=="p"):
        for i in temp:
            if i in [" ",","]:
                return False
        return True
    elif(tocheck=="n"):
        if re.search(r"^([a-zA-Z]+\. )*[a-zA-Z ]+$",temp):
            return True
        else:
            return False
    elif(tocheck=="e"):
        #if re.search(r"^[^@].+@[^@]+\.\w+",temp):
        if re.search(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$",temp):
            return True
        else:
            return False
    elif(tocheck=='f'):
        for item in facultysec:
            try:
                if item==int(temp):
                    return True
            except:
                return False
            else:
                continue
        return False
    else:
        return False

def fileio(name,email,pass1,sub=""):
    if(sub==""):
        global studrn
        studrn=studrn+1
        stdtemp='s'+str(studrn).zfill(5)
        temp = name+','+email+','+pass1+','+stdtemp
        with open("students.csv","a") as file:
            file.write(temp+'\n')
        main()
    else:
        global facurn
        facurn=facurn+1
        stdtemp='f'+str(facurn).zfill(5)
        temp = name+','+email+','+pass1+','+stdtemp+','+sub[0]
        with open("faculty.csv","a") as file:
            file.write(temp+'\n')
        main()

def eofdet(logged=False):
    os.system('clear')
    if(logged==False):
        print(Fore.GREEN + "Ctrl+D detected.\nReturning to previous page." + Fore.RESET)
        main()
    else:
        print(Fore.GREEN + "Ctrl+D detected.\nReturning to previous page." + Fore.RESET)
        loggedin()

def login():
    global loggedlist
    while True:
        print("\033[1m\033[4mSTUDENT/FACULTY LOGIN\033[0m")
        try:
            regnum=input("\nEmail Address      :\nPassword           :\33[F\33[FRegistration Number: ").strip()
        except EOFError:
            eofdet()
        else:
            result=chk_login(regnum,'r')
            if(result==0):
                os.system('clear')
                print(Fore.RED + "Invalid input\nReprompting." + Fore.RESET)
                continue
            elif(result==1):
                os.system('clear')
                print(Fore.RED + "Registration Number not found.\nReprompting." + Fore.RESET)
                continue
            elif(result==2):
                break
    os.system('clear')
    while True:
        print("\033[1m\033[4mSTUDENT/FACULTY LOGIN\033[0m")
        try:
            regmail=input("Registration Number: "+ Fore.GREEN + str(regnum) + Fore.RESET
                        +"\n\nPassword           :\33[FEmail Address      : ").strip()
        except EOFError:
            eofdet()
        else:
            result=chk_login(regmail,'e',regnum)
            global sorf
            if(result[0]==0):
                os.system('clear')
                print(Fore.RED + "Invalid input\nReprompting." + Fore.RESET)
                continue
            elif(result[0]==1):
                os.system('clear')
                print(Fore.RED + "Email Address not found.\nReprompting." + Fore.RESET)
                continue
            elif(result[0]==2):
                sorf=result[1]
                break
    os.system('clear')
    while True:
        print("\033[1m\033[4mSTUDENT/FACULTY LOGIN\033[0m")
        regpass=stdiomask.getpass("Registration Number: "+ Fore.GREEN + str(regnum) + Fore.RESET
                                +"\nEmail Address      : "+ Fore.GREEN + str(regmail) + Fore.RESET
                                +"\nPassword           : ",'●').strip()
        result=chk_login(regpass,'p',regmail,sorf)
        #print(result)
        if(result==2):
            os.system('clear')
            loggedin()
        else:
            os.system('clear')
            print(Fore.RED + "Incorrect password entered.\nReprompting." + Fore.RESET)
            continue

    #os.system('clear')
    #print(Fore.GREEN + "Successfully logged in.\nWelcome to COLLEGE50" + Fore.RESET)
    #break

def chk_login(temp,chr,opt1="",opt2=""):
#return 0 : invalid format
#return 1 : valid format, but not found
#return 2 : found
    global logstat
    global loggedlist
    global loginfac
    if(chr=='r'):
        if(len(temp)!=6 or temp[0] not in ('s','f')):
            return 0
        try:
            numint=int(temp[1:])
        except:
            return 0
        else:
            #global logstat
            with open("students.csv","r") as file:
                for line in file:
                    #print(line)
                    row=line.rstrip().split(",")
                    if(row[3]==temp):
                        logstat=True
                        break
            if(logstat==False):
                with open("faculty.csv","r") as file:
                    for line in file:
                        row=line.rstrip().split(",")
                        if(row[3]==temp):
                            logstat=True
                            break
            #print("This is logstat: ",logstat)
            if(logstat==True):
                return 2
            else:
                return 1
    elif(chr=='e'):
        tp=False
        if(chk_det("e",temp)==False):
            return [0]
        else:
            storfa=opt1[0]
            #tempno=int(opt[1:])
            if(storfa=="s"):
                with open("students.csv","r") as file:
                    for line in file:
                        row=line.rstrip().split(",")
                        if(row[3]==opt1):
                            if(row[1]==temp):
                                tp=True
                                break
                            break
            elif(storfa=="f"):
                with open("faculty.csv","r") as file:
                    for line in file:
                        row=line.rstrip().split(",")
                        if(row[3]==opt1):
                            if(row[1]==temp):
                                tp=True
                                break
                            break
            if(tp==True):
                return [2,storfa]
            else:
                return [1]
    elif(chr=='p'):
        tp=False
        #temp = pass, chr = useless, opt1 = mail, opt2 = character
        if(opt2=="s"):
            with open("students.csv","r") as file:
                for line in file:
                    r=line.rstrip().split(",")
                    if(r[1]==opt1):
                        if(r[2]==temp):
                            tp=True
                            loggedlist=r
                            loginfac=False
                            break
                        break
        if(opt2=="f"):
            with open("faculty.csv","r") as file:
                for line in file:
                    r=line.rstrip().split(",")
                    if(r[1]==opt1):
                        if(r[2]==temp):
                            tp=True
                            loggedlist=r
                            loginfac=True
                            break
                        break
        if(tp==True):
                return 2
        else:
                return 1

def loggedin():
    #os.system('clear')
    temp=""
    print("\033[1m" + (Figlet(font='big')).renderText('COLLEGE50') + "\033[0m")
    if(loginfac==True):
        temp="Faculty"
    else:
        temp="Student"
    print("\33[F\33[F\33[FLogged in as " + Fore.GREEN + loggedlist[0] + Fore.RESET
          + " (" + Fore.GREEN + temp + Fore.RESET + ")" + Fore.RESET)
    try:
        usrinp=int(input("\n\n\n\033[1m\33[F\33[F" + "\n(1) --> View Notices\n(2) --> Add Notice\n(3) --> Committees\n(4) --> View Faculty\n(5) --> View Schedule\n(6) --> About Us"+
                     "\033[1m\n" +
                    Fore.BLUE + "NOTE: \033[0m"+ Fore.BLUE + "Use Ctrl+D to logout." + Fore.RESET + "\n\33[F\33[F\33[F\33[F\33[F\33[F\33[F\33[FEnter a number: \033[0m").strip())
    except EOFError:
        try:
            over=int(input(Fore.RED + "\n\n\n\n\n\n\n\n\n\033[1mCtrl+D detected.\nRepeat to logout. \033[0m" + Fore.RESET))
        except EOFError:
            os.system('clear')
            print(Fore.GREEN + "Logged out.\nReturning to Register/Login Page." + Fore.RESET)
            #OTHER FUNCTIONS THAT HAVE TO BE RESET TO BE DONE IN MAIN
            main()
        except ValueError:
            os.system('clear')
            print(Fore.GREEN + "Ctrl+D not detected.\nReturning to home page." + Fore.RESET)
            loggedin()
        else:
            os.system('clear')
            print(Fore.GREEN + "Ctrl+D not detected.\nReturning to home page." + Fore.RESET)
            loggedin()
    except ValueError:
        os.system('clear')
        print(Fore.RED + "Invalid input.\nReprompting." + Fore.RESET)
        loggedin()
    else:
        try:
            userinp = int(usrinp)
        except:
            os.system('clear')
            print(Fore.RED + "Invalid input.\nReprompting." + Fore.RESET)
            ##main()
        else:
            match(int(usrinp)):
                case 1:
                    os.system('clear')
                    view_notices()
                case 2:
                    os.system('clear')
                    add_notice()
                case 3:
                    os.system('clear')
                    committees()
                case 4:
                    os.system('clear')
                    view_faculty()
                case 5:
                    os.system('clear')
                    view_schedule()
                case 6:
                    os.system('clear')
                    about_us()
                case _:
                    os.system('clear')
                    print(Fore.RED + "Invalid input.\nReprompting." + Fore.RESET)
                    loggedin()

def add_notice():
    print("\033[1m" + (Figlet(font='big',width=200)).renderText('ADD   NOTICE')
          + "\033[0m\033[F\033[F" + Fore.BLUE + "Use Ctrl+D to return to previous page.\n" + Fore.RESET)
    try:
        title=input("\033[1m\nEvent: \nDate :\nTime : \nVenue: \033[F\033[F\033[F\033[FTitle: \033[0m").strip()
    except EOFError:
        eofdet(True)
    try:
        event=input("\033[1m\nDate : \nTime : \nVenue:\033[F\033[F\033[F\033[FTitle: \nEvent: \033[0m").strip()
    except EOFError:
        eofdet(True)
    try:
        date=input("\033[1m\nTime : \nVenue:\033[F\033[F\033[F\033[FTitle: \nEvent: \nDate : \033[0m").strip()
    except EOFError:
        eofdet(True)
    try:
        time=input("\033[1m\nVenue:\033[F\033[F\033[F\033[FTitle: \nEvent: \nDate : \nTime : \033[0m").strip()
    except EOFError:
        eofdet(True)
    try:
        venue=input("\033[1m\033[F\033[F\033[F\033[FTitle: \nEvent: \nDate : \nTime : \nVenue: \033[0m").strip()
    except EOFError:
            eofdet(True)
    with open("notices.txt","a") as file:
        file.write(title+"$"+event+"$"+date+"$"+time+"$"+venue+"$"+loggedlist[0]+"\n")
    os.system('clear')
    print(Fore.GREEN + "Submitted.\nReturning to home page." + Fore.RESET)
    loggedin()

def view_notices():
    print("\033[1m" + (Figlet(font='big',width=200)).renderText('NOTICES') + "\033[0m\n\033[F\033[F\033[F")
    global loggedlist
    rows=[]
    with open("notices.txt","r") as file:
        for line in file:
            rows.insert(0,line.split("$"))
    for i in rows:
        print("="*12+"NOTICE"+"="*12
              +"\n"+i[0] + "\n" + i[1] + "\non "+i[2] + "\nfrom " + i[3] + "\nat " + i[4]
              + "\n    - by " + (i[5]).strip() + "\n"+"="*30 + "\n" )
    try:
        temp = input(Fore.BLUE + "Use Ctrl+D to return to previous page." + Fore.RESET)
    except EOFError:
        eofdet(True)
    else:
        view_notices()
    #print(rows)
    #sys.exit()
    #    file.write("="*12+"NOTICE"+"="*12
    #               +"\n"+)

def committees():
    os.system('clear')
    print("\033[1m" + (Figlet(font='big',width=200)).renderText('COMMITTIES') + "\033[0m\033[F\033[F")
    with codecs.open("committees.txt","r",encoding='unicode_escape') as file:
        for line in file:
            r=line.strip()
            print(r)
    try:
        temp = input(Fore.BLUE + "\nUse Ctrl+D to return to previous page." + Fore.RESET)
    except EOFError:
        eofdet(True)
    else:
        committees()

def about_us():
    os.system('clear')
    print("\033[1m" + (Figlet(font='big',width=200)).renderText('ABOUT US') + "\033[0m\033[F\033[F")
    with codecs.open("aboutus.txt","r",encoding='unicode_escape') as file:
        for line in file:
            r=line.strip()
            print(r)
    try:
        temp = input(Fore.BLUE + "\nUse Ctrl+D to return to previous page." + Fore.RESET)
    except EOFError:
        eofdet(True)
    else:
        committees()

def view_schedule():
    os.system('clear')
    print("\033[1m" + (Figlet(font='big',width=200)).renderText('ACADEMIC   SCHEDULE') + "\033[0m\033[F\033[F")
    with codecs.open("schedule.txt","r",encoding='unicode_escape') as file:
        for line in file:
            r=line.strip()
            print(r)
    try:
        temp = input(Fore.BLUE + "\nUse Ctrl+D to return to previous page." + Fore.RESET)
    except EOFError:
        eofdet(True)
    else:
        view_schedule()

def view_faculty():
    os.system('clear')
    print("\033[1m" + (Figlet(font='big',width=200)).renderText('OUR FACULTY') + "\033[0m\033[F\033[F")
    #0 name, 1 email, 2 pass, 3 code, 4 subject
    temp=[["Name","Subject"]]
    with open("faculty.csv","r") as file:
                for line in file:
                    r=line.rstrip().split(",")
                    temp.append([r[0],r[4]])
    print(tabulate(temp,headers="firstrow",tablefmt="outline"))
    try:
        temp = input(Fore.BLUE + "Use Ctrl+D to return to previous page." + Fore.RESET)
    except EOFError:
        eofdet(True)
    else:
        view_faculty()

def main():
    global sss,stdtemp,logstat,loggedlist,loginfac,sorf
    sss=""
    stdtemp=""
    logstat=False
    loggedlist=[]
    loginfac=False
    sorf=""
    with open("students.csv","r") as file:
        global studrn
        lines=file.readlines()
        try:
            studrn=int(lines[-1].split(",")[-1].strip()[1:])
        except:
            studrn=0
    with open("faculty.csv","r") as file:
        global facurn
        lines=file.readlines()
        try:
            facurn=int(lines[-1].split(",")[-2].strip()[1:])
        except:
            facurn=0
    print("\033[1m" + (Figlet(font='big')).renderText('COLLEGE50') + "\033[0m")
    try:
        usrinp=input("\033[1m\33[F\33[F" + "\n(1) --> Student Registration\n(2) --> Staff Registration"+
                     "\n(3) --> Login\033[1m\n" +
                    Fore.BLUE + "NOTE: \033[0m"+ Fore.BLUE + "Use Ctrl+D to return to previous page." + Fore.RESET + "\n\33[F\33[F\33[F\33[F\33[FEnter a number: \033[0m").strip()
    except EOFError:
        try:
            over=input(Fore.RED + "\n\n\n\n\n\n\033[1mCtrl+D detected.\nRepeat to exit COLLEGE50. \033[0m" + Fore.RESET)
        except EOFError:
            os.system('clear')
            sys.exit(Fore.GREEN + "Thank you for using COLLEGE50.\n\033[1mThis was CS50P.\033[0m" + Fore.RESET)
        else:
            os.system('clear')
            print(Fore.GREEN + "Ctrl+D not detected.\nReturning to Register/Login Page." + Fore.RESET)
            main()
    else:
        try:
            int(usrinp)
        except:
            os.system('clear')
            print(Fore.RED + "Invalid input.\nReprompting." + Fore.RESET)
            main()
        else:
            match(int(usrinp)):
                case 1:
                    os.system('clear')
                    student()
                case 2:
                    os.system('clear')
                    faculty()
                case 3:
                    os.system('clear')
                    login()
                case _:
                    os.system('clear')
                    print(Fore.RED + "Invalid input.\nReprompting." + Fore.RESET)
                    main()

if __name__=="__main__":
    main()

#num=input("Hello\nmy\n\nname\33[Fdead")
#                    ^^^^^^^^     ^^^^
#                    last line    2nd last(input comes in front of this)

#print('\003[3m' + 'Your text here' + '\033[0m')
#for bold text
