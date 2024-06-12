# Test RAG Chatbot

This project aims to implement the state-of-the-art techniques in Retrieval-Augmented Generation (RAG). Our primary objective is to collaboratively engage in a hands-on, end-to-end project that leverages the latest advancements in the LangChain library <img src="img/langchain.png" alt="Description" width="20"/>.Additionally, we focus on the interaction with the vector database Pinecone <img src="img/pinecone.png" alt="Description" width="15"/> 
 ensuring a cutting-edge approach to data management and retrieval.

 ![Project Logo](img/img.png),

## Table of Contents

1. [Introduction](#introduction)
2. [Readiness](#readiness)
    - [OpenAI](#OpenAI)
    - [Pinecone](#Pinecone)
    - [Langchain](#Langchain)
3. [Vector database population](#vector-database-population)
4. [Retrieval-Augmented Generation (RAG)](#Retrieval-Augmented-Generation-(RAG))
5. [Web application](#Web-application)
6. [Deployment](#Deployment)

## Introduction

Welcome to the ChatBotRAG project, where we embark on a journey to showcase the cutting-edge advancements in conversational AI technology. Our primary goal is to demonstrate the state-of-the-art capabilities of Retrieval-Augmented Generation (RAG), a powerful approach that combines retrieval-based methods with generative models to create more contextually relevant responses.

At the heart of our project lies the integration of advanced tools and technologies. We leverage the Vector Database Pinecone, a high-performance, scalable solution for storing and querying high-dimensional vector data. By harnessing the power of Pinecone, we ensure rapid and efficient retrieval of relevant information to enrich the conversational experience.

Additionally, we utilize the LangChain library, a sophisticated toolkit that empowers us to implement the latest advancements in natural language processing. With LangChain, we can seamlessly integrate state-of-the-art language models and techniques into our chatbot, enabling it to understand and generate human-like responses with unparalleled accuracy and fluency.

To bring our project to life, we employ a Flask Python server, providing a robust and flexible platform for hosting our chatbot. The Flask server acts as the backbone of our system, facilitating communication between the user interface and the backend components, ensuring smooth and seamless interactions.

Furthermore, we have enriched our database by loading the author's Curriculum Vitae (CV) and postgraduate thesis. By incorporating this valuable information into the database, we enhance the chatbot's ability to provide insightful and relevant responses, tailored to the user's queries and interests.

The model block diagram is represented as:

 ![Project Logo](img/chatbotdrawio.png),


## Readiness
Before diving into the project coding, it's essential to set up accounts with Pinecone, OpenAI, and LangChain. These accounts will serve as the foundation for accessing the necessary tools and APIs required for the project's development. By creating accounts with these platforms, you gain access to powerful technologies that will enable you to leverage cutting-edge capabilities in vector database management, natural language processing, and AI-powered generation.

### OpenAI
OpenAI offers a suite of powerful APIs and models for natural language processing and generation. With an OpenAI account, you gain access to state-of-the-art language models, including GPT (Generative Pre-trained Transformer) models, which can be used to power your chatbot's conversational capabilities.
To know how to get your OpenAI API key: https://www.youtube.com/watch?v=6LAl5IJM080

### Pinecone
Pinecone provides a scalable vector database solution, allowing you to store and query high-dimensional vector data efficiently. By creating a Pinecone account, you can set up your vector database, configure indexing parameters, and integrate it seamlessly into your project workflow.
To get started with Pinecone follow this video: https://www.youtube.com/watch?v=AGKY_Q3GjRc

### Langchain
LangChain provides a comprehensive library of tools and resources for implementing advanced language processing techniques. By creating a LangChain account, you can access pre-trained models, libraries, and utilities that will streamline the development process and enhance the performance of your chatbot.
It is recommended to register and implement LangSmith.

## Vector database population

To populate the Pinecone DB you have to execute this notebook: [inicial.ipynb](inicial.ipynb)