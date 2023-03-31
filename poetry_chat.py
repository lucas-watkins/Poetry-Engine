from happytransformer import HappyGeneration, GENSettings
from os import system
from gingerit.gingerit import GingerIt

system('cls')
prompt = '\n AI: Hello how are you?\n User: Hi, I am doing well\n AI: What can I do for you?\n User: Thank you!\n AI: You\'re welcome\n User: Could you write me a poem about '
poem = input('What would you like to a poem about: \n>>> ')

lucasAI = HappyGeneration(load_path = 'model')
 
top_k_sampling_settings = GENSettings(do_sample=True, top_k=50, max_length=100, min_length=10, temperature=3.5)

output_top_k_sampling = lucasAI.generate_text(prompt + poem + ' please?', args=top_k_sampling_settings)

system('cls')

print('Generated Poem:\n\n' + str(GingerIt().parse(str(GingerIt().parse(output_top_k_sampling.text)['result']))['result']))
#print('-----------------------------------------')
#print(output_top_k_sampling.text)