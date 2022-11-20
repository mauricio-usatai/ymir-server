import pandas as pd
from .solution import Solution

class DataSetRowAppend(Solution):
    def apply(self, datasets):
        d1, d2 = datasets
        df1 = pd.DataFrame(d1)
        df2 = pd.DataFrame(d2)

        df = df1.append(df2).reset_index()
        df = df.rename(columns={'A': 'Gender', 'B': 'Age'})
        number_of_females = df[df['Gender'] == 'female']['Gender'].count()
        return number_of_females