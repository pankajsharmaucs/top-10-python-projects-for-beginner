from pytrends.request import TrendReq
import pandas as pd

pytrends = TrendReq(hl='en-US', tz=360)

keywords = pytrends.suggestions(keyword='Business Intelligence')
df = pd.DataFrame(keywords)
print(df)