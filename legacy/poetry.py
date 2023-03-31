from happytransformer import HappyGeneration, GENSettings
from os import system
from random import random, randint
from gingerit.gingerit import GingerIt

system('cls')
prompt = input('Write your first line of poetry here: \n>>> ')

lucasAI = HappyGeneration(load_path = 'model')
 
top_k_sampling_settings = GENSettings(do_sample=True, top_k=50, max_length=100, min_length=10, temperature=3.5)

output_top_k_sampling = lucasAI.generate_text(prompt, args=top_k_sampling_settings)

system('cls')
print('Generating...')
generated_poem = list(str(GingerIt().parse(output_top_k_sampling.text)['result']))

print('Grammar Corrected...')
# Add periods affter random space and captial letter

counter1 = 0
for i in generated_poem:
    counter1 += 1
    if i == ' ' and generated_poem[counter1 + 1].isupper() and generated_poem[counter1 - 1].islower():
        generated_poem.insert(counter1, '.')
        print('Period Inserted')
    print('Counter1 Value:', counter1)
print('Periods Removed...')

# Sepearates words
counter2 = -1
try:
    for c in generated_poem:
        counter2 += 1
        if c.islower() and generated_poem[counter2 + 1].isupper():
            generated_poem.insert(counter2 + 1, ' ')
    
    print('Counter2 Value:', counter2)
except IndexError:
    pass
print('Spaces Removed...')

# Add periods affter random space and captial letter

counter1 = 0
for i in generated_poem:
    counter1 += 1
    if i == ' ' and generated_poem[counter1 + 1].isupper() and generated_poem[counter1 - 1].islower():
        generated_poem.insert(counter1, '.')
        print('Period Inserted')
    print('Counter1 Value:', counter1)
print('Periods Removed...')

final_poem = ''
for j in generated_poem:
    final_poem += j
final_poem = final_poem.replace('""','"')
final_poem = final_poem.replace('--','')
final_poem = final_poem.replace('_', '')
print('Poem loaded...')

system('cls')
print('Generated Poem:\n\n' + prompt + final_poem)