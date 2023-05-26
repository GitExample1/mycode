#!/usr/bin/python3

# parse keystone.common.wsgi and return number of failed login attempts
loginfail = 0 # counter for fails
loginsuccess = 0 # counter for successful login
failedip = []
# open the file for reading
with open("/home/student/mycode/attemptlogin/keystone.common.wsgi") as kfile:

    # loop over the file
    for line in kfile:
        # if this 'fail pattern' appears in the line...
        if "- - - - -] Authorization failed" in line:
            loginfail += 1 # this is the same as loginfail = loginfail + 1
            failedlines = line.split(" ")
            failedip.append(failedlines[-1])
            

        # if 'successful patter' appears in the line
        elif "-] Authorization failed" in line: 
            loginsuccess =+ 1


print("The number of failed log in attempts is", loginfail)
print("IP address for failed log in attempts are:", failedip)
print("The number of successful logins: ", loginsuccess)
