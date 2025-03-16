import streamlit as st



import pickle
pickled = open('model/IrisClassifier.pkl', 'rb')
iris_model = pickle.load(pickled)



layout = 'centered'
page_title = 'Iris App'
page_icon = ':rose:'

st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)

st.title(page_icon+' '+ page_title)


html_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>
"""
st.markdown(html_style, unsafe_allow_html=True)

with st.sidebar:
    st.markdown("## Iris Classification App")

with st.container():
    with st.form(key='my_form'):
        st.text("Enter Details Below")
        sep_len = st.text_input(label='Sepal Length')

        sep_wid = st.text_input(label='Sepal Width')

        pet_len = st.text_input(label='Petal Length')

        pet_wid = st.text_input(label='Petal Width')

        submitted = st.form_submit_button(label='Predict')
        
    if submitted:
        data = [[int(sep_len), int(sep_wid), int(pet_len), int(pet_wid)]]

        st.text(data)

        PredictedFlowers = iris_model.predict(data)
        st.text(PredictedFlowers[0])
        if PredictedFlowers == 'Setosa':
            st.image("setosa.jpg")
        
        elif PredictedFlowers == 'Versicolor':
            st.image("versicolor.jpg")
        
        else:
            st.image("virginica.jpg")

        
