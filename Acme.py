"HELLO EVERYBODY"
"""WITH THE NEXT REPORT WE'RE GOING TO KNOW HOW MANY EMPLOYEES HAVE COINCIDED BETWEEN THEM AT THE OFFICE
IN THE ACME COMPANY, FOR THIS WE'RE GOING TO INSERT THE INFORMATION BY KEYBOARD WHERE THIS WILL BE 
STORED IN A .TXT FILE"""

timFS = 0
timFT = 0
timST = 0
from ast import Continue

print ("THE ACNE COMPANY NEEDS TO KNOW HOW MANY TIMES THEIR EMPLOYEES HAVE COINCIDED")
print ("PLEASE INSERT THE REQUESTED DATA")
first_employee = input("Please insert the First Employee's name: ")
true_false1 = (input("Please tell me if "+ first_employee +" has worked at least a day the last week, YES/NO: "))

while (true_false1 != 'yes') and (true_false1 != 'YES') and (true_false1 != 'no') and (true_false1 != 'NO'):
    print ("you didn't input YES/NO, try again : ")
    true_false1 = (input("Please tell me if "+ first_employee +" has worked at least a day the last week, YES/NO: ")) 
    
if (true_false1 == 'yes') or (true_false1 == 'YES'):
    print ("If there is schedule input this way for example:",'\033[1m' + '(12:00-14:00)' + '\033[0m', "and if there isn't schedule input ",'\033[1m' + '(0)' + '\033[0m')
    monday_first = input("Please input the schedule of Monday :  ")
    tuesday_first = input("Please input the schedule of Tuesday : ")
    wednesday_first = input("Please input the schedule of Wednesday : ")
    thursday_first = input("Please input the schedule of Thurday : ")
    friday_first = input("Please input the schedule of Friday : ")
    saturday_first = input("Please input the schedule of Saturday : ")
    sunday_first = input("Please input the schedule of Sunday : ") 
if (true_false1 == 'no') or (true_false1 != 'NO'):
    Continue
#print (first_employee + " have worked" +"\n"+ "MO : " + monday_first +"\n"+ "TU : " + tuesday_first +"\n"+ "WE : " + wednesday_first +"\n" + "TH : " + thursday_first +"\n"+ "FR : " + friday_first +"\n"+ "SA : " + saturday_first +"\n"+ "SU : " + sunday_first)
second_employee = input("Please insert the Second Employee's name: ")
true_false2 = (input("Please tell me if "+ second_employee +" has worked at least a day the last week, YES/NO: "))

while (true_false2 != 'yes') and (true_false2 != 'YES') and (true_false2 != 'no') and (true_false2 != 'NO'):
    print ("you didn't input YES/NO, try again : ")
    true_false2 = (input("Please tell me if "+ second_employee +" has worked at least a day the last week, YES/NO: "))

if (true_false2 == 'yes') or (true_false2 == 'YES'):
    print ("If there is schedule input this way for example:",'\033[1m' + '(12:00-14:00)' + '\033[0m', "and if there isn't schedule input ",'\033[1m' + '(0)' + '\033[0m')
    monday_second = input("Please input the schedule of Monday :  ")
    tuesday_second = input("Please input the schedule of Tuesday : ")
    wednesday_second = input("Please input the schedule of Wednesday : ")
    thursday_second = input("Please input the schedule of Thurday : ")
    friday_second = input("Please input the schedule of Friday : ")
    saturday_second = input("Please input the schedule of Saturday : ")
    sunday_second = input("Please input the schedule of Sunday : ")
if (true_false2 == 'no') or (true_false2 != 'NO'):
    Continue
#print (second_employee + " have worked" +"\n"+ "MO : " + monday_second +"\n"+ "TU : " + tuesday_second +"\n"+ "WE : " + wednesday_second +"\n" + "TH : " + thursday_second +"\n"+ "FR : " + friday_second +"\n"+ "SA : " + saturday_second +"\n"+ "SU : " + sunday_second)
third_employee = input("Please insert the Third Employee's name: ")
true_false3 = (input("Please tell me if "+ third_employee +" has worked at least a day the last week, YES/NO: "))

while (true_false3 != 'yes') and (true_false3 != 'YES') and (true_false3 != 'no') and (true_false3 != 'NO'):
    print ("you didn't input YES/NO, try again : ")
    true_false3 = (input("Please tell me if "+ second_employee +" has worked at least a day the last week, YES/NO: "))

if (true_false3 == 'yes') or (true_false3 == 'YES'):
    print ("If there is schedule input this way for example:",'\033[1m' + '(12:00-14:00)' + '\033[0m', "and if there isn't schedule input ",'\033[1m' + '(0)' + '\033[0m')
    monday_third = input("Please input the schedule of Monday :  ")
    tuesday_third = input("Please input the schedule of Tuesday : ")
    wednesday_third = input("Please input the schedule of Wednesday : ")
    thursday_third = input("Please input the schedule of Thurday : ")
    friday_third = input("Please input the schedule of Friday : ")
    saturday_third = input("Please input the schedule of Saturday : ")
    sunday_third = input("Please input the schedule of Sunday : ")
#print (third_employee + " have worked" +"\n"+ "MO : " + monday_third +"\n"+ "TU : " + tuesday_third +"\n"+ "WE : " + wednesday_third +"\n" + "TH : " + thursday_third +"\n"+ "FR : " + friday_third +"\n"+ "SA : " + saturday_third +"\n"+ "SU : " + sunday_third)
   
    ##   FIRST EMPLOYEE AND SECOND EMPLOYEE   ##
if (true_false1 == 'yes') or (true_false1 == 'YES') and (true_false2 == 'yes') or (true_false2 == 'YES'):
    timFS = 0 
    Fi_Se = 0
    if monday_first == monday_second and monday_first != "0":
        print(first_employee + " and " + second_employee + " have coincided in the office on monday in this time : " + monday_first )
        timFS = Fi_Se + 1
    if tuesday_first == tuesday_second and tuesday_first != "0":
        print(first_employee + " and " + second_employee + " have coincided in the office on tuesday in this time : " + tuesday_first )
        timFS = timFS + 1
    if wednesday_first == wednesday_second and wednesday_first != "0":
        print(first_employee + " and " + second_employee + " have coincided in the office on wednesday in this time : " + wednesday_first )
        timFS = timFS + 1
    if thursday_first == thursday_second and thursday_first != "0":
        print(first_employee + " and " + second_employee + " have coincided in the office on thursday in this time : " + thursday_first )
        timFS = timFS + 1
    if friday_first == friday_second and friday_first != "0":
        print(first_employee + " and " + second_employee + " have coincided in the office on friday in this time : " + friday_first )
        timFS = timFS + 1
    if saturday_first == saturday_second and saturday_first != "0":
        print(first_employee + " and " + second_employee + " have coincided in the office on saturday in this time : " + saturday_first )
        timFS = timFS + 1
    if sunday_first == sunday_second and sunday_first != "0":
        print(first_employee + " and " + second_employee + " have coincided in the office on sunday in this time : " + sunday_first )
        timFS = timFS + 1
else:
    Continue
    ##   FIRST EMPLOYEE AND THIRD EMPLOYEE   ##
if (true_false1 == 'yes') or (true_false1 == 'YES') and (true_false3 == 'yes') or (true_false3 == 'YES'):
    timFT = 0
    Fi_Th = 0
    if monday_first == monday_third and monday_third != "0":
        print(first_employee + " and " + third_employee + " have coincided in the office on monday in this time : " + monday_third )
        timFT = Fi_Th + 1
    if tuesday_first == tuesday_third and tuesday_third != "0":
        print(first_employee + " and " + third_employee + " have coincided in the office on tuesday in this time : " + tuesday_third )
        timFT = timFT + 1
    if wednesday_first == wednesday_third and wednesday_third != "0":
        print(first_employee + " and " + third_employee + " have coincided in the office on wednesday in this time : " + wednesday_third )
        timFT = timFT + 1
    if thursday_first == thursday_third and thursday_third != "0":
        print(first_employee + " and " + third_employee + " have coincided in the office on thursday in this time : " + thursday_third )
        timFT = timFT + 1
    if friday_first == friday_third and friday_third != "0":
        print(first_employee + " and " + third_employee + " have coincided in the office on friday in this time : " + friday_third )
        timFT = timFT + 1
    if saturday_first == saturday_third and saturday_third != "0":
        print(first_employee + " and " + third_employee + " have coincided in the office on saturday in this time : " + saturday_third )
        timFT = timFT + 1
    if sunday_first == sunday_third and sunday_third != "0":
        print(first_employee + " and " + third_employee + " have coincided in the office on sunday in this time : " + sunday_third )
        timFT = timFT + 1
else:
    Continue
    ##   SECOND EMPLOYEE AND THIRD EMPLOYEE   ##
if (true_false2 == 'yes') or (true_false2 == 'YES') and (true_false3 == 'yes') or (true_false3 == 'YES'):
    Se_Th = 0
    timST = 0
    if monday_second == monday_third and monday_second != "0":
        print(second_employee + " and " + third_employee + " have coincided in the office on monday in this time : " + monday_second )
        timST = Se_Th + 1
    if tuesday_second == tuesday_third and tuesday_second != "0":
        print(second_employee + " and " + third_employee + " have coincided in the office on tuesday in this time : " + tuesday_second )
        timST = timST + 1
    if wednesday_second == wednesday_third and wednesday_second != "0":
        print(second_employee + " and " + third_employee + " have coincided in the office on wednesday in this time : " + wednesday_second )
        timST = timST + 1
    if thursday_second == thursday_third and thursday_second != "0":
        print(second_employee + " and " + third_employee + " have coincided in the office on thursday in this time : " + thursday_second )
        timST = timST + 1
    if friday_second == friday_third and friday_second != "0":
        print(second_employee + " and " + third_employee + " have coincided in the office on friday in this time : " + friday_second )
        timST = timST + 1
    if saturday_second == saturday_third and saturday_second != "0":
        print(second_employee + " and " + third_employee + " have coincided in the office on saturday in this time : " + saturday_second )
        timST = timST + 1
    if sunday_second == sunday_third and sunday_second != "0":
        print(second_employee + " and " + third_employee + " have coincided in the office on sunday in this time : " + sunday_second )
        timST = timST + 1
    
if (true_false1 == 'no') or (true_false2 == 'no') or (true_false3 == 'no') or (true_false1 == 'NO') or (true_false2 == 'NO') or (true_false3 == 'NO'):
    print ("END")
if (true_false1 == 'yes') or (true_false1 == 'YES') and (true_false2 == 'yes') or (true_false2 == 'YES'):
    print(first_employee + " and " + second_employee + " = " , timFS , " times")
if (true_false1 == 'yes') or (true_false1 == 'YES') and (true_false2 == 'yes') or (true_false2 == 'YES'):
    print(first_employee + " and " + third_employee + " = " , timFT , " times")
if (true_false1 == 'yes') or (true_false1 == 'YES') and (true_false2 == 'yes') or (true_false2 == 'YES'):
    print(second_employee + " and " + third_employee + " = " , timST , " times")
    print("END")

##    FILE NAME :  employees.txt  ##
file = open("employees.txt", "w")
file.write("COINCIDENCES ACME EMPLOYEES " + "\n")
file.writelines (first_employee + " and " + second_employee + " = " + str(timFS) + " times" + "\n" )
file.writelines (first_employee + " and " + third_employee + " = " + str(timFT) + " times" + "\n")
file.writelines (second_employee + " and " + third_employee + " = " + str(timST) + " times" + "\n")
file.write("END")