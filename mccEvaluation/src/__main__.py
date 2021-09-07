'''
Created on 28.05.2019

@author: marisakoe

evaluate the mcc scores to find the most optimal method
'''

import glob
from collections import defaultdict

def read_files_DB():
    '''
    read all files from a folder for the distance based method
    :return mcc_dict: dict with key=concept value=dict with key=method value=mcc_score
    :return eval_dict: dict with key=method value=o (int)
    '''
    ##get all the files from the folder
    files = glob.glob("input/DB/*.csv")
    ##initialize dict with key = concept value = dict with key=method value=mcc_score
    mcc_dict = defaultdict(lambda: defaultdict(float))
    eval_dict = defaultdict(int)
    for fileName in files:
        
        f = open(fileName)
        raw_data = f.readlines()
        f.close()
        method1 = fileName.split(".")[0].split("/")[-1].split("+")[-1]
        print method1
        eval_dict[method1]=0
        
        for l in raw_data:
            l = l.split("\t")
            concept = l[0].split("+")[0].split("_")[-1]

            mcc_score=float(l[1])
            mcc_dict[concept][method1]=mcc_score
    

    return mcc_dict, eval_dict

def read_files_ML():
    '''
    read all files from a folder for the maximum likelihood method.
    :return mcc_dict: dict with key=concept value=dict with key=method value=mcc_score
    :return eval_dict: dict with key=method value=o (int)
    '''
    ##get all the files from the folder
    files = glob.glob("input/ML/*.csv")
    ##initialize dict with key = concept value = dict with key=method value=mcc_score
    mcc_dict = defaultdict(lambda: defaultdict(float))
    eval_dict = defaultdict(int)
    for fileName in files:
        
        f = open(fileName)
        raw_data = f.readlines()
        f.close()
        method = fileName.split(".")[0].split("/")[-1].split("+")[-1]
        eval_dict[method]=0
        
        for l in raw_data:
            l = l.split("\t")
            if method == "Tcoffee":
                concept = l[0].split("_")[0]
                mcc_score=float(l[1])
                
                mcc_dict[concept][method]=mcc_score
            else:
                concept = l[0].split("_")[-1]
                #print concept

                mcc_score=float(l[1])
                mcc_dict[concept][method]=mcc_score
    

    return mcc_dict, eval_dict

def read_files_MB():
    '''
    read all files from a folder for the maximum likelihood method.
    :return mcc_dict: dict with key=concept value=dict with key=method value=mcc_score
    :return eval_dict: dict with key=method value=o (int)
    '''
    ##get all the files from the folder
    files = glob.glob("input/MB/*.csv")
    ##initialize dict with key = concept value = dict with key=method value=mcc_score
    mcc_dict = defaultdict(lambda: defaultdict(float))
    eval_dict = defaultdict(int)
    for fileName in files:
        
        f = open(fileName)
        raw_data = f.readlines()
        f.close()
        method = fileName.split(".")[0].split("/")[-1].split("+")[-1]
        print method
        eval_dict[method]=0
        
        for l in raw_data:
            l = l.split("\t")
            if method == "tcoffee" or method=="PMICog":
                concept = l[0].split("_")[0]
                mcc_score=float(l[1])
                
                mcc_dict[concept][method]=mcc_score
            else:
                concept = l[0].split("_")[-1]

                mcc_score=float(l[1])
                mcc_dict[concept][method]=mcc_score
    

    return mcc_dict, eval_dict

def find_optimal_method(mcc_dict, eval_dict, method):
    '''
    for each concept, get the highest mcc score and the method
    count the number of best concepts for each method
    the method with the highest number of best concepts is the most optimal method
    :param metohd: name of the method block
    :return dict: eval
    '''
    for concept, score_dict in mcc_dict.items():
        method_max_score = max(score_dict, key=lambda k: score_dict[k])
        eval_dict[method_max_score]+=1
    

    
    f = open("output/"+method+"_finalScores.csv","w")
    for method, score in eval_dict.items():
        f.write(method+"\t"+str(score)+"\n")
    f.close()
        
                
    





if __name__ == '__main__':
    ##methods names: DBcog, DBwords, CBml, CBmb
    #list_methods=["DBcog","DBwords"]
    list_methods=["MB"]
    for method in list_methods:
        if method == "DB":
            mcc_dict, eval_dict = read_files_DB()
            find_optimal_method(mcc_dict, eval_dict, method)
        elif method =="ML":
            mcc_dict, eval_dict = read_files_ML()
            find_optimal_method(mcc_dict, eval_dict, method)
        elif method == "MB":
            mcc_dict, eval_dict = read_files_MB()
            find_optimal_method(mcc_dict, eval_dict, method)
        
        
    
    
    
