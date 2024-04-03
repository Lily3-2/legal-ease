from flask import Flask, render_template, request
from transformers import PegasusForConditionalGeneration, PegasusTokenizer
import PyPDF2

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
        # Check if a file is uploaded
        if 'file' not in request.files:
            return render_template('index.html', error='No file uploaded')

        # Get the uploaded file
        uploaded_file = request.files['file']

        # Check if the file is empty
        if uploaded_file.filename == '':
            return render_template('index.html', error='No file selected')

        # Read the content of the file
        file_content = uploaded_file.read()

        # Check if the uploaded file is a PDF
        if uploaded_file.filename.endswith('.pdf'):
            # Extract text from the PDF
            pdf_reader = PyPDF2.PdfReader(io.BytesIO(file_content))
            text = ''
            for page in pdf_reader.pages:
                text += page.extractText()

            # Generate the summary
            summary = generate_summary(text)
        else:
            # Assume it's a text file
            text = file_content.decode('utf-8')

            # Generate the summary
            summary = generate_summary(text)

        return render_template('index.html', summary=summary)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
