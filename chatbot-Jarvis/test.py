from transformers import AutoModelForCausalLM, AutoTokenizer
import os
os.environ["TOKENIZERS_PARALLELISM"] = "false"
model_name = "microsoft/DialoGPT-medium"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)
def myChatBot(user_input):
    inputs = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors="pt")
    chat_history_ids = model.generate(inputs, max_length=1000, pad_token_id=tokenizer.eos_token_id)
    response = tokenizer.decode(chat_history_ids[:, inputs.shape[-1]:][0], skip_special_tokens=True)
    return response
# Load pre-trained model and tokenizer

# Chat loop
# print("ChatBot: Hi! Type 'exit' to end the conversation.")

    
