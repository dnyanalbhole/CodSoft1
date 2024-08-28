text = ""

def chatbot(user_input):
    user_input = user_input.lower()  # Convert input to lowercase for easier matching

    if "hello" in user_input or "hi" in user_input:
        return "hello! how can i assist you today?"
    
    elif "how are you" in user_input:
        return "i'm just a bot, but i'm doing great! how about you?"
    
    elif "what's your name" in user_input or "name" in user_input:

        return "i'm a simple chatbot created by openai's gpt-4. what's your name?"
    
    elif "bye" in user_input or "goodbye" in user_input:
        return "goodbye! have a great day!"
    
    elif "thank you" in user_input or "thanks" in user_input:
        return "you're welcome! happy to help."
    
    elif "weather" in user_input:
        return "i'm unable to provide real-time weather updates, but you can check a weather website or app for the latest information."
    

    elif "time" in user_input:
        from datetime import datetime
        now = datetime.now()
        return f"the current time is {now.strftime('%h:%m:%s')}."
    

    elif "date" in user_input:
        from datetime import datetime
        today = datetime.today()
        return f"today's date is {today.strftime('%y-%m-%d')}."
    
    elif "joke" in user_input:
        return "why don't scientists trust atoms? because they make up everything!"
    elif "favorite color" in user_input:
        return "as an ai, i don't have a favorite color, but i think all colors are amazing!"
    elif "creator" in user_input:
        return "i was created by the team at openai."
    
    elif "where are you from" in user_input:
        return "i exist in the cloud, so i don't have a physical location."
    elif "favorite food" in user_input:
        return "as an ai, i don't eat, but i hear pizza is quite popular!"
    elif "hobby" in user_input:
        return "i like to help people with their questions and learn new things."
    elif "age" in user_input:
        return "i don't have an age like humans do, but i was created in 2023."
    elif "tell me a fact" in user_input:
        return "did you know that honey never spoils? archaeologists have found pots of honey in ancient egyptian tombs that are over 3,000 years old and still edible."
    elif "favorite animal" in user_input:
        return "i think all animals are interesting, but i've heard many people love dogs and cats."
    elif "language" in user_input:
        return "i can understand and respond in many languages, but i'm currently using english."
    elif "sports" in user_input:
        return "i don't play sports, but soccer and basketball are very popular worldwide."
    
    elif "music" in user_input:
        return "  i can't listen to music, but i know many people enjoy pop, rock, and classical music."
    
    elif "movie" in user_input:

        return "i don't watch movies, but some popular ones include 'the godfather', 'star wars', and 'the shawshank redemption'."
    elif "book" in user_input:
        return "there are many great books, but 'to kill a mockingbird' by harper lee is a classic."
    elif "travel" in user_input:
        return "i can't travel, but i hear that places like paris, tokyo, and new york city are amazing to visit."
    elif "news" in user_input:
        return "i can't provide real-time news updates, but you can check a news website or app for the latest information."
    
    elif "math" in user_input:
        return "i can help with math problems! what do you need help with?"
    elif "science" in user_input:
        return "science is fascinating! do you have a specific question about science?"
    elif "history" in user_input:
        return "history is full of interesting events and people. do you have a specific question about history?"
    
    elif "technology" in user_input:
        return "technology is always advancing. do you have a specific question about technology?"
    
    elif "coding" in user_input:
        return "i can help with coding questions. what language are you working with?"
    elif "python" in user_input:
        return "python is a great programming language. what do you need help with in python?"
    
    elif "java" in user_input:
        return "java is a popular programming language. what do you need help with in java?"
    elif "javascript" in user_input:
        return "javascript is essential for web development. what do you need help with in javascript?"
    elif "html" in user_input:
        return "html is the backbone of web pages. what do you need help with in html?"
    
    elif "css" in user_input:
        return "css styles web pages. what do you need help with in css?"
    else:
        return "i'm not sure how to respond to that. can you ask something else?"

while True:
    text = input("ask your question: ")
    if text.lower() == "exit":
        break
    
    print("chatbot:", chatbot(text))
