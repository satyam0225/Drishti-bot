from gpt4all import GPT4All
import datetime

def localGreetingAi():
    model = GPT4All("orca-mini-3b-gguf2-q4_0.gguf",model_path="./model" ,allow_download=False)
    system_prompt = "### System:Create a model to greet users based on 24-hour time input. It should recognize morning, afternoon, and evening, responding with suitable messages. For example, between 00:00-11:59, greet 'Good morning!'; 12:00-17:59, 'Good afternoon!'; and 18:00-23:59, 'Good evening!'. Ensure friendly, tailored responses for a pleasant user experience. \n\n "
    prompt_template = '### User:\n{0}\n\n### Response:\n'
    with model.chat_session(system_prompt,prompt_template):
        r1=model.generate(f"current time is {datetime.datetime.now():%H:%M} in 24 hour format.")
        r2=model.generate("greet the user" ,max_tokens=50)
        
        model.close()
        return r2



def localAi(prompt:str):
    model = GPT4All("orca-mini-3b-gguf2-q4_0.gguf",model_path="./model" ,allow_download=False)
    system_prompt = '### System:\nYou are an AI assistant that follows instruction extremely well. Help as much as you can.\n\n'
    prompt_template = '### User:\n{0}\n\n### Response:\n'
    with model.chat_session(system_prompt,prompt_template):
        r1=model.generate(prompt,max_tokens=1000)
        return r1

# print(localAi("what is the capital of assam?"))
# print(localGreetingAi())