# AntibodyGPT:  Runpod Serverless Antibody Protein Generation API

This repository contains the code for the docker image published to dockerhub.

## AntibodyGPT: A Fine-Tuned GPT for De Novo Therapeutic Antibodies

- [Web Demo](https://orca-app-ygzbp.ondigitalocean.app/Demo_Antibody_Generator)
- [Huggingface Model Repository](https://huggingface.co/AntibodyGeneration)

Antibodies are proteins that bind to a target protein (called an antigen) in order to mount an immune response. 
They are incredibly **safe** and **effective** therapeutics against infectious diseases, cancer, and autoimmune disorders.

Current antibody discovery methods require a lot of capital, expertise, and luck. Generative AI opens up the possibility of 
moving from a paradigm of antibody discovery to antibody generation. However, work is required to translate the advances of LLMs to the realm of drug discovery.

AntibodyGPT is a fine-tuned GPT language model that researchers can use to rapidly generate functional, diverse antibodies for any given target sequence

## Getting Started

You can directly use the published image on docker hub in runpod by referencing:

**robertsj32/antibody_generation_runpod:latest**

This image is located here:

[https://hub.docker.com/repository/docker/robertsj32/antibody_generation_runpod/general](https://hub.docker.com/repository/docker/robertsj32/antibody_generation_runpod/general)


Once the image is published as an endpoint on Runpod you can call the api using the below as reference:

```python 
url = f'https://api.runpod.ai/v2/{runpod_id}/run'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {runpod_secret}'
        }

        # The JSON data payload
        data = {
            'input': {
                "model_name": model_name,
                "target_sequence": target_sequence_input,
                "number_of_sequences": number_of_sequences
            },
            "policy":{
                "executionTimeout": 600000 # 10 minutes in miliseconds -> Stop run away costly GPU jobs.
            }
        }

        # Make the POST request
        response = requests.post(url, json=data, headers=headers)
```

### Prerequisites

- Docker: The application is containerized with Docker, so you'll need Docker installed on your machine. You can download Docker [here](https://www.docker.com/products/docker-desktop).


### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/joethequant/docker_protein_generator.git
    ```

2. Navigate to the project directory:
    ```bash
    cd docker_protein_generator
    ```

4. Build and push to dockerhub: Edit contents to your location.
    ```bash
    build_and_push.sh
    ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.