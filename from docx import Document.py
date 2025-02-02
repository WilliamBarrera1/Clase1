from docx import Document
from wordcloud import WordCloud

# Open the .doc document
doc = Document('document.docx')

# Extract the text from the document
text = ""
for paragraph in doc.paragraphs:
    text += paragraph.text

# Generate the word cloud
wordcloud = WordCloud().generate(text)

# Save the word cloud as an image file
wordcloud.to_file("wordcloud.png")

#  Codigo nuevo
