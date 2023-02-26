# Azure OpenAI Service Advanced Samples

This repository provides sample code and instructions on how to use Azure OpenAI Service, Azure Search Service, and Azure Speech Service together to perform natural language searches and question answering.

## Prerequisites

Before you begin, you must have the following:

- A Windows machine with [WSL 2.0](https://learn.microsoft.com/en-us/windows/wsl/install), Ubuntu 20.04, and [VSCode](https://code.visualstudio.com/) installed, or a Linux machine with [VSCode](https://code.visualstudio.com/) installed.
- [Python 3.9](https://www.python.org/downloads/release/python-390/) or above and relevant pip packages installed.
- An Azure account with an active subscription. If you don't have an account, you can create a [free trial account](https://azure.microsoft.com/en-us/free/).
- An instance of [Azure OpenAI Service](https://azure.microsoft.com/en-us/services/cognitive-services/openai/).
- An instance of [Azure Search Service](https://azure.microsoft.com/en-us/services/search/).
- An instance of [Azure Speech Service](https://azure.microsoft.com/en-us/services/cognitive-services/speech-services/).

## Getting Started

To use this code, follow these steps:

1. Clone this repository to your local machine:

   ```
   git clone https://github.com/alezhao/openai.git
   ```

2. Navigate to the `notebook` folder.

3. Open the desired notebook in VSCode.

4. Replace the placeholder values in the notebook with your Azure service credentials e.g. <OPENAI_API_KEY>.

5. Run the notebook or python code, following the instructions provided in the comments.

## Samples

#### **Document Process Automation**

![](images\dpa.jpg)

### [openai_azure_search_with_summary_all.ipynb](https://github.com/alezhao/openainotebooks/openai_azure_search_with_summary_all.ipynb)

This notebook provides an example of how to use Azure OpenAI Service and Azure Search Service together to perform natural language searches on a given query. It demonstrates how to use the OpenAI Service to process natural language queries, and Azure Search Service to perform the search and the summary against the query.

<br>

#### **Contact Center Analytics using Speech API & OpenAI (only include key code)** 

![](images\speech_openai.jpg)

### [qa_aoai_speech.py](https://github.com/alezhao/openai/notebooks/qa_aoai_speech.py)

This notebook provides an example of how to use Azure OpenAI Service and Azure Speech Service together to perform question answering, including speech-to-text (STT) and text-to-speech (TTS). It demonstrates how to use the OpenAI Service to process natural language queries and generate responses, and Azure Speech Service to convert audio input to text and text output to audio.

<br>

## References

- [Azure OpenAI Service documentation](https://docs.microsoft.com/en-us/azure/cognitive-services/openai-index)
- [Azure Search Service documentation](https://docs.microsoft.com/en-us/azure/search/)
- [Azure Speech Service documentation](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/index)
- [Python documentation](https://docs.python.org/3/)