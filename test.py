#import cirpy
import numpy as np
import pandas as pd
import pubchempy as pcp
#from name2pdb import *
#import cirpy
#import pandas as pd
def name2molecule(oname,smiles_code):
       oname=''.join(oname.split())
       pdbfile = cirpy.resolve(smiles_code, 'pdb')
       pdb_output = open('PDB/'+oname + '.pdb', "w+")
       pdb_output.write(pdbfile)
       pdb_output.close()
       ans=True
       return None
df=pd.read_csv('SAMPL4.csv')
for oname,smiles in zip(df.NAME,df.SMILES):
	print oname,smiles
	name2molecule(oname,smiles)
