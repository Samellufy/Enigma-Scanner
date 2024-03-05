import matplotlib.pyplot as plt

labels = ["Strict-Transport-Security", "Content-Security-Policy", "X-Frame-Options", "X-Content-Type-Options", "Referrer-Policy", "Permissions-Policy"]
share = [1, 2, 3, 4, 5, 6]

explode = (0.1, 0, 0, 0, 0)
colors = ['red' if e > 0 else 'green' for e in explode]

plt.style.use("ggplot")
fig, ax = plt.subplots()
ax.pie(x=share, explode=explode, labels=labels, autopct="%.2f%%", shadow=True, startangle=90, colors=colors)
ax.axis('equal')
ax.legend(loc="upper left")

# Add a large A+ label in the center of the pie chart
ax.text(0, 0, 'A+', fontsize=20, color='black', ha='center', va='center')

# Save the figure as an image file (e.g., PNG)
fig.savefig('pie_chart.png')

print("Pie chart saved to pie_chart.png")
