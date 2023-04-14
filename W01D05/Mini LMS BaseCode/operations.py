from datetime import datetime,date
import json
import string
import random
from json import JSONDecodeError

def validate_details(Full_Name,Mobile_Number,Email_ID,Password):
    if len(Mobile_Number)==10 and '@' in Email_ID and (len(Full_Name)*len(Mobile_Number)*len(Email_ID)*len(Password))!=0:
        return True
    return False

def AutoGenerate_ModuleID():
    '''Return a autogenerated random Module ID'''
    Module_ID=''.join(random.choices(string.ascii_uppercase+string.digits,k=4))
    return Module_ID

def AutoGenerate_UnitID():
    '''Return a autogenerated random Module ID'''
    Unit_ID=''.join(random.choices(string.ascii_uppercase+string.digits,k=3))
    return Unit_ID

def Register(type,manager_json_file,student_json_file,Full_Name,Mobile_Number,Email,Password):
    '''Register a Program Manager/Student'''
    '''Already Implemented. No need to make changes'''
    ch=validate_details(Full_Name,Mobile_Number,Email,Password)
    if type.lower()=='manager':
        f=open(manager_json_file,'r+')
    else:
        f=open(student_json_file,'r+')
    if ch==True:
        if type.lower()=='manager':
            d={
                "Full Name":Full_Name,
                "Mobile Number":Mobile_Number,
                "Email":Email,
                "Password":Password,
              }
        else:
            d={
                "Full Name":Full_Name,
                "Mobile Number":Mobile_Number,
                "Email":Email,
                "Password":Password,
                "Modules Enrolled":[],
              }
        try:
            content=json.load(f)
            if d not in content:
                content.append(d)
                f.seek(0)
                f.truncate()
                json.dump(content,f)
                f.close()
                return True
        except JSONDecodeError:
            l=[]
            l.append(d)
            json.dump(l,f)
            f.close()
            return True
    else:
        f.close()
        return False
        
def login(type,students_json_file,managers_json_file,email,password):
    '''Return True is successfully logged in else False'''
    '''Already Implemented. No need to make changes'''
    if type.lower()=='student':
        f=open(students_json_file,'r+')
    else:
        f=open(managers_json_file,'r+')
    try:
        content=json.load(f)
    except JSONDecodeError:
        return False
    f.close()
    d=0
    for i in range(len(content)):
        if content[i]["Email"]==email and content[i]["Password"]==password:
            d=1
            break
    if d==1:
        return True
    else:
        return False

def Create_Module(module_json_file,module_ID,module_name,start_date,end_date,list_of_units,created_by):
    '''Already Implemented. No need to make changes''' 
    d={
        "Module ID":module_ID,
        "Module Name":module_name,
        "Module Start Date":start_date,
        "Module End Date":end_date,
        "Units":list_of_units,
        "Created By":created_by
        }
    f=open(module_json_file,'r+')
    try:
        content=json.load(f)
        if d not in content:
            content.append(d)
            f.seek(0)
            f.truncate()
            json.dump(content,f)
    except JSONDecodeError:
        l=[]
        l.append(d)
        json.dump(l,f)
    f.close()
    return True

def Read_Module(module_json_file,module_ID):
    '''View Module Details | Return a list containing the module details of the given Module_ID'''
    '''Already Implemented. No need to make changes'''
    Details=[]
    f=open(module_json_file,'r+')
    content=json.load(f)
    for i in range(len(content)):
        if content[i]["Module ID"]==module_ID:
            Details.append(content[i])
            break
    f.close()
    return Details

def Update_Module(Full_Name,module_json_file,module_ID,detail_to_be_updated,new_value):
    '''Update Module | Update a Module created by Full_Name with the given module_ID'''
    '''Already Implemented. No need to make changes'''
    f=open(module_json_file,'r+')
    content=json.load(f)
    for i in range(len(content)):
        if content[i]["Module ID"]==module_ID and content[i]["Created By"]==Full_Name:
            try:
                a=content[i][detail_to_be_updated]
            except KeyError:
                return False
            content[i][detail_to_be_updated]=new_value
            f.seek(0)
            f.truncate()
            json.dump(content,f)
            f.close()
            return True
    f.close()
    return False

def Delete_Module(Full_Name,module_json_file,module_ID):
    '''Delete a Module with the given module_ID'''
    '''Already Implemented. No need to make changes'''
    f=open(module_json_file,'r+')
    content=json.load(f)
    for i in range(len(content)):
        if content[i]['Module ID']==module_ID and content[i]["Created By"]==Full_Name:
            del content[i]
            f.seek(0)
            f.truncate()
            json.dump(content,f)
            f.close()
            return True
    f.close()
    return False

def Read_Student(student_json_file,Mobile_Number):
    '''View Student Details | Read Students details'''
    '''Write your code below'''
    f=open(student_json_file, "r+")
    content=json.load(f)
    student_list = []
    for i in range(len(content)):
        if content[i]["Mobile Number"] == Mobile_Number:
            student_list.append(content[i])
            break
    f.close()
    return student_list


def Update_Student(student_json_file,Mobile_Number,detail_to_be_updated,new_detail):
    '''Update Student | Update the details of a student based on Mobile Number'''
    '''Write your code below'''
    f=open(student_json_file, "r+")
    content=json.load(f)
    for i in range(len(content)):
        if content[i]["Mobile Number"]==Mobile_Number:
            try:
                content[i][detail_to_be_updated]
            except KeyError:
                f.close()
                return False
            content[i][detail_to_be_updated]=new_detail
            f.seek(0)
            f.truncate()
            json.dump(content, f)
            f.close()
            return True
    f.close()
    return False
    


def Delete_Student(student_json_file,Mobile_no):
    '''Delete the student with the given Mobile_no'''
    '''Write your code below'''
    f=open(student_json_file, "r+")
    content=json.load(f)
    for i in range(len(content)):
        if content[i]["Mobile Number"]==Mobile_no:
            del content[i]
            f.seek(0)
            f.truncate()
            json.dump(content, f)
            f.close()
            return True
    f.close()
    return False

def Create_Unit(unit_json_file,ID,type_of_unit,title,start_time,end_time,scheduled_date):
    '''Create a Unit || Format of date is YYYY-MM-DD , Format of time is HH:MM:SS'''
    '''Write your code below'''

def Read_all_Units(unit_json_file):
    '''View All Units | Return a list of all Units '''
    '''Write your code below'''


def Read_Unit_Details(units_json_file,Unit_ID):
    '''View Unit Details | Return a dictionary of all the details of the unit with the given unit ID'''
    '''Write your code below'''


def Update_Unit(unit_json_file,Unit_ID,detail_to_be_updated,new_detail):
    '''Update the detail to be updated of the unit with given unit id to the new details'''
    '''Write your code below'''

    
def Delete_Unit(unit_json_file,Unit_ID):
    '''Delete the unit with the given unit id'''
    '''Write your code below'''


def Enroll_in_module(students_json_file,Mobile_Number,Module_Id):
    '''Enroll a Student | Enroll the student with given Mobile Number in the module with given Module ID || Return True if successful else False'''
    '''Write your code below'''


def Read_all_created_modules(modules_json_file,Full_name):
    '''Return a list of all modules created by logged in Program Manager'''
    '''Already Implemented. No need to make changes.'''
    l=[]
    f=open(modules_json_file,'r')
    content=json.load(f)
    for i in range (len(content)):
        if content[i]["Created By"]==Full_name:
            l.append(content[i])
    return l

def Read_all_enrolled_modules(students_json_file,Full_Name):
    '''View My Modules | Return a list of all enrolled modules of the student with Full name as Full_Name'''
    '''Already implemented, no need to make changes'''
    details=[]
    f=open(students_json_file,'r')
    try:
        content=json.load(f)
        f.close()
    except KeyError:
        f.close()
        return details
    for i in range(len(content)):
        if content[i]["Full Name"]==Full_Name:
            details=content[i]["Modules Enrolled"]
            return details
    return details


def View_all_modules(modules_json_file,Full_Name,upcoming,ongoing,completed):
    '''View all Modules Functionlity || Return true if modules exist else False'''
    '''Already Implemented. No need to make changes'''
    date_today=str(date.today())
    f=open(modules_json_file,'r+')
    try:
        content=json.load(f)
        f.close()
    except JSONDecodeError:
        f.close()
        return False
    for i in range(len(content)):
        if content[i]["Created By"]==Full_Name:
            if date_today<content[i]["Module Start Date"]:
                upcoming.append(content[i]["Module ID"])
            elif date_today>=content[i]["Module Start Date"] and date_today<=content[i]["Module End Date"]:
                ongoing.append(content[i]["Module ID"])
            else:
                completed.append(content[i]["Module ID"])
    return True    

def View_Todays_Schedule(list_of_units,units_json_file,upcoming,ongoing,completed):
    ''''View Today's Schedule Functionality'''
    '''Already implemented, no need to make changes'''
    date_today=str(date.today())
    l=list_of_units
    f=open(units_json_file,'r')
    content3=json.load(f)
    f.close()
    for i in range(len(l)):
        for j in range(len(content3)):
            if content3[j]["Unit ID"]==l[i]:
                scheduled_date=content3[j]["Scheduled Date"]
                if date_today>scheduled_date:
                    completed.append(content3[j])
                    break
                elif date_today==scheduled_date:
                    ongoing.append(content3[j])
                elif date_today<scheduled_date:
                    upcoming.append(content3[j])
                    break
    

def Get_Unit_Status(units_json_file,unit_ID):
    '''Already implemented, no need to make changes'''
    date_today=str(date.today())
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    f=open(units_json_file,'r')
    status=""
    try:
        content=json.load(f)
    except JSONDecodeError:
        f.close()
        return status
    f.close()
    for j in range(len(content)):
        if content[j]["Unit ID"]==unit_ID:
            scheduled_date=content[j]["Scheduled Date"]
            start_time=content[j]["Start Time"]
            end_time=content[j]["End Time"]
            if date_today>scheduled_date:
                status="Completed"
                return status
            elif date_today==scheduled_date:
                if current_time>end_time:
                    status="Completed"
                    return status
                elif current_time<start_time:
                    status="Upcoming"
                    return status
                else:
                    status="Ongoing"
                    return status
            elif date_today<scheduled_date:
                status="Upcoming"
                return status
    return status


    