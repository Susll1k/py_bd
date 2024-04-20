import pandas as pd
import numpy
import matplotlib.pyplot as plt

days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
sales = [272, 147, 217, 292, 423, 351, 295]


sale = pd.DataFrame({'День': days, 'Продажи': sales})
print(sale)
mean = sale.loc[:, 'Продажи'].mean()
weighted_mean = numpy.average(sale.drop(columns='День'), axis=0, weights=[1/7]*7)[0]
max = sale.loc[:, 'Продажи'].max()
min = sale.loc[:, 'Продажи'].min()
print(f"Средние: {mean}")
print(f"Средневзвешенные: {weighted_mean}")
print(f"Максимальные: {max}")
print(f"Минимальные: {min}")


plt.plot(days, sales)
plt.plot(days, sales)
plt.plot(days, sales,)
plt.plot(days, sales)

plt.title('MessUUUUUUU')
plt.xlabel('Days')
plt.ylabel('Sales')

plt.show()
