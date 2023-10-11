import streamlit

streamlit.title('My Parents New Healthy Diner')
streamlit.header('breakfast favorites')
streamlit.text('🥣 omega meal & blueberry oatmeal')
streamlit.text('🥗  kale,spinach & rocket smoothie')
streamlit.text('🐔 hard-boiled free-range egg')
streamlit.text('🥑🍞 avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

# Let's put a pick list here so they can pick the fruit they want to include 

stremlit.multiselect("pick some fruits:",list(my_fruit_list.index))

# Display the table on the page.




