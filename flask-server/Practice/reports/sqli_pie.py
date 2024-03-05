import matplotlib.pyplot as plt
class SqlPie:
    def __init__(self,types_of_injection_possible):
         self.types_of_sql_possible = types_of_injection_possible
     
    def sql_injection_draw_pie(self):
                labels = ["sql_url_based","Blind Error Based","Blind Time Based"]
                share = [1,1,1]

                explode = self.types_of_sql_possible
                colors = ['red' if e > 0 else 'green' for e in explode]

                plt.style.use("ggplot")
                fig, ax = plt.subplots()
                ax.pie(x=share, explode=explode, labels=labels, autopct="%.2f%%", shadow=True, startangle=90,colors=colors)
                ax.axis('equal')
                ax.legend(loc="upper left")

                # Add a large A+ label in the center of the pie chart

                # Save the figure as an image file (e.g., PNG)
                fig.savefig('sql_injection_pie.png')