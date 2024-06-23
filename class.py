import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from twilio.rest import Client

# Twilio setup
account_sid = "AC894538ff53709392887cf2e9bbef69df"
auth_token = ""
client = Client(account_sid, auth_token)
phone_numbers = [
    "+919442621187", "+919000228323", "+919442621187",
    "+919000228323", "+919000228323", "+919442621187",
    "+919442621187", "+919000228323", "+919000228323"
]

# Data preparation
header = [
    "Farmer's Name", "Pincode", "Aadhar Number", "Contact Number", "Area Ploughed (acres)", "Season",
    "Crop grown", "Seeds Used (Own, Given by IFTR, Purchased from Outside)", "Variety Used", "Quantity Used",
    "Date of Seed sown", "Transplanting (Manual)", "Transplanting (Machine)", "Irrigation Method (Borewell)",
    "Irrigation Method (Well)", "Irrigation Method (River)", "Irrigation Method (Drip Irrigation)",
    "Fertilizers Use (Organic)", "Fertilizers Use (Chemical)", "Fertilizers Use (Bioinputs)",
    "Date of Harvesting", "Yield (kg)", "Financial Aid"
]

data = [
    ["John Doe", 123456, "1234-5678-9012", "9876543210", 5, "Rabi", "Rice", "Own", "IR64", "10kg", "2024-01-15", "No", "No", "No", "No", "No", "Yes", "Yes", "No", "No", "2024-05-20", 5000, "Yes"],
    ["Jane Smith", 654321, "2345-6789-0123", "8765432109", 10, "Rabi", "Rice", "Given by IFTR", "HD2967", "15kg", "2024-02-20", "No", "Yes", "No", "No", "No", "No", "No", "Yes", "No", "2024-06-25", 8000, "Yes"],
    ["Sam Brown", 234567, "3456-7890-1234", "7654321098", 8, "Zaid", "Rice", "Purchased from Outside", "HQPM-1", "12kg", "2024-03-10", "No", "No", "Yes", "No", "Yes", "No", "Yes", "No", "Yes", "2024-07-30", 7000, "Yes"],
    ["Lucy Green", 543210, "4567-8901-2345", "6543210987", 6, "Kharif", "Rice", "Own", "JS335", "8kg", "2024-04-15", "No", "Yes", "No", "Yes", "Yes", "Yes", "Yes", "No", "No", "2024-09-10", 6000, "Yes"],
    ["Mark White", 345678, "5678-9012-3456", "5432109876", 7, "Rabi", "Barley", "Given by IFTR", "PL751", "9kg", "2024-05-25", "No", "No", "Yes", "Yes", "No", "Yes", "Yes", "No", "Yes", "2024-10-15", 5500, "Yes"],
    ["Nina Black", 456789, "6789-0123-4567", "4321098765", 4, "Zaid", "Tomato", "Purchased from Outside", "Bt Cotton", "20kg", "2024-06-05", "No", "Yes", "Yes", "Yes", "Yes", "No", "Yes", "No", "No", "2024-11-20", 7200, "Yes"],
    ["Oscar Blue", 567890, "7890-1234-5678", "3210987654", 12, "Rabi", "Sugarcane", "Own", "Co86032", "30kg", "2024-07-12", "Yes", "No", "Yes", "No", "No", "Yes", "Yes", "No", "Yes", "2024-12-25", 9000, "No"],
    ["Paula Red", 678901, "8901-2345-6789", "2109876543", 9, "Rabi", "Tomato", "Given by IFTR", "Arkel", "5kg", "2024-08-20", "No", "Yes", "Yes", "No", "Yes", "No", "Yes", "No", "No", "2025-01-30", 4000, "No"],
    ["Quinn Purple", 789012, "9012-3456-7890", "1098765432", 15, "Zaid", "Tomato", "Purchased from Outside", "Arka Rakshak", "10kg", "2024-09-10", "Yes", "No", "No", "Yes", "Yes", "No", "Yes", "No", "Yes", "2025-03-20", 8500, "No"],
    ["Rita Yellow", 890123, "0123-4567-8901", "0987654321", 3, "Kharif", "Paddy", "Own", "BPT5204", "25kg", "2024-10-15", "No", "Yes", "Yes", "No", "Yes", "No", "Yes", "No", "No", "2025-02-15", 4500, "No"]
]

df = pd.DataFrame(data, columns=header)

# Streamlit App
def main():
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", ["Home", "Login", "Dashboard", "Notifications","Farmers Registration Form","Upload Image"])

    if selection == "Home":
        st.title("Indigenous and Frontier Technology Research Centre (IFTR) ")
        st.write("Indigenous and Frontier Technology Research Centre (IFTR) was established in 2002 as a not-for-profit organization to help women in rural areas to stand on their own legs by using an evolving technology – eco-friendly paper production using agricultural wastes.")
        st.write("IFTR aims to accelerate the use of modern science and technology for the development of interventions to improve the livelihoods of people and society at large. IFTR will act as a vehicle for taking new technologies/skills to the masses. For this, IFTR will acquire, adopt, adapt, retrofit appropriate science and technology products/processes to provide solutions to practical problems faced by people. Wherever possible, IFTR will also strive to develop suitable technologies/interventions.")
    elif selection == "Login":
        st.title("Login")
        st.write("Please login to access the dashboard.")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            if username == "admin" and password == "password":
                st.success("Logged in as admin")
                st.session_state.logged_in = True
            else:
                st.error("Invalid credentials")
    
    elif selection == "Dashboard":
        if "logged_in" not in st.session_state or not st.session_state.logged_in:
            st.error("Please login first.")
        else:
            st.title("Dashboard")
            st.write("Data visualizations and analysis")

            # Visualization 1: Number of Farmers in Each Location
            location_counts = df['Pincode'].value_counts()
            plt.figure(figsize=(10, 6))
            plt.pie(location_counts, labels=location_counts.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette('Set3', len(location_counts)))
            plt.title('Number of Farmers in Each Location')
            st.pyplot(plt)

            # Visualization 2: Types of Crops in Different Locations
            location_crop_counts = df.groupby(['Pincode', 'Crop grown']).size().unstack(fill_value=0)
            location_crop_counts.plot(kind='bar', stacked=True, figsize=(12, 8), colormap='tab20')
            plt.title('Types of Crops in Different Locations')
            plt.xlabel('Pincode')
            plt.ylabel('Number of Farmers')
            plt.legend(title='Crop Grown', bbox_to_anchor=(1.05, 1), loc='upper left')
            plt.xticks(rotation=45)
            st.pyplot(plt)
            st.title('Types of Crops in Different Locations')

            # Visualization 3: Variety of Crops Grown
            crop_varieties = df['Crop grown'].value_counts()
            plt.figure(figsize=(10, 8))
            plt.pie(crop_varieties, labels=crop_varieties.index, autopct='%1.1f%%', colors=plt.cm.tab20.colors)
            plt.title('Variety of Crops Grown')
            st.pyplot(plt)

            # Visualization 4: Fertilizers Used
            fertilizers_used = {
                "Organic": df['Fertilizers Use (Organic)'].value_counts().get('Yes', 0),
                "Chemical": df['Fertilizers Use (Chemical)'].value_counts().get('Yes', 0),
                "Bioinputs": df['Fertilizers Use (Bioinputs)'].value_counts().get('Yes', 0)
            }
            fertilizers_df = pd.DataFrame(list(fertilizers_used.items()), columns=['Fertilizer Type', 'Count'])
            plt.figure(figsize=(10, 6))
            sns.barplot(x='Fertilizer Type', y='Count', data=fertilizers_df, palette='viridis')
            plt.title('Types of Fertilizers Used')
            plt.xlabel('Fertilizer Type')
            plt.ylabel('Count')
            st.pyplot(plt)

            # Visualization 5: Transplanting Methods
            manual_transplanting_percentage = (df['Transplanting (Manual)'].value_counts().get('Yes', 0) / len(df)) * 100
            machine_transplanting_percentage = (df['Transplanting (Machine)'].value_counts().get('Yes', 0) / len(df)) * 100
            transplanting_methods = {
                'Manual': manual_transplanting_percentage,
                'Machine': machine_transplanting_percentage
            }
            transplanting_df = pd.DataFrame(list(transplanting_methods.items()), columns=['Transplanting Method', 'Percentage'])
            plt.figure(figsize=(10, 6))
            sns.barplot(x='Transplanting Method', y='Percentage', data=transplanting_df, palette='pastel')
            plt.title('Transplanting Methods')
            plt.xlabel('Transplanting Method')
            plt.ylabel('Percentage')
            st.pyplot(plt)

    elif selection == "Notifications":
        if "logged_in" not in st.session_state or not st.session_state.logged_in:
            st.error("Please login first.")
        else:
            st.title("Send Notifications")
            message_body = st.text_area("Enter the message to send")
            if st.button("Send Message"):
                for number in phone_numbers:
                    message = client.messages.create(
                        body=message_body,
                        from_="+18479061061",
                        to=number,
                    )
                st.success("Message sent successfully!")
    elif selection == "Farmers Registration Form":
        st.title("Farmers Registration")
        st.write("Please fill out the form below to register as a farmer.")
        st.markdown(
            """
            <iframe src="https://docs.google.com/forms/d/e/1FAIpQLSfDw4905Hj93J2uB3Cg_VrDOcOzaQ2MXYbKRB_FO_R7GON3Bg/viewform?pli=1" width="100%" height="800"></iframe>
            """,
            unsafe_allow_html=True
        )
    elif selection == "Upload Image":
        st.title("Please upload image")
        st.markdown(
            """
            <iframe src="" width="100%" height="800"></iframe>
            """,
            unsafe_allow_html=True
        )

if __name__ == "__main__":
    main()
