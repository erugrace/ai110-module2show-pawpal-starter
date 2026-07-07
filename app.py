import streamlit as st

from pawpal_system import Owner, Pet, Task, Scheduler


# Create owner once
if "owner" not in st.session_state:

    st.session_state.owner = Owner(
        id=1,
        name="Grace",
        email="grace@email.com"
    )


# Create scheduler once
if "scheduler" not in st.session_state:

    st.session_state.scheduler = Scheduler(
        st.session_state.owner
    )


st.title("🐾 PawPal+ Pet Scheduler")


# Add Pet Section

st.header("Add a Pet")


pet_name = st.text_input("Pet Name")

species = st.text_input("Species")

breed = st.text_input("Breed")

age = st.number_input(
    "Age",
    min_value=0
)


if st.button("Add Pet"):

    new_pet = Pet(
        id=len(st.session_state.owner.pets)+1,
        name=pet_name,
        species=species,
        breed=breed,
        age=age
    )


    st.session_state.owner.add_pet(new_pet)


    st.success(
        f"{pet_name} added successfully!"
    )


# Display Pets

st.header("My Pets")


for pet in st.session_state.owner.pets:

    st.write(
        f"""
        🐾 {pet.name}
        
        Species: {pet.species}
        
        Breed: {pet.breed}
        
        Age: {pet.age}
        """
    )