## [Youtube](https://www.youtube.com/watch?v=K8dJ8bmF3TU)


MLOPS Tutorials :


Deploy ML flask App in : 
	- AWS Fargate ===>  Tutorial already done ✅
	- GCP ===> Tutorial already done ✅
	- Azure Cloud ===> Tutorial already done ✅


Build, train and deploy models in AWS Sagemaker ===> Tutorial already done ✅

Build Gradio app and deploy in Hugging Face ===> covered today 🏃


Build Streamlit app and deploy in Render hosting solution


ML Pipelines :
	- ZenML
	- MLFlow
	- KubeFlow
	- DVC
	- Pycaret




# Build Gradio app and deploy in Hugging Face

conda create -n pycaretenv python=3.8
	conda activate pycaretenv
	pip install pycaret
	pip install ipykernel
	python -m ipykernel install --user --name pycaretenv --display-name "pycaretenvkernel"
	lancer jupyter depuis batch
	jupyter notebook

Got to the https://huggingface.co/davidtchouta
Create a space
Upload file 

See your gradio app in action







---
title: Irispace
emoji: 👀
colorFrom: blue
colorTo: pink
sdk: gradio
sdk_version: 4.16.0
app_file: app.py
pinned: false
license: mit
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference
