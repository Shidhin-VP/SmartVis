import pandas as pd
import plotly.express as px
from itertools import combinations, permutations

def visualizeEverything(df,maxPermutations=None,maxGraph=None,permute=True):
    try:
        plottedPer=1
        plottedGraph=1
        dfNew=df.copy()
        columns=dfNew.select_dtypes(include="object").columns
        for i in columns:
            if dfNew[i].nunique()<=20:
                dfNew[i]=pd.factorize(df[i])[0]
            else: 
                dfNew.drop(i,axis=1,inplace=True)
        finColumns=list(dfNew.select_dtypes(include='number').columns)
        print(f"Plotting for these below Columns:\n{finColumns}")
        finColumns=list(permutations(finColumns,2) if permute==True else combinations(finColumns,2))
        second=finColumns[0][1]
        for i, j in finColumns:
            if (maxGraph is not None and maxPermutations is None and plottedGraph<=maxGraph) or (maxGraph is None and maxPermutations is not None and plottedPer<=maxPermutations):
                if i==second:
                    if plottedPer<maxPermutations:
                        fig=px.scatter(dfNew,x=i,y=j,title=f"Scatter Plot: {i.upper()} with {j.upper()}")
                        fig.show()
                    plottedPer+=1
                    second=j
                    continue
                fig=px.scatter(dfNew,x=i,y=j,title=f"Scatter Plot: {i.upper()} with {j.upper()}")
                fig.show()
                plottedGraph+=1 if maxGraph is not None else plottedGraph

            elif (maxGraph is not None and maxPermutations is not None):
                if i == second:
                    if plottedPer<maxPermutations:
                        fig=px.scatter(dfNew,x=i,y=j,title=f"Scatter Plot: {i.upper()} with {j.upper()}")
                        fig.show()
                    plottedPer+=1
                    second=j
                else:
                    if plottedGraph>maxGraph:
                        continue
                    else:
                        fig=px.scatter(dfNew,x=i,y=j,title=f"Scatter Plot: {i.upper()} with {j.upper()}")
                        fig.show()
                        plottedGraph+=1

            else:
                fig=px.scatter(dfNew,x=i,y=j,title=f"Scatter Plot: {i.upper()} with {j.upper()}")
                fig.show()
    except Exception as e:
        print(f"Error: {e}")
