import fastai
from fastai.vision.all import *
import gradio as gr

def label_func(fname):
    if int(str(fname)[str(fname).index('_')+1]) == 0:
        return "Male"
    return "Female"

def get_age(fpath):
    return int(str(fpath).split('/')[5].split('_')[0])


# learn2 = load_learner('age.pkl')


learn = load_learner('gender.pkl')

categories = ('Female', 'Male')

def classify_image(img):
    pred, idx, probs = learn.predict(img)
    # age=learn2.predict(img)
    return dict(zip(categories, map(float, probs))),age[0]

image = gr.inputs.Image(shape=(192,192))

label = gr.outputs.Label()
examples = ['Male.jpg', 'Female.jpg']
iface = gr.Interface(fn=classify_image, inputs=image, outputs=["label","text"], examples=examples)
# with gr.Blocks(css=".gradio-container {background-color:red}") as iface:
iface.launch()

