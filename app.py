import gradio as gr
from getData import get_list

def get_drugs_list(drug: str) -> dict:
    data = get_list(drug)
    return data

theme = gr.themes.Soft(
    primary_hue="purple",
    secondary_hue="cyan",
    neutral_hue="slate",
    font=[gr.themes.GoogleFont('Syne'), gr.themes.GoogleFont('poppins'), gr.themes.GoogleFont('poppins'), gr.themes.GoogleFont('poppins')],
)

with gr.Blocks(theme=theme) as app:
    gr.HTML("<h1 style='text-align: center;'>Indian MedGuide API</h1><spacer style='height: 10%;'>")
    gr.HTML("<h1 style='text-align: center;'>Built using 1mg.com API with <a style='color: red; text-decoration-line: none;'>&#10084;</a> by <a href='http://nayankasturi.eu.org' target='_blank' rel='noopener noreferrer'>Nayan Kasturi</a></h1><spacer style='height: 10%;'> ")
    gr.HTML("<spacer style='height: 25%;'> ")
    with gr.Row():
        drug = gr.Textbox(label="Enter the drug name")
        search = gr.Button(value="Search the drug here")
    data = gr.TextArea(label="Search Results", max_lines=10, lines=10, interactive=False, value="Search results will be displayed here.")
    search.click(fn=get_drugs_list, inputs=drug, outputs=data, concurrency_limit=120)
   
app.queue(default_concurrency_limit=120).launch(show_api=True)