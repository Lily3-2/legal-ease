from flask import Flask, render_template, request
from transformers import PegasusForConditionalGeneration, PegasusTokenizer

app = Flask(__name__)

# Load the pre-trained Pegasus model and tokenizer
model_name = "google/pegasus-billsum"
pegasus_tokenizer = PegasusTokenizer.from_pretrained(model_name)
pegasus_model = PegasusForConditionalGeneration.from_pretrained(model_name)

# Define a function to generate summaries
def generate_summary(text):
    # Tokenize the input text
    inputs = pegasus_tokenizer(text, truncation=True, padding="longest", return_tensors="pt")

    # Generate the summary
    summary_ids = pegasus_model.generate(inputs["input_ids"])

    # Decode the generated summary
    summary = pegasus_tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the text from the uploaded file
        uploaded_text = request.files['file'].read().decode('utf-8')

        # Generate the summary
        summary = generate_summary(uploaded_text)

        return render_template('index.html', summary=summary)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)