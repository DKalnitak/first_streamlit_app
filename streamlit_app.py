import streamlit
import pandas
import requests
import snowflake.connector
#import one more library we will need to use this in our control of flow changes
from urllib.error import URLError
# url error for error message handling

streamlit.title('My Parents New Healthy Diner')
streamlit.header('breakfast favorites')
streamlit.text('🥣 omega meal & blueberry oatmeal')
streamlit.text('🥗  kale,spinach & rocket smoothie')
streamlit.text('🐔 hard-boiled free-range egg')
streamlit.text('🥑🍞 avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#import pandas
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

"""
# anew section to display fruity vice api response
fruit_choice=streamlit.text_input('what fruit would you like information about?','Kiwi')
streamlit.write('The user entered',fruit_choice)

#import requests
fruityvice_response=requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)


#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/kiwi")
#streamlit.text(fruityvice_response.json()) just writes data to the screen

# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)
"""


# writing code using try and except
#anew section to display fruity vice api response
streamlit.header('fruityvice fruit advice!')
try:
  fruit_choice=streamlit.text_input('what fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("please select a fruit to get information.")
  else:
    fruityvice_response=requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
    fruityvice_normalized=pandas.json_normalize(fruityvice_response.json())
    streamlit.dataframe(fruityvice_normalized)
except URLError as e:
  streamlit.error()

#create the repeatable code block(called a function)
def get_fruityvice_data(this_fruit_choice):
  fruityvice_response=requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
  fruityvice_normalized=pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalized
#new section to display fruityvice api
streamlit.header('fruityvice fruit advice!')
try:
  fruit_choice=streamlit.text_input('what fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("please select a fruit to get information.")
  else:
    back_from_function=get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)

  





# dont run
streamlit.stop()
#import snowflake.connector
#connecting streamlite to snowflake
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)


#accessing a snowflake table from streamlit

my_cnx=snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur=my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_row=my_cur.fetchone()
streamlit.text("The fruit load lst contains:")
streamlit.text(my_data_row)

#accessing a snowflake table from streamlit
#to make little nicer

my_cnx=snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur=my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_row=my_cur.fetchone()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_row)

#to fetch all rows
my_cur.execute("select * from fruit_load_list")
my_data_row=my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_row)

# add a new section to display fruit 
add_new_fruit=streamlit.text_input('what fruit would you like to add?','jackfruit')
streamlit.write('Thanks for adding',add_new_fruit)
#this will not run now whenever u made changes in streamlit it add value to table
my_cur.execute("insert into fruit_load_list values('from streamlit')")

