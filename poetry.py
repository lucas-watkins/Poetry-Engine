from happytransformer import HappyGeneration, GENSettings
from os import system
from random import random, randint

system('cls')
prompt = input('Write your first line of poetry here: \n>>> ')

lucasAI = HappyGeneration(load_path = 'model')
 
top_k_sampling_settings = GENSettings(do_sample=True, top_k=50, max_length=randint(50,75), min_length=10, temperature=random())

output_top_k_sampling = lucasAI.generate_text(prompt, args=top_k_sampling_settings)

system('cls')
print('Generated Poem:\n\n' + prompt + output_top_k_sampling.text.replace('    ', '\n'))