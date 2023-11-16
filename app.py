from flask import Flask, render_template, send_file, request, make_response
import pdfkit
from datetime import datetime
import time

from core import extract_article, generate_summary_prompt, generate_image, translate_title
from generate_pdf import generate_pdf_for_list


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url_list = [request.form[i] for i in request.form]
        pdf_input_list = []
        for i, url in enumerate(url_list):
            print(f'Started processing {i+1} article')
            start_time = time.time()
            article_title, article_text = extract_article(url)
            translated_title = translate_title(article_title)
            summary, prompt = generate_summary_prompt(article_text)
            # image = 1
            image = generate_image(prompt)
            pdf_input_list.append((translated_title, summary, image, url))
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f'Finished processing {i+1} article elapsed time: {elapsed_time}')
        print(pdf_input_list)

        # Generate PDF
        output_path = generate_pdf_for_list(pdf_input_list)
        current_datetime = datetime.now()
        date_string = current_datetime.strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"newsletter_gpt_{date_string}.pdf"

        #Create response
        return send_file(output_path, as_attachment=True, download_name=filename)
        # response = make_response(pdf_content)
        # response.headers['Content-Type'] = 'application/pdf'
        # response.headers['Content-Disposition'] = 'attachment; filename=generated_document.pdf'

        # return response

    return render_template('index.html')

def generate_pdf(urls):
    pass

if __name__ == '__main__':
    app.run(debug=True)
