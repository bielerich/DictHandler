#!/usr/bin/python

import sys
sys.path.insert(0, ".")
import DictHandler as dh


def main():

    string      ="reading dict"
    print(string)

    #### read stl files from constant/STL and write matrices
    dict_name   = 'exampleDict'
    DICT    = dh.DictHandler()
    DICT.readDict(dict_name)

    print(DICT.dict)
    
    
if __name__ == "__main__":
    main()

