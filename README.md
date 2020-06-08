# Visuals-in-python
## Using Seaborn in Python
Seaborn makes visualisation easy. It's build on top of the matplotlib library and is named after a character **S**amuel **No**rman **S**eaborn (sns) in the famous TV Show "The West Wing"
1. Read file in python using ```df = pd.read_csv('path/File.csv')```
2. Have the flavour of the dataset using `df.head`
3. To color category wise, use the category column name in hue aggument: `hue="catrgory_column_name"`, and to present category in certain order in the legend of graph use `hue_order=["list of categories present in category column"]`
4. Decide colour for each category using, eg.  `palette_colors = {"Rural": "green", "Urban": "blue"}`, where Rural and Urban are categories. And then you can use the above pallete in `sns.xyzplot(palette=palette_colors)`
5. To save plots use: `plt.savefig("path/name.png", bbox_inches='tight')`. bbox_inches='tight' will hep save complete lables (long labels) if they are long.
```python
import seaborn as sns
import matplotlib.pyplot as plt
plt.show()
```

    sns.scatterplot(data=, x=, y=)

Count Plots for categorical data counting and plotting:
eg: a list containing gendere (male and female)

    sns.countplot(x=gender)
#### Relational Plots
Scatter plots and line plots are relational plots because the enable us to understand relationship between two variable. However, if you are interested to plot two categories separately, you can use `relplot()` function of python and `row`  or `column` subfuctions.
eg, using tipse dataset of python
```python
import seaborn as sns
import matplotlib.pyplot as plt
tips = sns.load_dataset("tips")
sns.relplot(x="total_bill", y="tip", data=tips, kind="scatter", col = "smoker", col_wrap=2)
plt.show()
```

    col="smoker" ##will plot graphs horizontally
    row="smoker" #will plot graph vertically
    using both will give 4 plots row="smoker", col="time"

The `col_wrap` allows you to define how many subplots you want in a single line.
