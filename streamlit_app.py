import streamlit
import pandas
import requests
import requests
import requests
import snowflake.connector
#import urllib.error import URLerror
from urllib.error import URLError



streamlit.title('My parents new Healthy Diner')
streamlit.header('🍔Breakfast menu🍔')
streamlit.text('🍱Omega 3 & Blueberry outmeal')
streamlit.text('🫘Kale ,Spinach & Rocket Smoothie')
streamlit.text('🍳🥚Hard-Boiled Free-Range Egg')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')






# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])

fruits_to_show = my_fruit_list.loc[fruits_selected]


# Display the table on the page.

streamlit.dataframe(fruits_to_show)


#import snowflake.connector






#New section to display fruitvice API response

streamlit.header("Fruityvice Fruit Advice!")





fruit_choice = streamlit.text_input('What fruit would you like information about?')
streamlit.write('The user entered ', fruit_choice)


fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)





fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)

fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)

##

#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/")



#create the header repitable code called(a function)

def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalized
  
streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit for information")
  else:
    back_from_function=get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)
except URLError as e:
  streamlit.error();

  
  
  
streamlit.header("The Fruit Load List Contains:")

def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("select * from fruit_load_list")
    return my_cur.fetchall()


# add a button to lode
  
if streamlit.button('Get fruit load list'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows= get_fruit_load_list()
  streamlit.dataframe(my_data_rows)

      
    
    def insert_row_snowflake(new_fruit):
  with my_cnx.cursor() as my_cur:
    my_cur.execute("insert into fruit_load_list values('" + new_fruit + "')")
    return "Thanks for adding" + new_fruit
  
  

    
    
    #  streamlit.header("Fruityvice Fruit Advice!")
#try:
#  fruit_choice = streamlit.text_input('What fruit would you like information about?')
 # if not fruit_choice:
  #  streamlit.error("Please select a fruit for information")
 # else:
  #  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/")
  #  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  #streamlit.dataframe(fruityvice_normalized)
   
#except URLError as e:
 # streamlit.error();

  
  
  
  
  ######
#take the json version of the response and normalize it
#fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
#streamlit.dataframe(fruityvice_normalized)


#New section to display fruitvice API response
#streamlit.header("Fruityvice Fruit Advice!")

#fruit_choice = streamlit.text_input('What fruit would you like information about?')
#streamlit.write('The user entered ', fruit_choice)

#import requests
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)





my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()


my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
my_data_rows = my_cur.fetchall()

streamlit.header("The fruit load list contain:")
streamlit.dataframe(my_data_rows)

  


add_my_fruit=streamlit.text_input('What fruit would you like to add?')

streamlit.write('Thanks for adding',add_my_fruit)
my_cure.execute("insert into fruit_lode_list values ('from streamlit')")
  
  
  #my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  
  

 
 # if streamlit.button('Add a fruit to list'):
 # my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  #back_from_function=insert_row_snowflake(add_my_fruit)
  #streamlit.text(back_from_function)

  
   
