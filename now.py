import numpy as np
from numpy.lib.index_tricks import AxisConcatenator
from numpy.lib.shape_base import apply_along_axis
import pandas as pd
data = { 
        "total_corona_cases":[500, 800, 900], 
        "total_active_cases":[200, 300, 400], 
        "total_corona_deaths":[80, 90, 200] 
        } 
date = ['1-July-2021', '2-July-2021', '3-July-2021'] 
# Write a Python program to get the total corona cases, total_deaths and 
# total active cases with its % increase each with respect to other day .
data1=np.array(data)
das = pd.DataFrame(data,index=date)
print(das)
# total_population = 10000
tc = data1.sum(axis=0)
# tac = data1.sum(axis=1)
# td = data1.sum(axis=2)
print(tc)
# res = tc[0]/td[0]
# res2=tc[1]/td[1]
# res3=tc[2]/td[2]
# final=res/res2
# final2=res2/res3
# final3=res3
# d=final//
# dd= final2//
# ddd=final3//
# print(final,"%")
# print(final2,"%")
# print(final3,"%")