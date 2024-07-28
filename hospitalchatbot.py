

pip install python-aiml

import aiml

# Create the kernel and learn AIML files
kernel = aiml.Kernel()
kernel.learn('/content/Hospital_ChatBot.xml')
kernel.respond("load prac 2")

while True:
    input_text= input(">Human: ")
    response =kernel.respond(input_text)
    print(">Bot: "+response)

