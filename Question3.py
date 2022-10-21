#Matplotlib
# 1. Write a Python programming to create a below chart of the popularity of programming Languages.
# 2. Sample data:
# Programming languages: Java, Python, PHP, JavaScript, C#, C++
# Popularity: 22.2, 17.6, 8.8, 8, 7.7, 6.7
import matplotlib.pyplot as plt

prog_languages = ('Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++')
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

explode = (0.1, 0, 0, 0,0,0)
wedge_props = {'linewidth':1,'edgecolor':'black'}
plt.pie(popularity, explode=explode, labels=prog_languages, colors=None,
autopct='%1.1f%%', shadow=True, wedgeprops= wedge_props, startangle=140)

plt.show()