import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re
import emoji
import streamlit as st

## Title of the dashboard
## Caption of the dashboard

##LOAD the dataset
df = pd.read_csv("whatsapp_data.csv")
    ## Change the main columns into different columns
df['Date2'] = pd.to_datetime(df['Date'], format='%d.%m.%y').dt.strftime('%Y-%m-%d')
df['Year'] = pd.to_datetime(df['Date2']).dt.year
df['Month'] = pd.to_datetime(df['Date2']).dt.month
df['Name'] = df['Name'].str.strip()
    ## delete the rows with a value of 2023 in the "Year" column of a DataFrame
df = df[df['Year']!=2023]
    ## create two datasets
msg_stephie= df[df['Name'] =='Stephie']
msg_janine= df[df['Name'] =='Janine']

# Grouping the data by year and counting the number of occurrences
stephie_counts = msg_stephie.groupby('Year').count()['Text']
janine_counts = msg_janine.groupby('Year').count()['Text']

fig, ax = plt.subplots(figsize=(10, 6))
# Plotting the data on the same graph
plt.plot(stephie_counts.index, stephie_counts, label='Partner 1')
plt.plot(janine_counts.index, janine_counts, label='Partner 2')

# Adding labels and title to the plot
plt.xlabel('Jahr')
plt.ylabel('Anzahl')
plt.title('Whatsapp-Kommunikation im Wandel')

# Adding a legend
plt.legend()

# Adding vertical lines
# vertical_lines = [2018, 2019, 2020]  # Example x-values where vertical lines should be added

# for line in vertical_lines:
#     ax.axvline(x=line, color='green', linestyle='--')

# Adding an arrow with description
## ZUSAMMENGEZOGEN Ende 2017
arrow1_x = 2018  # Example x-value where the arrow should point
arrow1_y = 5200   # Example y-value where the arrow should point

arrow1_text = 'Umzug'  # Description for the arrow

ax.annotate(arrow1_text,
            xy=(arrow1_x, arrow1_y),
            xytext=(arrow1_x - 1.0, arrow1_y + 50),  # Position of the text
            arrowprops=dict(arrowstyle='->'),
            fontsize=12)

## HOCHZEIT
arrow2_x = 2019  # Example x-value where the arrow should point
arrow2_y = 4900   # Example y-value where the arrow should point

arrow2_text = 'Hochzeit'  # Description for the arrow

ax.annotate(arrow2_text,
            xy=(arrow2_x, arrow2_y),
            xytext=(arrow2_x + 0.2, arrow2_y + 300),  # Position of the text
            arrowprops=dict(arrowstyle='->'),
            fontsize=12)
## GEBURT
arrow3_x = 2020  # Example x-value where the arrow should point
arrow3_y = 1800   # Example y-value where the arrow should point

arrow3_text = 'Geburt'  # Description for the arrow

ax.annotate(arrow3_text,
            xy=(arrow3_x, arrow3_y),
            xytext=(arrow3_x + 0.5, arrow3_y + 800),  # Position of the text
            arrowprops=dict(arrowstyle='->'),
            fontsize=12)
# Displaying the plot
plt.show()


with st.container():
    