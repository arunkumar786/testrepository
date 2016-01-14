'''
Created on 10-Jan-2016

@author: root
'''
from csvmodules.employeeDetails import empCredentialList

empCredentialObjList = []
class EmployeeCredentials(object):
    
    def __init__(self):
        
        self.eName = ""
        self.ePassword = ""
        self.eprofile = {}
        
class EmployeeProfile(object):
    
    def __init__(self):
        
        self.eProfileName = ""
        self.eProfileAttr = []
# iterating over the employeeCredentials Attributes
for ecred in empCredentialList:
    
    # creating the object for every employee row.
    empCredObj = EmployeeCredentials()
    
    # here why this logic is we have every list as
    # Ex:[(empprofileName, arun), (ename,arun),(eadd,bang)]
    # so prepare dictionary for every row and adding to the
    # every object.
    empCredentialDict = {}
    
    for k,v in ecred:
        
        empCredentialDict[k] = v
        
        
    empCredObj.eName = empCredentialDict['ename']
    empCredObj.ePassword = empCredentialDict['epassword']
    empCredentialObjList.append(empCredObj)

# for i in empCredentialObjList:
#     print vars(i)
        
