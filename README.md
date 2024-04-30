# simple-rag-app
Can AI explain itself? In other words, if I take an AI model and ask it questions about any another AI model, I would expect it to answer my questions. But it turns out that the model simply doesn't know about any other models. 

Can a simple workaround for this problem lies with Retrieval Augmented Generation or RAG in short? This repo implements a RAG pipeline using LangFlow and StreamLit to develop an App called, "AI Explans AI".

### YouTube video 
Checkout the below YouTube video which walks through the app development.
[![AI explains AI](https://img.youtube.com/vi/1ic-V0TCscM/0.jpg)](https://www.youtube.com/watch?v=1ic-V0TCscM&t=31s)


### Installation
* Clone the repo 
```
git clone git@github.com:ai-bites/simple-rag-app.git
```
* Its important that the vwe are in  `python 3.10` to get the installation right. Then we just need `langflow` `streamlit` and `langchain-community`
```
conda create -n rag-app python=3.10
conda activate rag-app
pip install langflow
pip install streamlit
pip install langchain-community
```

### Running the app
To run the app directly, just run streamlit on `app.py`.
```
streamlit run app.py
```
If you just want to run langflow, run langflow and import the `json` file
```
langflow run
```


