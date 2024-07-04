import boto3

client = boto3.client('translate')

def translate_text():
    response = client.translate_text(
        Text = input(f"Enter the text you want to translate: "),
#### Add the new text below this line ####

        SourceLanguageCode = input(f"Enter the source language code: "),
        TargetLanguageCode = input(f"Enter the destination langurage code: "),
    )
#### Add the new text below this line ####
    print(response)

    # this code is inside the function and will print the contents of the variable 'response'

translate_text()

# This line will call our function. Without it, python will not do anything.
