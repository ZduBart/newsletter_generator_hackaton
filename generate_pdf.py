from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, Image as ImagePlatypus, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from PIL import Image
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
 

def generate_pdf_for_list(data_list, output_path='C:/Users/Public/newsletter.pdf'):
    # Tworzenie nowego pliku PDF
    pdf_doc = SimpleDocTemplate(output_path, pagesize=letter)
    styles = getSampleStyleSheet()
 
    # Tworzenie listy elementów do umieszczenia w dokumencie
    elements = []
 
    # Iteracja przez listę tekstów i obrazków
    for title, text, image_path, articleUrl in data_list:
        pdfmetrics.registerFont(TTFont('Arial', 'arial.ttf'))
 
        title_style = ParagraphStyle(
        'LinkStyle',
        parent=styles['Normal'],
        spaceAfter=10,  # Dodatkowy odstęp po paragrafie
        backColor=colors.transparent,  # Przezroczyste tło
        borderPadding=(0, 0, 0, 0),  # Brak odstępu od krawędzi
        underline=True,
        fontSize=12,
        fontName='Arial',  # Możesz dostosować rodzaj czcionki
        alignment=0  # Wyrównanie do lewej
    )
        txt_style = ParagraphStyle(
        'TxtStyle',
        fontName='Arial',  # Możesz dostosować rodzaj czcionki
    )
        text_with_link = '<b><u><a href="%s">%s</a></u></b>' % (articleUrl, title)
        title_paragraph = Paragraph(text_with_link, title_style)
        txt_paragraph = Paragraph(text, txt_style)
        paragraphs = [
        title_paragraph,
        txt_paragraph
        ]
        # Tworzenie tabeli z dwiema kolumnami (lewa - obrazek, prawa - tekst)
        data = [[ImagePlatypus(image_path, width=180, height=180), paragraphs]]
        table = Table(data, colWidths=[200, 300], rowHeights=[200])
 
        # Usunięcie obramowania
        table.setStyle([('GRID', (0, 0), (-1, -1), 0, colors.white)])
        table.setStyle([('VALIGN', (0, 0), (-1, -1), 'TOP')])
 
        # Dodawanie tabeli do listy elementów
        elements.append(table)
        elements.append(Spacer(1, 10))
 
    # Dodawanie elementów do dokumentu
    pdf_doc.build(elements)
    return output_path
if __name__ == "__main__":
    input_data_list = [('Klarna planuje debiut na giełdzie. Może nastąpić już za kilka kwartałów.', 'Szwedzka firma Klarna utworzyła spółkę holdingową w Wielkiej Brytanii, co może wskazywać na jej przygotowania do debiutu giełdowego. Zarówno termin jak i miejsce debiutu remain nieznane. Przejściowe problemy z związkami zawodowymi zostały zażegnane. Firma osiągnęła porozumienie z związkowcami, co jest istotne w kontekście przygotowań do IPO. Działalność Klarny na nowym rynku zależeć będzie od działań brytyjskiego regulatora rynku BNPL.', 'https://dalleprodsec.blob.core.windows.net/private/images/402c2984-1a07-42f0-b7a9-666aa9b08c78/generated_00.png?se=2023-11-17T14%3A22%3A06Z&sig=vc855b2GDXg9YogsCzyWQzHNAUo52rGWkxUMPR5JAoQ%3D&ske=2023-11-22T10%3A18%3A29Z&skoid=e52d5ed7-0657-4f62-bc12-7e5dbb260a96&sks=b&skt=2023-11-15T10%3A18%3A29Z&sktid=33e01921-4d64-4f8c-a055-5bdaffd5e33d&skv=2020-10-02&sp=r&spr=https&sr=b&sv=2020-10-02', 'https://www.cashless.pl/14473-klarna-debiut-gieldowy-spolka-holdingowa'), ('Allegro Platform Operator udostępnia aplikację mobilną dla Apple Watch', 'Allegro udostępniło nową aplikację mobilną na Apple Watch, która ułatwia odbieranie przesyłek z automatów paczkowych. Aplikacja informuje o statusie wszystkich przesyłek zamówionych na allegro.pl i umożliwia odbiór przesyłek przez zeskanowanie kodów QR na zegarku. Aplikacja jest dostępna w języku polskim, angielskim, czeskim, ukraińskim i słowackim.', 'https://dalleprodsec.blob.core.windows.net/private/images/15d6070c-e977-46f4-b73c-89208d8ac5de/generated_00.png?se=2023-11-17T14%3A23%3A00Z&sig=0xSt2yWIPm85bxoChj5PU5FDQFQ%2FYuXGS4WP%2F%2FYJciw%3D&ske=2023-11-22T10%3A11%3A24Z&skoid=e52d5ed7-0657-4f62-bc12-7e5dbb260a96&sks=b&skt=2023-11-15T10%3A11%3A24Z&sktid=33e01921-4d64-4f8c-a055-5bdaffd5e33d&skv=2020-10-02&sp=r&spr=https&sr=b&sv=2020-10-02', 'https://www.cashless.pl/14483-allegro-aplikacja-applewatch')]
 
    generate_pdf_for_list(input_data_list)