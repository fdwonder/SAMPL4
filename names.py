import pandas as pd
import pubchempy as pcp
df=pd.read_csv('SAMPL4.csv')
for oname in df.NAME:
	cs = pcp.get_compounds(oname, 'name')
	print oname,cs[0].canonical_smiles
df['NSMILES'] = [pcp.get_compounds(oname, 'name')[0].canonical_smiles for oname in df.NAME] 
print df.to_csv(index=False)
