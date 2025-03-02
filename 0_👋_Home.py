import streamlit as st
import base64

    
# ----- Page configs (tab title, favicon) -----
st.set_page_config(
    page_title="Fabrizio Troche Portfolio",
    page_icon="📊",
)


# ----- Left menu -----
with st.sidebar:
    st.image("eae_img.png", width=200)
    st.header("Introduction to Programming Languages for Data")
    st.write("###")
    st.write("***Final Project - Dec 2023***")
    st.write("**Author:** <Your Name>")
    st.write("**Instructor:** [Enric Domingo](https://github.com/enricd)")


# ----- Top title -----
st.write(f"""<div style="text-align: center;"><h1 style="text-align: center;">👋 Hi! My name is Fabrizio Troche 🐐</h1></div>""", unsafe_allow_html=True)  # TODO: Add your name


# ----- Profile image file -----
profile_image_file_path = r"C:\Users\troch\OneDrive\Escritorio\EAE\Intro to programming\eae_ipld_project\data\profile.png"       # TODO: Upload your profile image to the same folder as this script and update this if it has a different name

with open(profile_image_file_path, "rb") as img_file:
    img = "data:image/png;base64," + base64.b64encode(img_file.read()).decode()


# ----- Your Profile Image -----
st.write(f"""
<div style="display: flex; justify-content: center;">
    <img src="{img}" alt="Your Name" width="300" height="300" style="border-radius: 50%; object-fit: cover; margin-top: 40px; margin-bottom: 40px;">
</div>
""", unsafe_allow_html=True)


# ----- Personal title or short description -----
current_role = "Master’s Student in Big Data & Analytics | Data Analyst & Industrial Engineer"  # TODO: Change this

st.write(f"""<div style="text-align: center;"><h4><i>{current_role}</i></h4></div>""", unsafe_allow_html=True)

st.write("##")    # Adding some space


# ----- About me section -----
st.subheader("About Me")

# TODO: Modify and adapt the following lines to your info, you can add or remove some details if you want
st.write("""
- 👨‍💻 I am a **Data Analyst & Industrial Engineer**, passionate about transforming data into impactful decisions. Currently pursuing a **Master’s in Big Data & Analytics** at **EAE Business School, Barcelona**.
  
- ✂️ prev: **Strategic Planning Analyst at Lexus (2021-2024, Paraguay)**  
  Led the strategic planning for Lexus, helping the brand climb from **6th to 4th** place in the **premium automotive market share**.  
  Managed **KPI dashboards** and developed **data-driven reports** to support optimization strategies.

- ❤️ My passions: **Data Analysis, Business Intelligence, and Process Optimization**.  
  I enjoy working with **SQL, Python, Power BI**, and **Excel** to create meaningful insights.

- 📺 Personal Projects: **Building dashboards & automating reports** using **Power BI & Python**.

- ✈️ Hobbies: **Traveling, playing FIFA, and working on analytics projects**.

- 📩 How to reach me: **trochejm@gmail.com** | **[LinkedIn](https://www.linkedin.com/in/fabriziotroche)**

- 📍 Barcelona

- 🖥️ Check my projects: **[GitHub](https://github.com/fabriziotroche)**
         


""")

# Feel free to add other points like your Linkedin, Github, Social Media, etc.
