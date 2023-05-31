#!/usr/bin/python3
## Try a real world test with getpass

## import Paramiko so we can talk SSH
import paramiko # allows Python to ssh
import os # low level operating system commands
import getpass # we need this to accept passwords


def main():
    ## where to connect to
    t = paramiko.Transport("10.10.2.3", 22) ## IP and port of bender
    
    ## how to connect (see other labs on using id_rsa private / public keypairs)
    t.connect(username="bender", password=getpass.getpass()) # notice the password references getpass
    
    ## Make an SFTP connection object
    sftp = paramiko.SFTPClient.from_transport(t)
    
    ## iterate across the files within directory
    for x in os.listdir("/home/student/filestocopy/"): # iterate on directory contents
      if not os.path.isdir("/home/student/filestocopy/"+x): # filter everything that is NOT a directory
        sftp.put("/home/student/filestocopy/"+x, "/tmp/"+x) # move file to target location

    
    ## close the connection
    sftp.close() # close the connection
if __name__ == "__main__":
    main()
 
