import cirpy
import sys
import pandas as pd
#molecule = sys.argv[1]
df=pd.read_csv('SAMPL4.csv')
for molecule in df.NAME[:24]: 
	smiles_code = cirpy.resolve(molecule, 'smiles')
	print smiles_code,molecule
	pdbfile = cirpy.resolve(smiles_code, 'pdb')
	oname = ''.join(molecule.split())
	file_output = open(oname + '.pdb', "w+")
	file_output.write(pdbfile)
	file_output.close()
