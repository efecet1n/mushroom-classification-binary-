import pandas as pd
import pickle
import streamlit as st
from PIL import Image
import base64

with open("mushroom_model.pkl", "rb") as file:
    loaded_model = pickle.load(file)

def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

edible_image_base64 = get_base64_image("mushroom_edible.webp")
poison_image_base64 = get_base64_image("mushroom_poison.png")

st.title("Mushroom Edibility Prediction 🍄")
st.write("Enter mushroom features to predict if it's edible or poisonous.")

with st.expander("🍄 Examples"):
    col1, col2 = st.columns(2)

    with col1:
        st.image("poison.jpg", caption="Example: Poisonous Mushroom", use_container_width=True)
        st.markdown(
            """
            **Attributes:**
            - Cap Shape: Bell  
            - Cap Surface: Smooth  
            - Cap Color: Red  
            - Bruises: No  
            - Odor: Foul  
            - Gill Attachment: Free  
            - Gill Spacing: Crowded  
            - Gill Size: Narrow  
            - Gill Color: White  
            - Stalk Shape: Enlarging  
            - Stalk Root: Bulbous  
            - Stalk Surface Above Ring: Smooth  
            - Stalk Surface Below Ring: Smooth  
            - Stalk Color Above Ring: White  
            - Stalk Color Below Ring: White  
            - Veil Type: Partial  
            - Veil Color: White  
            - Ring Number: One  
            - Ring Type: Pendant  
            - Spore Print Color: White  
            - Population: Scattered  
            - Habitat: Woods  
            """
        )

    with col2:
        st.image("edible.jpg", caption="Example: Edible Mushroom", use_container_width=False, width=300)
        st.markdown(
            """
            **Attributes:**
            - Cap Shape: Convex  
            - Cap Surface: Smooth  
            - Cap Color: Brown  
            - Bruises: Yes  
            - Odor: None  
            - Gill Attachment: Free  
            - Gill Spacing: Close  
            - Gill Size: Broad  
            - Gill Color: Brown  
            - Stalk Shape: Tapering  
            - Stalk Root: Equal  
            - Stalk Surface Above Ring: Smooth  
            - Stalk Surface Below Ring: Smooth  
            - Stalk Color Above Ring: Brown  
            - Stalk Color Below Ring: Brown  
            - Veil Type: Partial  
            - Veil Color: White  
            - Ring Number: One  
            - Ring Type: Flaring  
            - Spore Print Color: Brown  
            - Population: Numerous  
            - Habitat: Meadows  
            """
        )

with st.form("mushroom_form"):
    st.write("**Enter Mushroom Attributes**")
    col1, col2, col3 = st.columns(3)

    cap_shape = col1.selectbox("Cap Shape", ["Bell", "Conical", "Convex", "Flat", "Knobbed", "Sunken"])
    cap_surface = col2.selectbox("Cap Surface", ["Fibrous", "Grooves", "Scaly", "Smooth"])
    cap_color = col3.selectbox("Cap Color",
                               ["Brown", "Buff", "Cinnamon", "Gray", "Green", "Pink", "Purple", "Red", "White",
                                "Yellow"])
    bruises = col1.selectbox("Bruises", ["Bruises", "No"])
    odor = col2.selectbox("Odor", ["Almond", "Anise", "Creosote", "Fishy", "Foul", "Musty", "None", "Pungent", "Spicy"])

    gill_attachment = col3.selectbox("Gill Attachment", ["Attached", "Descending", "Free", "Notched"])
    gill_spacing = col1.selectbox("Gill Spacing", ["Close", "Crowded", "Distant"])
    gill_size = col2.selectbox("Gill Size", ["Broad", "Narrow"])
    gill_color = col3.selectbox("Gill Color",
                                ["Black", "Brown", "Buff", "Chocolate", "Gray", "Green", "Orange", "Pink", "Purple",
                                 "Red", "White", "Yellow"])
    stalk_shape = col1.selectbox("Stalk Shape", ["Enlarging", "Tapering"])
    stalk_root = col2.selectbox("Stalk Root", ["Bulbous", "Club", "Cup", "Equal", "Rhizomorphs", "Rooted", "Missing"])
    stalk_surface_above_ring = col3.selectbox("Stalk Surface Above Ring", ["Fibrous", "Scaly", "Silky", "Smooth"])
    stalk_surface_below_ring = col1.selectbox("Stalk Surface Below Ring", ["Fibrous", "Scaly", "Silky", "Smooth"])
    stalk_color_above_ring = col2.selectbox("Stalk Color Above Ring",
                                            ["Brown", "Buff", "Cinnamon", "Gray", "Orange", "Pink", "Red", "White",
                                             "Yellow"])
    stalk_color_below_ring = col3.selectbox("Stalk Color Below Ring",
                                            ["Brown", "Buff", "Cinnamon", "Gray", "Orange", "Pink", "Red", "White",
                                             "Yellow"])
    veil_type = col1.selectbox("Veil Type", ["Partial", "Universal"])
    veil_color = col2.selectbox("Veil Color", ["Brown", "Orange", "White", "Yellow"])
    ring_number = col3.selectbox("Ring Number", ["None", "One", "Two"])
    ring_type = col1.selectbox("Ring Type",
                               ["Cobwebby", "Evanescent", "Flaring", "Large", "None", "Pendant", "Sheathing", "Zone"])
    spore_print_color = col2.selectbox("Spore Print Color",
                                       ["Black", "Brown", "Buff", "Chocolate", "Green", "Orange", "Purple", "White",
                                        "Yellow"])
    population = col3.selectbox("Population", ["Abundant", "Clustered", "Numerous", "Scattered", "Several", "Solitary"])
    habitat = col1.selectbox("Habitat", ["Grasses", "Leaves", "Meadows", "Paths", "Urban", "Waste", "Woods"])
    predict_button = st.form_submit_button("🔍 Predict")

if predict_button:
    inputs = {
        "CapShape": cap_shape,
        "CapSurface": cap_surface,
        "CapColor": cap_color,
        "Bruises": bruises,
        "Odor": odor,
        "GillAttachment": gill_attachment,
        "GillSpacing": gill_spacing,
        "GillSize": gill_size,
        "GillColor": gill_color,
        "StalkShape": stalk_shape,
        "StalkRoot": stalk_root,
        "StalkSurfaceAboveRing": stalk_surface_above_ring,
        "StalkSurfaceBelowRing": stalk_surface_below_ring,
        "StalkColorAboveRing": stalk_color_above_ring,
        "StalkColorBelowRing": stalk_color_below_ring,
        "VeilType": veil_type,
        "VeilColor": veil_color,
        "RingNumber": ring_number,
        "RingType": ring_type,
        "SporePrintColor": spore_print_color,
        "Population": population,
        "Habitat": habitat,
    }
    input_df = pd.DataFrame([inputs])
    input_df = pd.get_dummies(input_df)
    input_df = input_df.reindex(columns=loaded_model.feature_names_in_, fill_value=0)

    prediction = loaded_model.predict(input_df)[0]
    result = "Edible" if prediction == 0 else "Poisonous"
    color = "green" if prediction == 0 else "red"
    emoji_image = edible_image_base64 if prediction == 0 else poison_image_base64

    st.markdown(
        f"""
        <h3 style='text-align: center; color: {color};'>
            The mushroom is: {result} 
            <img src='data:image/png;base64,{emoji_image}' style='width:40px; height:40px; vertical-align:middle;'>
        </h3>
        """,
        unsafe_allow_html=True,
    )
