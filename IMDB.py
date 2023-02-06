import sys
import pandas as pd
import numpy as np
print( f"Python {sys.version}\nPandas {pd.__version__}\nNumPy {np.__version__}" ) 
# Load the pokemon dataset
df = pd.read_csv('https://raw.githubusercontent.com/pongsapaks/DADS5001/main/movie_metadata.csv?token=GHSAT0AAAAAAB6LQAJQITJGOD32HZ4VFQDEY7ALARA')  
df