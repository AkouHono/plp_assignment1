Technologies Used

Python 3
Pandas
Matplotlib
Seaborn
Scikit-learn (for Iris dataset)

Steps in the Notebook

Data Loading & Exploration

Loaded Iris dataset from scikit-learn.

Displayed first few rows and dataset information.

Checked for missing values.

Basic Analysis

Calculated descriptive statistics.

Grouped data by species.

Observed patterns in features.

Data Visualization

Line Chart: Sepal length (first 30 values).

Bar Chart: Average petal length per species.

Histogram: Distribution of sepal length.

Scatter Plot: Sepal length vs Petal length.

Error Handling

Added try/except for dataset loading.

Checked for invalid column references.

Sample Plots

Bar Chart Example:
Average Petal Length per Species

How to Run

Open in Google Colab:


Or clone the repository and run locally:

git clone https://github.com/AkouHono/Week7_Python
cd your-repo
jupyter notebook analysis_notebook.ipynb

Observations & Conclusion

Setosa flowers generally have smaller sepal and petal sizes compared to Versicolor and Virginica.

Virginica species tend to have the largest petal length and width.

The dataset is clean (no missing values) and well-suited for classification problems.