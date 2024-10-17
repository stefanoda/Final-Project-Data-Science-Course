import streamlit as st
import pandas as pd
import os
from camera_models import camera_models
from countries import country_states  # Importing the country and state data from countries.py

# Function to save data to CSV with a unique ID
def save_data_to_csv(data, file_name):
    # Check if file exists
    if os.path.exists(file_name):
        # Read existing data to get the last ID
        existing_data = pd.read_csv(file_name, delimiter=';', encoding='ISO-8859-1')
        last_id = int(existing_data['ID'].max())
    else:
        # If file doesn't exist, start with ID 0
        last_id = 0
    
    # Assign a unique ID to the new data
    data['ID'] = last_id + 1
    
    # Reorder columns as per the specified order
    columns_order = [
        'ID', 'Age', 'Country', 'State', 'Gender', 'Level', 'Starting Year',
        'Main Field of Photography', 'First Camera Brand', 'Previous Camera Brand',
        'Current Camera Brand', 'Sensor Size', 'Current Camera Model',
        'Amount of Lenses', 'Preferred Lens Type', 'Favourite Focal Length',
        'Shooting in Film?', 'Are you happy with your gear?'
    ]
    
    # Reorder data columns
    data = data[columns_order]
    
    # Save to CSV with semicolon delimiter
    if os.path.exists(file_name):
        # Append data without header
        data.to_csv(file_name, mode='a', header=False, index=False, sep=';')
    else:
        # Write data with header
        data.to_csv(file_name, mode='w', header=True, index=False, sep=';')

# Streamlit app configuration
st.set_page_config(layout="wide")

# Initialize session state for button click
if 'submitted' not in st.session_state:
    st.session_state['submitted'] = False

#background-color: #2E86C1; /* Light blue background for contrast */

# Display the thank you message
def display_thank_you_message():
    st.markdown(
        """
        <style>
            /* Center the container vertically and horizontally */
            .thank-you {
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                height: 100vh;
                
                color: #FFFFFF; /* White text color */
            }

            /* Larger font size for the main thank you message */
            .thank-you h1 {
                font-size: 3em; /* Larger size for the main message */
                margin-bottom: 20px; /* Space between the two messages */
                text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2); /* Subtle shadow for depth */
            }

            /* Smaller font size for the discount message */
            .thank-you p {
                font-size: 1.5em; /* Smaller size for the discount message */
                margin-top: 0;
                font-style: italic; /* Italic style for emphasis */
                background-color: #A9A9A9; /* Darker blue background for discount message */
                padding: 10px 20px; /* Padding around the discount message */
                border-radius: 10px; /* Rounded corners for better aesthetics */
                box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.2); /* Shadow for a lifted look */
            }

            /* Hide Streamlit header and footer */
            body > div:first-child {visibility: hidden;}
            footer {visibility: hidden;}
        </style>
        <div class="thank-you">
            <h1>Thank you for taking part in our survey!</h1>
            <p>Use code <strong>"SURVEY5"</strong> to get a 5% discount on your next order.</p>
        </div>
        """,
        unsafe_allow_html=True
    )


# UI Layout only if not submitted
if not st.session_state['submitted']:
    col1, col2, col3, col4 = st.columns([10,15,40,20])

    with col1:
        st.image('logo.png', width=170)

    with col3:
        for _ in range(8):
            st.write(' ')

        st.header('Welcome to the Lumiora Newsletter')
        st.write('   ')
        st.subheader('Tell us about yourself')


        # User Input Fields
        age = st.text_input('How old are you?', placeholder="Enter your age in numbers")

        # Validate input to ensure it's only digits
        if age and not age.isdigit():
            st.warning("Please enter a valid age using only numbers.")
        # Country selectbox
        countries = [
            "Australia", "Austria", "Belgium", "Canada", "Czech Republic", "Denmark", "Finland", 
            "France", "Germany", "Ireland", "Italy", "Japan", "Netherlands", 
            "New Zealand", "Norway", "Poland", "Portugal", "Singapore", "South Korea", "Spain", 
            "Sweden", "Switzerland", "United Kingdom", "United States"
        ]
        country = st.selectbox('Please select your country', [' '] + sorted(countries))
        
        # State selectbox based on country selection
        if country != ' ':
            states = country_states.get(country, [])
            if states:
                state = st.selectbox('Select your state/region', [' '] + states)
            else:
                state = None
        else:
            state = None

        gender = st.radio('Please select your gender', ('Male', 'Female'))
        level = st.radio('How would you rate yourself?', ('Hobbyist', 'Enthusiast', 'Professional'))
        starting_year = st.slider('When did you start with photography?', 1950, 2024, 1987)
        main_field = st.selectbox('What is your main field of photography?', (' ', 'Portrait', 'Landscape', 'Sports', 'Commercial','Documentary', 'Architecture','Event', 'Fashion', 'Astro', 'Street','Travel', 'Macro', 'Wedding', 'Wildlife', 'Other'))

        st.write('   ')
        st.write('   ')

        st.subheader('What are you equipped with?')

        # Camera Brands
        brands = list(camera_models.keys())

        first_brand = st.selectbox('What was your first camera brand?', [' '] + brands)
        previous_brand = st.selectbox('What was your previous camera brand?', [' '] + brands)
        camera_brand = st.selectbox('What is your current camera brand?', [' '] + brands + ['Other'])
        sensor_size = st.selectbox('What sensor-size do you use?', [' ', 'Full-Frame', 'APS-C', 'Micro Four Thirds', 'Medium Format', '1-inch', 'Other'])

        # Show camera models based on selected brand and sensor size, only after sensor size is chosen
        if sensor_size != ' ':
            if camera_brand == 'Other':
                selected_model = 'Other'
                st.write(f'You selected: {selected_model}')
            elif camera_brand in camera_models and sensor_size in camera_models[camera_brand]:
                filtered_models = camera_models[camera_brand].get(sensor_size, [])
                selected_model = st.selectbox('Select your camera model', [' '] + filtered_models)
                
        else:
            selected_model = None

        num_lenses = st.selectbox('How many lenses do you own?', [' ', '1', '2', '3', '4', '5', '>5'])
        lens_type = st.radio('What is your preferred lens type?', ['Zoom', 'Prime'])
        
        
        # Preferred Focal Length input field - Only allow numbers or text with a hyphen
        focal_length = st.text_input('What is your favourite lens? Please enter focal length in digits.', placeholder="e.g 85 or 24-70")

        # Check if input is valid (either all digits or includes a hyphen for custom text)
        if focal_length:
            # Check if the input is only digits or contains a hyphen
            if focal_length.isdigit() or '-' in focal_length:
                focal_length += 'mm'
            else:
                st.warning("Please enter a valid focal length (e.g., 85 or 24-70).")

        shoot_film = st.radio('Do you also shoot film?', ['Yes', 'No'])
        gear_satisfaction = st.radio('Are you happy with your gear?', ['Yes', 'No'])

        # Collecting all data in a dictionary with the specified column names
        data = {
            'ID': None,  # This will be assigned in the save_data_to_csv function
            'Age': age,
            'Country': country,
            'State': state,
            'Gender': gender,
            'Level': level,
            'Starting Year': starting_year,
            'Main Field of Photography': main_field,
            'First Camera Brand': first_brand,
            'Previous Camera Brand': previous_brand,
            'Current Camera Brand': camera_brand,
            'Sensor Size': sensor_size,
            'Current Camera Model': selected_model,
            'Amount of Lenses': num_lenses,
            'Preferred Lens Type': lens_type,
            'Favourite Focal Length': focal_length,
            'Shooting in Film?': shoot_film,
            'Are you happy with your gear?': gear_satisfaction
        }

        # Button to save data
        if not st.session_state['submitted']:
            if st.button("Send"):
                missing_fields = []

                # Check required fields
                if not age or not age.isdigit():
                    missing_fields.append('Age')
                if country == ' ':
                    missing_fields.append('Country')
                if state is not None and state == ' ':
                    missing_fields.append('State')
                if not gender:
                    missing_fields.append('Gender')
                if not level:
                    missing_fields.append('Level')
                if main_field == ' ':
                    missing_fields.append('Main Field of Photography')
                if first_brand == ' ':
                    missing_fields.append('First Camera Brand')
                if previous_brand == ' ':
                    missing_fields.append('Previous Camera Brand')
                if camera_brand == ' ':
                    missing_fields.append('Current Camera Brand')
                if sensor_size == ' ':
                    missing_fields.append('Sensor Size')
                if selected_model is None or selected_model == ' ':
                    missing_fields.append('Current Camera Model')
                if num_lenses == ' ':
                    missing_fields.append('Amount of Lenses')
                if not focal_length or not focal_length[:-2].isdigit():  # Remove 'mm' and check for digits
                    missing_fields.append('Favourite Focal Length')

                # Check for any missing fields
                if missing_fields:
                    st.error(f"Please fill in all the required fields: {', '.join(missing_fields)}")
                else:
                    # Convert data dictionary to DataFrame
                    data_df = pd.DataFrame([data])
                    
                    # Save the data to CSV
                    save_data_to_csv(data_df, 'dataset_newsletter.csv')
                    
                    # Set the session state to True to indicate submission
                    st.session_state['submitted'] = True
                    
                    # Display success message and refresh the page
                    st.experimental_rerun()  # Refresh the page to prevent re-submission

# Redirect to thank you page if submitted
if st.session_state['submitted']:
    display_thank_you_message()
