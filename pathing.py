#! /usr/bin/python
# Description: This package will perform many tasks required for l-t separation physics analysis 
# Analysis script required dynamically defining pathing...
'''

'''
# ================================================================
# Time-stamp: "2021-11-03 07:58:56 trottar"
# ================================================================
#
# Author:  Richard L. Trotta III <trotta@cua.edu>
#
# Copyright (c) trottar
#
from pathlib import Path
import sys,os,glob

class SetPath():

    def __init__(self, CURRENT_ENV):
        CURRENT_ENV = CURRENT_ENV.replace(os.getlogin(),"${USER}")
        CURRENT_ENV = CURRENT_ENV.split("/UTIL_",1)[0] # Redefine path to hallc_replay_lt (if in replay env)
        CURRENT_ENV = CURRENT_ENV.split("/cut.py",1)[0] # Redefine path to ltsep (if in package env)
        self.CURRENT_ENV = CURRENT_ENV

    def getPath(self,inp_dir,DEBUG=False):

        PACKAGE_ENV = os.path.dirname(os.path.realpath(__file__))
        USER = os.getlogin()
        HOST = os.uname()[1]

        if DEBUG==True:
            print("CURRENT_ENV ",self.CURRENT_ENV)

        path_check = "{}/PATH_TO_DIR".format(PACKAGE_ENV)
        
        for fname in glob.glob(path_check+"/*.path"):
            with open(fname) as f:
                search = f.read()
            if USER == "cdaq":
                if PACKAGE_ENV in search:
                    PATHFILE = fname
            else:
                if self.CURRENT_ENV in search:
                        PATHFILE = fname
        try:
            PATHFILE
        except NameError:
            print("ERROR: PATHFILE not defined. Invalid enviroment...\n\t{}".format(self.CURRENT_ENV))
            sys.exit(1)

        inp_path = open(PATHFILE)

        pathDict = {}
        for line in inp_path:
            line  = line.split("=")
            # Create dictionary of pathing. Assuring that ${USER} is replaced with proper user names
            pathDict.update({line[0].strip().strip("\n") : line[1].strip().strip("\n").replace("${USER}",USER)})
            
        pathDict.update({"USER" : USER})
        pathDict.update({"HOST" : HOST})

        if DEBUG==True:
            print("pathDict ",pathDict)

        inp_path.close()

        return pathDict[inp_dir]

    def checkDir(self,inp_dir):
        if os.path.exists(inp_dir):
            if os.path.islink(inp_dir):
                pass
            elif os.path.isdir(inp_dir):
                pass
            else:
                print ("{} exists but is not a directory or sym link, check your directory/link and try again".format(inp_dir))
                sys.exit(2)
        else:
            print("Output path not found, please make a sym link or directory called OUTPUT in {} to store output").format(UTILPATH.replace(REPLAYPATH+"/",""))
            sys.exit(3)

    def checkFile(self,inp_file):
        if os.path.isfile(inp_file):
            print ("{} exists, processing".format(inp_file))
        else:
            print ("{} not found - do you have the correct sym link/folder set up?".format(inp_file))
            sys.exit(4)
