import streamlit as st
from langchain.llms import OpenAI  # Import LangChain's LLM module


# Sidebar for taking user api key
st.sidebar.header("API Key")
api_key = st.sidebar.text_input("Enter your API key", type="password")


# Adding a if statement so the UI will not be rendered unless api key is entered
if api_key:
    # Initialize LangChain's LLM module
    llm = OpenAI(
        openai_api_key=api_key,
        max_tokens=1000,
    )

    # Set the title of your app
    st.title("🍳🤖 AI Recipe Generator")

    # Create columns for square buttons
    col1, col2, col3, col4 = st.columns(4)

    # Define meal type options
    meal_type_options = ["Appetizer", "Main Course", "Dessert", "Custom"]

    # Create square buttons for meal type selection
    meal_type = col1.selectbox("Select Meal Type", meal_type_options, index=0)

    # Input field for ingredients
    ingredients = st.text_input("Enter Ingredients (comma-separated)")

    # Create checkboxes for dietary preferences
    dietary_preferences = col2.selectbox(
        "Select Dietary Preferences", ["Normal", "Vegetarian", "Vegan", "Gluten-Free", "Low Carb"]
    )

    # Input field for preparation time
    preparation_time = st.slider(
        "Preparation Time (minutes)", min_value=0, max_value=240, value=60
    )

    user_instructions = st.text_area("Add Your Custom Message (Optional)")

    # Inside the Streamlit app logic
    if st.button("Generate Recipe"):
        # Validate that ingredients are not empty
        if not ingredients:
            st.warning("Please enter ingredients.")
        else:
            # Split the comma-separated ingredients and remove leading/trailing spaces
            ingredients_list = [
                ingredient.strip() for ingredient in ingredients.split(",")
            ]

            # Construct a prompt for recipe generation based on user inputs
            prompt = f"Create a {meal_type} recipe using {', '.join(ingredients_list)}"
            if dietary_preferences:
                prompt += f" that is {' and '.join(dietary_preferences)}"

            prompt += f" with a preparation time of {preparation_time} minutes."
            if user_instructions:
                prompt += f"follow these custom instructions: {user_instructions}"

            #Adding Warning
            st.warning("AI-generated recipes may not be safe or accurate. Please use caution when following these recipes.")
            
            # Call the LangChain LLM to generate the recipe
            generated_recipe = llm.predict(prompt)
            print(generated_recipe)

            # Display the generated recipe
            st.subheader("Generated Recipe")
            st.write(generated_recipe)
# Else statement to show warning message unless user enter his or her API Key
else:
    st.warning("Please enter your API Key")
