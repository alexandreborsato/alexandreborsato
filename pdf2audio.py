#transform PDF to Audio
#pip install pyttsx3
import pyttsx3,PyPDF2

from PyPDF2 import PdfReader

#insert name of your pdf 
pdfreader = PdfReader(open('/Users/borsatoa/Desktop/AB/Actual/lab/03/book.pdf', 'rb'))

speaker = pyttsx3.init()

page_num = len(pdfreader.pages)
page = pdfreader.pages[0]

text = page.extract_text()
clean_text:str
#loop through each page
#if page_num != 0:
 #   for page_num in len(pdfreader.pages):
  #      text = pdfreader.getPage(page_num).extractText()
   #     clean_text = text.strip().replace('\n', ' ')
    #    print({clean_text})

#name mp3 file whatever you would like
print(text)

# speaker.say(text)
securitytext = text
#"Security groups in a VPC enable you to specify both inbound and outbound network traffic that is allowed to or from each Amazon EC2 instance. Traffic which is not explicitly allowed to or from an instance is automatically denied. Security groups in a VPC specify which traffic is allowed to or from an Amazon EC2 instance. Network ACLs operate at the subnet level and evaluate traffic entering and exiting a subnet. Network ACLs can be used to set both Allow and Deny rules. Network ACLs do not filter traffic between instances in the same subnet. In addition, network ACLs perform stateless filtering while security groups perform stateful filtering. "

speaker.save_to_file(text, 'story.aiff')
speaker.save_to_file(securitytext, 'fromfile.aiff')
speaker.save_to_file("Hello, this is test for Traffic which is not explicitly allowed to or from an instance is automatically denied. Security groups in a VPC specify which traffic is allowed to or from an Amazon EC2 instance.", "testii.mp3")
speaker.runAndWait()
speaker.stop()
