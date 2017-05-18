import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf

data = pd.read_csv('Advertising.csv')


x = data[['TV','Radio','Newspaper']]
y = data['Sales']


plt.figure(figsize=(9,12))
plt.subplot(311) 
plt.plot(data['TV'], y, 'ro')
plt.title('TV')
plt.grid()
plt.subplot(312) 
plt.plot(data['Radio'], y, 'g^') 
plt.title('Radio')
plt.grid()
plt.subplot(313) 
plt.plot(data['Newspaper'], y, 'b*')
plt.title('Newspaper')
plt.grid()
plt.tight_layout()
plt.show()

