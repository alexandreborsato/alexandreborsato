import os
import pypdf
import pyttsx4
from pypdf import PdfReader

#review: https://pypi.org/project/pyttsx4/
#review: https://pypi.org/project/PyPDF4/


text = ""

# Get the PDF file path from the user
pdf_file = input("Enter the path to the PDF file: ")

# Open the PDF file
with open(pdf_file, 'rb') as file:
    # Create a PDF reader object

    # Loop through each page and extract the text
    reader = pypdf.PdfReader(file)
    for page in reader.pages:
        text += page.extract_text()

print(text)

          

    # Initialize the text-to-speech engine
engine = pyttsx4.init()
#for voice in engine.getProperty('voices'):
 #   print(voice)

    
    # Set the speech rate (optional)
engine.setProperty('rate', 150)
engine.setProperty('voice', "com.apple.voice.compact.pt-BR.Luciana")
# Eddy, Flo, Luciana, Reed, Rocko, Sandy, 
    
    # Save the audio to an MP3 file
audio_file = os.path.splitext(pdf_file)[0] + ".wav"
engine.save_to_file(text, audio_file)
engine.runAndWait()
    
print(f"Audio file saved as: {audio_file}")
