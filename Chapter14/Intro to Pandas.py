# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import pandas as pd
ts = pd.read_csv('Gold.csv', index_col=0, parse_dates=True)
ts

# <codecell>

ts.plot()

# <codecell>

ts["2006":"2007"].plot(color = "green")

# <codecell>

ts_res = ts.resample("A")
ts_res.plot(style='g--')

# <codecell>

ts_res = ts.resample("A", how=["mean", np.max, np.min])
ts_res.plot(subplots=True)
ts_res.plot()

# <codecell>

iris = pd.read_csv("iris.csv")
pd.tools.plotting.radviz(iris, "name")

# <codecell>

iris.head()

# <codecell>

iris.describe()

# <codecell>

iris.groupby("name").sum()

# <codecell>

iris.groupby("name").max()

# <codecell>

iris.groupby("name").min()

# <codecell>

iris.groupby("name").describe()

# <codecell>

iris["SepalLength"].corr(iris["PetalLength"])

# <codecell>

iris.corr()

# <codecell>


