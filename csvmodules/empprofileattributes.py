'''
Created on 10-Jan-2016

@author: root
'''
from csvmodules.employeeDetails import empProfileAttrList
from csvmodules.empcredentials import empCredentialObjList, EmployeeProfile

empProfileObjList = []

class EmpProfileAttributes(object):
    """
    Class deals with the Employee Profile Attributes.
    """
    def __init__(self):
        
        self.eprofileName = ""
        self.eName = ""
        self.eAdd = ""
        self.eDob = ""
        self.eId = ""
        self.eSal = ""

# iterating over the employeeProfile Attributes
for eproattr in empProfileAttrList:
    
    # creating the object for every employee row.
    empProObj = EmpProfileAttributes()
    
    # here why this logic is we have every list as
    # Ex:[(empprofileName, arun), (ename,arun),(eadd,bang)]
    # so prepare dictionary for every row and adding to the
    # every object.
    empProfileDictionary = {}
    
    for k,v in eproattr:
        
        empProfileDictionary[k] = v
        
    empProObj.eprofileName = empProfileDictionary['eprofile']
    empProObj.eName = empProfileDictionary['ename']
    empProObj.eAdd = empProfileDictionary['eadd']
    empProObj.eDob = empProfileDictionary['edob']
    empProObj.eId = empProfileDictionary['eid']
    empProObj.eSal = empProfileDictionary['esal']
    empProfileObjList.append(empProObj)
    
# for i in empProfileObjList:
#     print vars(i)
    
# final employee objects by creating a common Profile class.
# comparing both credentialsObject and ProfileAttr objects
# to get profile name.if exists adding to the profile class
# object.
final_emp_list = []
for creObj in empCredentialObjList:
    profileNameObj = EmployeeProfile()
    for proObj in empProfileObjList:
        
        if creObj.eName in proObj.eName:
            
            profileNameObj.eProfileName = proObj.eName
            profileNameObj.eProfileAttr.append(proObj)
            profileNameObj.eProfileAttr.append(creObj)
            final_emp_list.append(profileNameObj)
            
for i in final_emp_list:
    for j in  i.eProfileAttr:
          
        print vars(j)

    print vars(i)             
            
    