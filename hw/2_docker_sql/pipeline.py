import sys
import pandas as pd 

# when run "docker run -it test:pandas 2024-01-21" 
print(sys.argv) # this will give ['pipeline.py', '2024-01-21']
# 0 is the name of the file, 1 is day
day = sys.argv[1]

print('Job finished for day ', day)