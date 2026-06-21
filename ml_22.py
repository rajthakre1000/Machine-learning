# pip install ydata-profiling
# installing for panda profiling
import seaborn as sns 
flights = sns.load_dataset('flights')
from pandas_profiling import ProfileReport
prof = ProfileReport(flights)
prof.to_file(output_file='ml_22_profiling.html')
 