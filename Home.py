import streamlit as st
from sys import path
from chatgpt import ChatGPT


path.append("./CropYieldModel.py")
path.append("./utils.py")


from CropYieldModel import CropYieldModel
from utils import predict_yield 

# define the features of the model
xmodel = CropYieldModel()

"# Maize Yield predictor for Zimbabwe! "

chatbot = ChatGPT()
def chatbot_widget():
    st.subheader('Chat with the Bot')
    user_input = st.text_input('Enter your message:')
    if st.button('Send'):
        if user_input!= '':
            response = chatbot.get_response(user_input)
            st.write(response)


# AN image of crops
image_file = "mynew.jpg"
def add_image(image_file):
  st.image(image_file, caption="Maximise crop Yield with AI")

#where the image was
if __name__ == "__main__":
  add_image(image_file)

# ui to allow user input
"# Rainfall in mm"
xmodel.rainfall = st.number_input(
    label="Rainfall",
    step=10
)

"# Pesticides in Tonnes"
xmodel.pesticides = st.number_input(
    label="Tonnes",
    step=10
)


"# Average Temperature"
xmodel.temp = st.number_input(
    label="Degrees Celcius",
    step=5
)

# function to generate results
def onClick():
    prediction = predict_yield(xmodel)
    displayResults(prediction)
# display results

def displayResults(res : float):
    st.warning("Highest Possible Yield : " + str(res))

st.button(
    label="Predict",
    on_click=onClick
)
image_file = "Predicted_values.PNG"
if __name__ == "__main__":
  add_image(image_file)
  chatbot_widget()
"The model uses Data from FAO and The Word Data Bank"
"More improvements will be made to the model in the near future"
"This model was built by : Wilson Katsande & Tinevimbo Tasara"
