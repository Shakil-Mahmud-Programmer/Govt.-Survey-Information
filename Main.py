import matplotlib.pyplot as plt, pandas as pd
gdp=pd.read_csv("file/data-gdp.csv")
population=pd.read_csv("file/data-population.csv")
accident=pd.read_csv("file/data-accident.csv")

plt.style.use('seaborn')
fig,ax=plt.subplots(3,1)
fig.suptitle('GDP, Population & Accident Rate\nby Shakil Mahmud',color='purple',size=14)
fig.tight_layout(pad=2)

ax[0].set_title('GDP Growth Rate',color='green',size=10)
ax[0].plot(gdp['Year'],gdp['GDP Growth Rate'],color='green',marker='o',markersize=3,linewidth=0.5,label='GDP')
ax[0].set_xlabel('Year',color='green',size=9)
ax[0].set_ylabel('Rate',color='green',size=9)
ax[0].legend()

ax[1].set_title('Population Growth Rate',color='red',size='10')
ax[1].plot(population['Year'],population['Population'],color='red',marker='o',markersize=2,linewidth=0.5,label='Population')
ax[1].plot(population['Year'],population['Male'],color='blue',marker='o',markersize=2,linewidth=0.5,label='Male')
ax[1].plot(population['Year'],population['Female'],color='maroon',marker='o',markersize=2,linewidth=0.5,label='Female')
ax[1].set_xlabel('Year',color='red',size=9)
ax[1].set_ylabel('Rate',color='red',size=9)
ax[1].legend()

ax[2].set_title('Accident Rate',color='blue',size='10')
ax[2].plot(accident['Year'],accident['Number of Accidents'],color='blue',marker='o',markersize=2,linewidth=0.5,label='Accidents')
ax[2].plot(accident['Year'],accident['Injury'],color='maroon',marker='o',markersize=2,linewidth=0.5,label='Injury')
ax[2].plot(accident['Year'],accident['Death'],color='red',marker='o',markersize=2,linewidth=0.5,label='Death')
ax[2].set_xlabel('Year',color='blue',size=9)
ax[2].set_ylabel('accidents',color='blue',size=9)
ax[2].legend()

plt.show()