# Boolean Indexing with Pandas
import pandas as pd

dict = {'name': ["aparna", "pankaj", "sudhir", "Geeku"],
        'degree': ["MBA", "BCA", "M.Tech", "MBA"],
        'score': [90, 40, 80, 98]}

df = pd.DataFrame(dict)
print("the third value in duct:\n", df.loc[3])
print("All dict Value:\n",df)