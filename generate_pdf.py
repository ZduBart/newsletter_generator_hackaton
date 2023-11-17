from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, Image as ImagePlatypus, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from PIL import Image
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
 

def generate_pdf_for_list(data_list, opening_text, summary_text, output_path='C:/Users/Public/newsletter.pdf'):
    # Tworzenie nowego pliku PDF
    pdf_doc = SimpleDocTemplate(output_path, pagesize=letter, leftMargin=0, rightMargin=0, topMargin=-6)
    styles = getSampleStyleSheet()
    pdfmetrics.registerFont(TTFont('Arial-Bold', 'arialbd.ttf'))
    pdfmetrics.registerFont(TTFont('Arial', 'arial.ttf'))
    # Tworzenie listy elementów do umieszczenia w dokumencie
    elements = []
    image_width, image_height = letter
    # Open an Image
    elements.append(ImagePlatypus('C:/Users/Public/image002.png', width=image_width, height=130))
    elements.append(Spacer(1, 20))
    #wstep
    opening_text_style = ParagraphStyle(
    'OpeningTxtStyle',
    fontName='Arial',  # Możesz dostosować rodzaj czcionki
    fontSize=15,
    alignment=1,
    spaceAfter=50,
    leading=15,
    leftIndent=50,  # Margines lewy
    rightIndent=50  # Margines prawy
    )
    opening_paragraph = Paragraph(opening_text, opening_text_style)
    elements.append(opening_paragraph)
    # Iteracja przez listę tekstów i obrazków
    for title, text, image_path, articleUrl in data_list:
        title_style = ParagraphStyle(
        'LinkStyle',
        parent=styles['Normal'],
        spaceAfter=10,  # Dodatkowy odstęp po paragrafie
        backColor=colors.transparent,  # Przezroczyste tło
        borderPadding=(0, 0, 0, 0),  # Brak odstępu od krawędzi
        underline=True,
        fontSize=12,
        fontName='Arial-Bold',  # Możesz dostosować rodzaj czcionki
        alignment=0  # Wyrównanie do lewej
    )
        txt_style = ParagraphStyle(
        'TxtStyle',
        fontName='Arial',  # Możesz dostosować rodzaj czcionki
        fontSize=11

    )
       
        text_with_link = '<u><a href="%s">%s</a></u>' % (articleUrl, title)
        title_paragraph = Paragraph(text_with_link, title_style)
        txt_paragraph = Paragraph(text, txt_style)
        paragraphs = [
        Spacer(1, 8),
        title_paragraph,
        txt_paragraph
        ]
        imageData = [Spacer(1, 8), ImagePlatypus(image_path, width=180, height=180)]
        # Tworzenie tabeli z dwiema kolumnami (lewa - obrazek, prawa - tekst)
        data = [[imageData, paragraphs]]
        table = Table(data, colWidths=[200, 300], rowHeights=[200])
 
        # Usunięcie obramowania
        table.setStyle([('GRID', (0, 0), (-1, -1), 0, colors.white)])
        table.setStyle([('VALIGN', (0, 0), (-1, -1), 'TOP')])
 
        # Dodawanie tabeli do listy elementów
        elements.append(table)
        elements.append(Spacer(1, 10))
 
    #zakonczenie
    elements.append(Paragraph(summary_text, opening_text_style))
 
    # Dodawanie elementów do dokumentu
    pdf_doc.build(elements)
 
    return output_path


if __name__ == "__main__":
    input_data_list = [('Grok: dowcipny chatbot Elona Muska oficjalnie! ChatGPT i Bard zagrożone?', 'Grok, pierwszy chatbot stworzony przez Elona Muska dla serwisu X, jest już testowany. Ma on wyróżnić się na tle konkurencji wbudowanym poczuciem humoru i zdolnością zbierania informacji w czasie rzeczywistym. Grok jest jednak dostępny tylko dla użytkowników płatnej wersji serwisu - X Premium+.', 'https://dalleprodsec.blob.core.windows.net/private/images/3d7ed702-553d-4984-9cba-ac1a8c5447ec/generated_00.png?se=2023-11-18T09%3A58%3A46Z&sig=6%2FU30npSOTd%2FgPFE1BaASK9ldCxyRKtRJMCjeP74Jak%3D&ske=2023-11-24T07%3A15%3A32Z&skoid=e52d5ed7-0657-4f62-bc12-7e5dbb260a96&sks=b&skt=2023-11-17T07%3A15%3A32Z&sktid=33e01921-4d64-4f8c-a055-5bdaffd5e33d&skv=2020-10-02&sp=r&spr=https&sr=b&sv=2020-10-02', 'https://dailyweb.pl/grok-dowcipny-chatbot-elona-muska-oficjalnie-chatgpt-i-bard-zagrozone/'), ('Zbliża się koniec epoki przelewów typu pay by link w Polsce. Zobaczcie, jak tracą na rzecz otwartej bankowości', 'Przelewy typu pay by link, kiedyś najpopularniejszy sposób płatności bezgotówkowych w polskich sklepach internetowych, tracą na znaczeniu. Według danych Narodowego Banku Polskiego, liczba tych transakcji spadła z ponad 70 mln w II kwartale 2022 r. do 29,1 mln w II kwartale 2023 r. Rośnie za to popularność płatności opartych na otwartej bankowości.', 'https://dalleprodsec.blob.core.windows.net/private/images/4bc6c451-392b-4a4c-84ca-67b86db448eb/generated_00.png?se=2023-11-18T09%3A59%3A51Z&sig=D6k4fb%2BeB7rplD6iarErZU%2BCVtLa9wPwXNfeGq4jhFQ%3D&ske=2023-11-24T09%3A49%3A24Z&skoid=e52d5ed7-0657-4f62-bc12-7e5dbb260a96&sks=b&skt=2023-11-17T09%3A49%3A24Z&sktid=33e01921-4d64-4f8c-a055-5bdaffd5e33d&skv=2020-10-02&sp=r&spr=https&sr=b&sv=2020-10-02', 'https://www.cashless.pl/14474-koniec-przelewow-pay-by-link'), ('Wystartowała nowa platforma z ofertami aut dostępnych od ręki: mamGO. Rozwiązanie od BNP Paribas', 'Grupa BNP Paribas uruchomiła w Polsce platformę mamGO, na której klienci mogą znaleźć oferty nowych i używanych samochodów od różnych dostawców i dealerów. Strona oferuje także sfinansowanie zakupu pojazdu poprzez kredyt samochodowy, leasing czy wynajem. Platforma pozwala z łatwością porównać modele samochodów, oferuje szczegółowe informacje o nich i umożliwia otrzymanie propozycji finansowania. Całość jest wynikiem współpracy między BNP Paribas bankiem, BNP Paribas Leasing Solutions, BNP Paribas Group Service Center oraz Arval.', 'https://dalleprodsec.blob.core.windows.net/private/images/e8993acf-a8ce-4eab-86cf-33e6c24333b1/generated_00.png?se=2023-11-18T10%3A01%3A08Z&sig=I%2FZlToZtWVvtw0FW7IDlbpsLr0q3kFHc8OpalqYdl9Q%3D&ske=2023-11-24T07%3A15%3A32Z&skoid=e52d5ed7-0657-4f62-bc12-7e5dbb260a96&sks=b&skt=2023-11-17T07%3A15%3A32Z&sktid=33e01921-4d64-4f8c-a055-5bdaffd5e33d&skv=2020-10-02&sp=r&spr=https&sr=b&sv=2020-10-02', 'https://www.cashless.pl/14461-BNP-Paribas-mamGO-platforma-oferty-aut-zakup'), ('Klarna przymierza się do giełdowego debiutu. Może do niego dojść już za kilka kwartałów', 'Szwedzka firma Klarna rozpoczyna przygotowania do IPO, tworząc spółkę holdingową w Wielkiej Brytanii. Termin i miejsce debiutu są nieznane. Kwestie dotyczące możliwego strajku zostały zażegnane dzięki porozumieniu z związkami zawodowymi. Wycena Klarny może przekroczyć 15 mld dolarów przed jej debiutem.', 'https://dalleprodsec.blob.core.windows.net/private/images/e12597e3-d271-4ac7-bf99-986d02d1ca94/generated_00.png?se=2023-11-18T10%3A01%3A56Z&sig=rNtnqTjwX3tRlxK%2BXjxQn3s3RPIvyX1gRA9RsaAMhmk%3D&ske=2023-11-24T07%3A15%3A32Z&skoid=e52d5ed7-0657-4f62-bc12-7e5dbb260a96&sks=b&skt=2023-11-17T07%3A15%3A32Z&sktid=33e01921-4d64-4f8c-a055-5bdaffd5e33d&skv=2020-10-02&sp=r&spr=https&sr=b&sv=2020-10-02', 'https://www.cashless.pl/14473-klarna-debiut-gieldowy-spolka-holdingowa'),('Pagbank z Brazylii osiąga 30M klientów, zajmuje miejsce wśród największych neobanków LatAm', 'Sektor bankowości cyfrowej w Brazylii dynamicznie rośnie. Nubank o wartości 30 miliardów dolarów aktywnie się rozwija w całej Ameryce Łacińskiej, podczas gdy portfel cyfrowy PicPay zdobywa miliony klientów. PagBank, cyfrowy oddział procesora płatności PagSeguro, stale zwiększa swoją bazę klientów, osiągając prawie 30 milionów w Brazylii. W obliczu nasycenia rynku, banki zaczynają skupiać się na zyskowności, a nie tylko na zdobyciu klientów.', 'https://dalleprodsec.blob.core.windows.net/private/images/d7c0459d-ffe8-46c6-8716-2c71ce3d9833/generated_00.png?se=2023-11-18T10%3A05%3A28Z&sig=tKZjDvalj%2F3i8%2B%2FPMW9TfRBI7omAcZ1bjAvyU1io5jA%3D&ske=2023-11-24T09%3A49%3A24Z&skoid=e52d5ed7-0657-4f62-bc12-7e5dbb260a96&sks=b&skt=2023-11-17T09%3A49%3A24Z&sktid=33e01921-4d64-4f8c-a055-5bdaffd5e33d&skv=2020-10-02&sp=r&spr=https&sr=b&sv=2020-10-02', 'https://www.fintechnexus.com/brazils-pagbank-hits-30m-clients-claims-a-spot-among-latams-largest-neobanks/')]
    opening_text = "W najnowszym newsletterze mamy dla Was wiele interesujących informacji z różnych dziedzin. Czytajcie o pierwszym chatbocie stworzonym przez Elona Muska, zmianach w preferencjach płatności internetowych Polaków, nowej platformie BNP Paribas oferującej kredyt samochodowy, leasing czy wynajem oraz o planach Szwedzkiej firmy Klarna na debiut giełdowy. Serdecznie zapraszamy do lektury!"
    summary_text = "Przyszłość sztucznej inteligencji przepełniona jest nieskończonymi możliwościami, które uczynią nasze codzienne życie prostsze, wydajniejsze i bardziej innowacyjne."
    generate_pdf_for_list(input_data_list, opening_text=opening_text, summary_text=summary_text)