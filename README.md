# newsletter_generator_hackaton

## Project Description

This innovative Flask web application was developed during a hackathon organized by Microsoft Polska. The primary functionality of the application is to generate a personalized newsletter in PDF format by processing a list of article URLs. Leveraging cutting-edge technologies, the application extracts article content, translates titles, and generates engaging summaries and opening texts using a GPT model.

One of the standout features of this project is the use of DALL-E-3, a powerful image generation model. The application dynamically creates corresponding images to complement the generated content, enhancing the visual appeal of the newsletter.
## Getting Started

### Prerequisites

Make sure you have Python installed. You can download it from [python.org](https://www.python.org/downloads/).

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/ZduBart/newsletter_generator_hackaton.git
   
2. Navigate to the project directory:
   ```bash
   cd newsletter_generator_hackaton

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Running the Application
### Run the Flask application by executing the following command:

    pip install -r requirements.txt

This will start the development server, and you can access the application by navigating to http://localhost:5000/ in your web browser.

## Project Structure
  - app.py: The main Flask application file.
  - core.py: Module containing functions for article processing.
  - generate_pdf.py: Module for generating PDFs.
  - templates: Folder containing HTML templates for the web application.
## Dependencies
  - Flask
  - pdfkit
  - reportlab
  - newspaper3k
   - openai
  - python-dotenv
  - Pillow
 ## Usage
  Open the application in your web browser.

Enter the URLs of the articles you want to include in the newsletter.

Click the "Generate" button.

The application will process the articles, generate a PDF, and prompt you to download it.

## Project Files
## app.py
The main Flask application file that handles the web interface and PDF generation.

## generate_pdf.py
Module for generating PDFs using the reportlab library.

## core.py
Module containing functions for article processing, including article extraction, summary generation, title translation, image generation, and opening text generation.






