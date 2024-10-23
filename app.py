import streamlit as st
from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.functions import col

# App title
st.title("🍕 Custom Pizza Builder 🍕")
st.write("Build your perfect pizza by choosing toppings, size, and crust!")

# Snowflake session
session = get_active_session()

# Fetch available pizza options (toppings, crusts, sizes)
toppings_df = session.table("pizza_orders.public.pizza_options").filter(col("INGREDIENT_TYPE") == 'Topping').select(col('INGREDIENT_NAME')).to_pandas()
crusts_df = session.table("pizza_orders.public.pizza_options").filter(col("INGREDIENT_TYPE") == 'Crust').select(col('INGREDIENT_NAME')).to_pandas()
sizes_df = session.table("pizza_orders.public.pizza_options").filter(col("INGREDIENT_TYPE") == 'Size').select(col('INGREDIENT_NAME')).to_pandas()

# User inputs
name = st.text_input("Enter your name for the order")
chosen_toppings = st.multiselect('Choose your toppings:', toppings_df['INGREDIENT_NAME'], max_selections=5)
chosen_crust = st.radio('Choose your crust:', crusts_df['INGREDIENT_NAME'])
chosen_size = st.radio('Choose your pizza size:', sizes_df['INGREDIENT_NAME'])

# Order submission
if st.button('Submit Pizza Order'):
    if not name:
        st.error("Please enter your name before submitting!")
    else:
        toppings_string = ', '.join(chosen_toppings)
        
        # Create SQL statement to insert order
        insert_order_query = f"""
        INSERT INTO pizza_orders.public.pizza_orders (CUSTOMER_NAME, INGREDIENTS, SIZE, CRUST)
        VALUES ('{name}', '{toppings_string}', '{chosen_size}', '{chosen_crust}')
        """
        session.sql(insert_order_query).collect()  # Submit the order to Snowflake
        
        st.success(f"Thanks, {name}! Your pizza is on the way 🍕")

# View pending orders
if st.checkbox('Show Pending Orders'):
    pending_orders = session.table('pizza_orders.public.pizza_orders').filter(col('ORDER_FILLED') == False).select(col('CUSTOMER_NAME'), col('INGREDIENTS')).to_pandas()
    st.dataframe(pending_orders)
