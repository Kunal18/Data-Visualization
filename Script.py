import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
print("Setup Complete")

# Set up code checking
from learntools.core import binder
binder.bind(globals())
from learntools.data_viz_to_coder.ex7 import *
print("Setup Complete")


# ## Step 2: Specify the filepath
my_filepath = "../input/fivethirtyeight-comic-characters-dataset/dc-wikia-data.csv"
my_marvel_filepath = "../input/fivethirtyeight-comic-characters-dataset/marvel-wikia-data.csv"


my_data = pd.read_csv(my_filepath)
my_marvel_data = pd.read_csv(my_marvel_filepath)


# Print the first five rows of the data
my_data.head()
my_marvel_data.head()

# ## Step 4: Visualize the data
plt.rcParams['figure.figsize'] = (20, 8)
plt.style.use('fivethirtyeight')

my_data['APPEARANCES'].fillna(0, inplace = True)
my_marvel_data['APPEARANCES'].fillna(0, inplace = True)

import warnings
warnings.filterwarnings('ignore')

plt.subplot(1, 2, 1)
sns.kdeplot(my_data['APPEARANCES'], color = 'green')
plt.title('DC')

plt.subplot(1, 2, 2)
sns.kdeplot(my_marvel_data['APPEARANCES'], color = 'skyblue')
plt.title('Marvel')

plt.suptitle('Appearances comparison vs DC and Marvel', fontsize = 20)
plt.show()
