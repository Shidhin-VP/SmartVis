import pandas as pd
import plotly.express as px

def visualizeEverything(df,maxPermutations=None,maxGraph=None,removeSwap=True):
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
        for i in finColumns[:]:
            if maxPermutations is not None and plottedPer>maxPermutations:
                        break
            else:
                for j in finColumns:
                        if maxGraph is not None and plottedGraph>maxGraph:
                            break
                        else:
                            if i!=j:
                                fig=px.scatter(dfNew,x=i,y=j,title=f"Scatter Plot: {i.upper()} with {j.upper()}")
                                fig.show()
                                plottedGraph+=1
                plottedPer+=1
                if maxGraph is not None and maxPermutations is not None:
                     plottedGraph=1
                if removeSwap:
                    finColumns.remove(i)
    except Exception as e:
        print(f"Error: {e}")