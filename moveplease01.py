#!/usr/bin/env python3

# standard library imports
import shutil # shell utilities will be used to move files
import os     # provides access to low level os operations 


def main():   # moves and renames file 

    # starts code in home directory
    os.chdir('/home/student/mycode/')

    # moves folder to new location
    shutil.move('raynor.obj', 'ceph_storage/')

    # asks user for new file name
    xname = input('What is the new name for kerrigan.obj? ')

    # renames kerrigan.obj file
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)


main()       # calls main function

