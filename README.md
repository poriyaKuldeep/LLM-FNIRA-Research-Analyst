
 # LLM-FNIRA: URL Analysis AI Platform for Deeper Insights in Finance, Stock Market, and News

LLM-FNIRA (Language Learning Model - Finance News Insights and Research Assistant) is an advanced AI platform designed to analyze URLs from finance, stock market, and news domains to provide deeper insights without requiring a full article read. With LLM-FNIRA, users can input URLs, ask questions, and receive cited sources, enabling efficient research and analysis in these critical domains.

## Why LLM-FNIRA?

In today's fast-paced world, staying updated with the latest developments in finance, stock markets, and news is crucial for making informed decisions. However, the sheer volume of information available can be overwhelming, making it challenging to sift through and extract relevant insights efficiently. LLM-FNIRA addresses this challenge by leveraging cutting-edge AI technologies to analyze URLs and distill key information, saving users time and effort while enhancing their research capabilities.

## How LLM-FNIRA Can Help Research and Analysis

### 1. Efficient Information Extraction
LLM-FNIRA streamlines the process of gathering insights by extracting relevant information from URLs without the need for users to read entire articles. This enables researchers and analysts to focus their time and attention on analyzing insights rather than searching for relevant content.

### 2. Citation of Sources
One of the key features of LLM-FNIRA is its ability to provide cited sources for the information it presents. This not only helps users verify the credibility of the information but also facilitates further exploration and in-depth analysis.

### 3. Customized Queries
Users can ask specific questions related to finance, stock markets, or news topics, and LLM-FNIRA will provide targeted responses based on the content of the input URLs. This feature allows for tailored analysis and enables users to gain insights on specific aspects of interest.

### 4. Deep Insights Without Full Article Read
By employing advanced natural language processing techniques, LLM-FNIRA is capable of extracting deep insights from URLs even without users having to read the full articles. This capability is particularly valuable in scenarios where time is limited, and quick access to relevant information is essential.

### 5. Seamless Integration
LLM-FNIRA can be seamlessly integrated into existing research and analysis workflows, enhancing productivity and enabling users to leverage its capabilities without disrupting their established processes.

## Features

### 1. Langchain
Langchain is a proprietary language processing engine that powers LLM-FNIRA's ability to understand and extract insights from URLs. It utilizes state-of-the-art natural language processing algorithms to parse text and identify key information relevant to finance, stock markets, and news.

### 2. LLM (Language Learning Model)
LLM is the core machine learning model behind LLM-FNIRA, trained on vast amounts of financial and news data to understand complex financial concepts and extract insights accurately. LLM continually learns and improves over time, ensuring that LLM-FNIRA stays up-to-date with the latest trends and developments in the finance and news domains.

### 3. Streamlit Interface
LLM-FNIRA features a user-friendly Streamlit interface that allows users to interact with the platform effortlessly. The Streamlit interface provides intuitive controls for inputting URLs, asking questions, and exploring insights, making it easy for users to harness the power of LLM-FNIRA for their research and analysis needs.

## Getting Started

To start using LLM-FNIRA, simply follow these steps:

1. Clone the repository to your local machine.
2. Install the necessary dependencies as specified in the documentation.
3. Run the application and input the URLs you wish to analyze.
4. Ask questions or explore the insights provided by LLM-FNIRA.
5. Experiment with different URLs and queries to further explore its capabilities.

## Sample Output:
![output new new final](https://github.com/fenil210/Research-Analyst/assets/121050723/6a7c69b8-bff9-434f-9f64-079896aab04e)



## Used News URLs:
1) https://www.business-standard.com/finance/news/sovereign-gold-bonds-help-save-3-3-billion-in-india-s-gold-import-bill-124031000374_1.html
2) https://www.business-standard.com/finance/news/sidbi-secures-first-green-climate-fund-project-worth-120-million-124031100590_1.html

## Acknowledgements
[OpenAI](https://openai.com/) for providing access to the GPT 3.5 Turbo model.

[Streamlit](https://streamlit.io/) for simplifying the development of interactive web applications.

[Langchain](https://www.langchain.com/) for ensuring content integrity through blockchain integration.

[Dhaval Patel](https://www.linkedin.com/in/dhavalsays/) for LLM, Streamlit and Langchain guidance.

## Installation

1.Clone this repository to your local machine using:

```bash
  git clone [https://github.com/codebasics/langchain.git](https://github.com/poriyaKuldeep/News_Research_Tool_project.git)
```
2. Install the required dependencies using pip:

```bash
  pip install -r requirements.txt
```
3.Set up your OpenAI API key by creating a .env file in the project root and adding your API

```bash
  OPENAI_API_KEY=your_api_key_here
```
## Usage/Examples

1. Run the Streamlit app by executing:
```bash
streamlit run main.py

```

2.The web app will open in your browser.

- On the sidebar, you can input URLs directly.

- Initiate the data loading and processing by clicking "Process URLs."

- Observe the system as it performs text splitting, generates embedding vectors, and efficiently indexes them using FAISS.

- The embeddings will be stored and indexed using FAISS, enhancing retrieval speed.

- The FAISS index will be saved in a local file path in pickle format for future use.
- One can now ask a question and get the answer based on those news articles.

## Project Structure

- main.py: The main Streamlit application script.
- requirements.txt: A list of required Python packages for the project.
- faiss_store_openai.pkl: A pickle file to store the FAISS index.
- .env: Configuration file for storing your OpenAI API key.




