from happytransformer import HappyGeneration, GENTrainArgs, GENSettings

gpt_neo = HappyGeneration(model_type="GPT-NEO", model_name="EleutherAI/gpt-neo-125M") 

train_args = GENTrainArgs(num_train_epochs=1, learning_rate=2e-05, batch_size=1) 

gpt_neo.train("trainingdata.txt", args=train_args)

gpt_neo.save('model')