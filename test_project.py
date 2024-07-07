from project import to_print,chk_det,chk_login
from colorama import Fore
import pytest
def test_to_print():
    assert to_print("stu")==('\033[1m' + '\033[4m' + 'STUDENT REGISTRATION' + '\033[0m'
               + Fore.BLUE + '\033[1m' + '\nKINDLY REMEMBER YOUR REGISTRATION NUMBER' + Fore.RESET + '\033[0m')
    assert to_print("fac")==('\033[1m' + '\033[4m' + 'FACULTY REGISTRATION' + '\033[0m'
               + Fore.BLUE + '\033[1m' + '\nKINDLY REMEMBER YOUR REGISTRATION NUMBER' + Fore.RESET + '\033[0m')
    assert to_print("stulo")=="Student"
    assert to_print("faclo")=="Faculty"
    with pytest.raises(ValueError):
        to_print("cat")
    with pytest.raises(ValueError):
        to_print(2)
    with pytest.raises(ValueError):
        to_print(["cat","DOG"])
    with pytest.raises(ValueError):
        to_print("STULO")
    with pytest.raises(ValueError):
        to_print("FAC")

def test_chk_det():
    assert chk_det("p","pass@cs50")==True
    assert chk_det("p","!9023@college50")==True
    assert chk_det("p","pass cs50")==False
    assert chk_det("p","pass,cs50")==False
    assert chk_det("p","hello, world")==False
    assert chk_det("n","Aadi Joshi")==True
    assert chk_det("n","Dr. Aadi Joshi")==True
    assert chk_det("n","Prof. A. Joshi")==True
    assert chk_det("n","Prof. !!@Aadi")==False
    assert chk_det("n","Aadi19 Joshi")==False
    assert chk_det("e","toaadi@gmail")==False
    assert chk_det("e","toaadi@college50.com")==True
    assert chk_det("e","@college50.com")==False
    assert chk_det("e","toaadi@@gmail.com")==False
    assert chk_det("e","professor.college50@gmail.co.in")==True
    assert chk_det("f",21085)==True
    assert chk_det("f",21086)==False

def test_chk_login():
    assert chk_login("s000",'r')==0
    assert chk_login("s0001",'r')==0
    assert chk_login("cat",'r')==0
    assert chk_login("s00001",'r')==2
    assert chk_login("alice.johnson@example.com",'e','s00001')==[2,"s"]
    assert chk_login("amandac@gmail.com",'e','f00001')==[2,"f"]
    assert chk_login("amandac@gmail.com",'e','f00002')==[1]
    assert chk_login("amandac@gmail",'e','f00002')==[0]
    assert chk_login("College50!@",'p',"alice.johnson@example.com","s")==2
    assert chk_login("College50!@",'p',"michael.smith@mail.com","s")==1
