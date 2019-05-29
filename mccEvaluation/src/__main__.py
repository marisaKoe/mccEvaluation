'''
Created on 28.05.2019

@author: marisakoe

evaluate the mcc scores to find the most optimal method
'''

import glob
from collections import defaultdict

def read_files(method):
    '''
    read all files from a folder for a specific method.
    :param method: the name of the method block 
    :return mcc_dict: dict with key=concept value=dict with key=method value=mcc_score
    :return eval_dict: dict with key=method value=o (int)
    '''
    ##get all the files from the folder
    files = glob.glob("input/"+method+"/*.csv")
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
            concept = l[0].split("+")[0].split("_")[-1]
            mcc_score=float(l[1])
            mcc_dict[concept][method]=mcc_score
    

    return mcc_dict, eval_dict

def find_optimal_method(method):
    '''
    for each concept, get the highest mcc score and the method
    count the number of best concepts for each method
    the method with the highest number of best concepts is the most optimal method
    :param metohd: name of the method block
    :return dict: eval
    '''
    mcc_dict, eval_dict = read_files(method)

    for concept, score_dict in mcc_dict.items():
        method_max_score = max(score_dict, key=lambda k: score_dict[k])
        eval_dict[method_max_score]+=1
    
    print eval_dict
    
    f = open("output/"+method+"_finalScores.csv","w")
    for method, score in eval_dict.items():
        f.write(method+"\t"+str(score)+"\n")
    f.close()
        
                
    





if __name__ == '__main__':
    ##methods names: DBcog, DBwords, CBml, CBmb
    #read_files("mccPMI")
    list_methods=["DBcog","DBwords"]
    for method in list_methods:
        find_optimal_method(method)
    
    
    
    