'''
Created on 08-Jan-2016

@author: root
'''
import csv
# i = 0
# open a csv file to read the contents which returns the list of 
# all individual rows
 
with open("/home/aachutha/Desktop/stuff/test.xl.csv",'rb') as csvfile:
    
    csv_file_obj = csv.reader(csvfile)
    
    emp_name_list = []; emp_passwd_list = [];all_list = []
    
    # just calculating the length of the row.
    
    for col_len in csv_file_obj:
        all_list.append(col_len)
        colLength = len(col_len)
    
print "csv reader object list:-----", all_list    
# while i <= colLength:
#      
#     new_list = list()
#     
#     for row in all_list:
#                                     
#         for col in xrange(len(row)):
#               
#             if col == i:
#                   
#                 new_list.append(row[col])
#                 
#     emp_name_list.append(new_list)
#                 
#     i = i + 1
    
#empName, empPass = emp_name_list[0:2]
# zip function to get the list  of tuples
def zipFun(first, second):
    
    return zip(first, second)

# new list to collect the empcredential list.
empCredentialList = []
# collecting all the credential headers from the csv reader object.
empCredentialHeader = all_list[0][:2]

# here the logic is pointing all the rows to 
# credential headers correctly.

for empcreattr in all_list[1:]:
    
    empcreAttr = empcreattr[:2]
    
    empCredentials = zipFun(empCredentialHeader, empcreAttr)
    
    empCredentialList.append(empCredentials)
    
#print empCredentialList

# these are the headers related to the empProfile attributes.
emp_headers = all_list[0][2:]

# list to collect the empProfileAttribute list
empProfileAttrList = []

# here the logic is pointing all the rows to 
# empProfile headers correctly.
for empattr in all_list[1:]:
    
    empAttr = empattr[2:]
    zipped = zipFun(emp_headers, empAttr )
    empProfileAttrList.append(zipped)
    
