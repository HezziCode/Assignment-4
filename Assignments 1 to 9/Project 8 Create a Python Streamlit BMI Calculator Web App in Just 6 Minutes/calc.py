import streamlit as st


def main():
    st.set_page_config(page_title="BMI Calculator", page_icon="🏋️")
    st.title(" Body Mass Index Calculator (BMI)")
    weight = st.number_input("Enter your weight (kg)", min_value=0.0, step=0.1)
    height = st.number_input("Enter your height (m)", min_value=0.0, step=0.1)
    if st.button("Calculate BMI"):
        if weight > 0 and height > 0:
            bmi = weight / (height ** 2)
            rounded = round(bmi, 2)
            st.write(f"Your BMI is: {rounded}")

            if bmi < 18.5:
                st.write("You are underweight.")
            elif 18.5 <= bmi < 24.9:
                st.write("You have a normal weight.")
            elif 25 <= bmi < 29.9:
                st.write("You are overweight.")
            else:
                st.write("You are obese.")
        else:
            st.error("Please enter valid weight and height values.")
if __name__ == "__main__":
    main()