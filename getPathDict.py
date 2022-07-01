#! /usr/bin/python

#
# Description: 
# ================================================================
# Time-stamp: "2021-11-03 02:35:39 trottar"
# ================================================================
#
# Author:  Richard L. Trotta III <trotta@cua.edu>
#
# Copyright (c) trottar
#
from .pathing import SetPath

HCANAPATH=SetPath.getPath("HCANAPATH")
REPLAYPATH=SetPath.getPath("REPLAYPATH")
UTILPATH=SetPath.getPath("UTILPATH")
PACKAGEPATH=SetPath.getPath("PACKAGEPATH")
OUTPATH=SetPath.getPath("OUTPATH")
ROOTPATH=SetPath.getPath("ROOTPATH")
REPORTPATH=SetPath.getPath("REPORTPATH")
CUTPATH=SetPath.getPath("CUTPATH")
PARAMPATH=SetPath.getPath("PARAMPATH")
SCRIPTPATH=SetPath.getPath("SCRIPTPATH")
USER=SetPath.getPath("USER")
HOST=SetPath.getPath("HOST")

BashPathEntry=("%s %s %s %s %s %s %s %s %s %s %s %s" % (HCANAPATH, REPLAYPATH, UTILPATH, PACKAGEPATH, OUTPATH, ROOTPATH, REPORTPATH, CUTPATH, PARAMPATH, SCRIPTPATH, USER, HOST))
print(BashPathEntry)
