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



my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 

streamlit.multiselect("pick some fruits:",list(my_fruit_list.index))

# Display the table on the page.

streamlit.dataframe(my_fruit_list)


# lets put a pick list so they can pick the fruit they want to include

# streamlit.multiselect("pick some fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])

fruits_selected=streamlit.multiselect("pick some fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show=my_fruit_list.loc[fruits_selected]
# to display table on page
streamlit.dataframe(fruits_to_show)

#new section to display fruityvice api response

streamlit.header("Fruityvice Fruit Advice!")


# anew section to display fruity vice api response
fruit_choice=streamlit.text_input('what fruit would you like information about?','Kiwi')
streamlit.write('The user entered',fruit_choice)

import requests
fruityvice_response=requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)


#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/kiwi")
#streamlit.text(fruityvice_response.json()) just writes data to the screen

# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)





