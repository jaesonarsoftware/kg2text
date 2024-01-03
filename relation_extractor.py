import os
import subprocess
import glob
import pandas as pd

def Stanford_Relation_Extractor():

    
    print('Relation Extraction Started')
    origCwd = os.getcwd()
    os.chdir(origCwd + '/stanford-openie')
    for f in glob.glob(origCwd + "/data/output/kg/*.txt"):   
       
        print("Extracting relations for " + f.split("/")[-1])  
        p = subprocess.Popen(['./process_large_corpus.sh',f,f + '-out.csv'], stdout=subprocess.PIPE)

        output, err = p.communicate()
   

    print('Relation Extraction Completed')


if __name__ == '__main__':
    Stanford_Relation_Extractor()
