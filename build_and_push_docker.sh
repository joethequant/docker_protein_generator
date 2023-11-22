pip freeze > requirements.txt

docker build . --tag=robertsj32/antibody_generation_runpod:latest

docker push robertsj32/antibody_generation_runpod:latest