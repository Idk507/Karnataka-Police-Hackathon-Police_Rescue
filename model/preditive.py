import streamlit as st

def display_predicted_crimes(year):
    if year == 2025:
        st.markdown('<iframe src="https://661a6f7a824e4d86fd1f8607--musical-kheer-bc563e.netlify.app/" width="700" height="500"></iframe>', unsafe_allow_html=True)
    elif year == 2026:
        st.markdown('<iframe src="https://661a70638576dc86b614a8b0--delightful-chebakia-aafaa1.netlify.app/" width="700" height="500"></iframe>', unsafe_allow_html=True)
    else:
        st.write("Year not supported.")

def main():
    st.title("Prediction for top 5 cases")
    st.write("Select a year and click 'Predict' to see the predicted crimes for that year.")

    year = st.selectbox("Select Year", [2025, 2026])

    if st.button("Predict"):
        display_predicted_crimes(year)

if __name__ == "__main__":
    main()
