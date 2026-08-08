import matplotlib.pyplot as plt
year = [1950, 1970, 1990, 2010]
pop = [2.519, 3.692, 5.263, 6.972]

# Add more data
year = [1800, 1850, 1900] + year
pop = [1.0, 1.262, 1.650] + pop

plt.scatter(year, pop, s = 1000, c = 'blue', alpha = 0.5)

# Customizing the plot
plt.xlabel('Year')
plt.ylabel('Population')
plt.title('World Population Projection')

# To make the y-axis's label this way: Customized
plt.yticks([0, 2, 4, 6, 8, 10],
           ['0B', '2B', '4B', '6B', '8B', '10B'])   # B stands for Billions
                    # This replaces the [0, 2, 4, 6, 8, 10]

# To add text inside the plot
plt.text(1950, 2.519, 'It just doubled')

# To add grid
plt.grid(True)


plt.show()