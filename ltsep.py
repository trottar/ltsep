#! /usr/bin/python
#
# Description:
# ================================================================
# Time-stamp: "2021-11-03 04:32:52 trottar"
# ================================================================
#
# Author:  Richard L. Trotta III <trotta@cua.edu>
#
# Copyright (c) trottar
#
        
class Branch(dict):
    '''
    This class, with its findBranch method, will grab the leaves in a branch using uproot package. This takes the tree as an input.
    '''

    def __init__(self,inputTree):
        self.inputTree = inputTree

    def findBranch(self,inputBranch, inputLeaf):
        tree = self.inputTree
        branch = tree.array(inputBranch)
        branch  = list(zip(*branch)) # Match elements to proper leaves
        leafList = tree[inputBranch].interpretation.fromdtype.descr
        i=0
        for name,typ in leafList:
            if name == inputLeaf:
                leaf = name
                leafVal = i
                break
            i+=1
        leafHist = branch[leafVal]

        return np.array(leafHist)

class Root():
    '''    
    This class is for converting files into root files after the analysis steps
    '''

    # Save arrays,lists,etc. from csv to root file as histograms
    def csv2root(self,inputDict,rootName):
        try:
            tmp = ""
            hist_key = []*len(inputDict)
            hist_val = []*len(inputDict)
            for key,val in inputDict.items():
                tmp = "hist_%s" % key
                tmp = TH1F( tmp, '%s' % key, len(val), 0., max(val))
                hist_key.append(tmp)
                hist_val.append(val)

            f = TFile( rootName, 'recreate' )
            for i, evt in enumerate(hist_val):
                for j, hevt in enumerate(hist_val[i]):
                    print(hist_key[i], "-> ", hevt)
                    hist_key[i].Fill(hevt)
                hist_key[i].Write()
 
            f.Write()
            f.Close()
        except TypeError:
            print("\nERROR 1: Only current accepting 1D array/list values\n")

class Equation():
    '''            
    This class stores a variety of equations often used in the KaonLT analysis procedure
    '''

    # Define missing mass calculation
    def missmass():
        print("missmass")

class Misc():
    '''
    This is the most extensive class of the kaonlt package. This class will perform many required tasks
    for doing in depth analysis in python. This class does not require, but will use the pyDict class to
    apply cuts. Set the dictionary to None if no cuts are required.
    '''
    
    def progressBar(self,value, endvalue, bar_length):
        '''
        A simple progress bar to use in loops
        '''

        percent = float(value) / endvalue
        arrow = '=' * int(round(percent * bar_length)-1) + '>'
        spaces = ' ' * (bar_length - len(arrow))
        
        sys.stdout.write(" \r[{0}] {1}%".format(arrow + spaces, int(round(percent * 100))))
        sys.stdout.flush()

