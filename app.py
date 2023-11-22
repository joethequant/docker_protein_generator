import runpod

import torch
import torch.nn as nn
from tokenizers import Tokenizer
from models.progen.modeling_progen import ProGenForCausalLM

model_id = 'simple_fine_tuned_progen2-small'

def is_even(job):   

    job_input = job["input"]
    target_sequence = job_input["target_sequence"]
    number_of_sequences = job_input["number_of_sequences"]

    if not isinstance(target_sequence, str):
        return {"error": "Silly human, you need to pass a string."}

    if not isinstance(number_of_sequences, int):
        return {"error": "Silly human, you need to pass an integer."}


    model_path = f'model_checkpoints/{model_id}'
    device = 'cuda:0'  # Define the device variable outside the if-else condition

    # Initialize the model first
    model = ProGenForCausalLM.from_pretrained(model_path).to(device)

    # Check if multiple GPUs are available and use ProGen's parallelization
    if torch.cuda.device_count() > 1:
        # print(f"Using {torch.cuda.device_count()} GPUs!")
        model.parallelize() # ProGen's parallelize method
    else:
        print(f'Device: {device}')
    
    def predict_sequence(model, tokenizer, sequence, device='cuda:0', number_of_sequences=1 ):
        # Tokenize the sequence
        tokenized_sequence = tokenizer.encode(sequence)
        
        # Convert to PyTorch tensor and add batch dimension
        input_tensor = torch.tensor([tokenized_sequence.ids]).to(device)
        
        # Pass the tensor through the model
        with torch.no_grad():
            output = model.generate(input_tensor, max_length=1024, pad_token_id=tokenizer.encode('<|pad|>').ids[0], do_sample=True, top_p=0.9, temperature=0.8, num_return_sequences=number_of_sequences)

            as_lists = lambda batch: [batch[i, ...].detach().cpu().numpy().tolist() for i in range(batch.shape[0])]
            sequences = tokenizer.decode_batch(as_lists(output))

            if len(sequences) > 0:
                sequences = [x.replace('2', '') for x in sequences] #replace stop token with empty string
            else:
                return []
            
            return sequences

    tokenizer = Tokenizer.from_file('tokenizer.json')

    test = predict_sequence(model, tokenizer, target_sequence, device, number_of_sequences=number_of_sequences)

    return test

runpod.serverless.start({"handler": is_even})