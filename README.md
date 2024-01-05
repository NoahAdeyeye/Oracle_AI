# Oracle_AI

## Introduction

Welcome to Oracle_AI, a personal project that attempts to use artificial intelligence, inspired by iconic figures such as Ironman, Batman, and Blue Beetle. The aim is to use AI tools to enhance user experiences. In homage to Batman, the personal AI in this project is named "Oracle."

## Project Overview

The project utilizes Python to create an AI using the GPT-3.5-turbo model from OpenAI. The AI, Oracle, can answer user queries and engage in dialogue. Additionally, the project includes speech recognition and text-to-speech functionalities for a more interactive experience.

## Code Structure

The code has two main factors:

### Conversational AI

This section includes the implementation of a Conversational Retrieval Chain using the langchain library. It uses OpenAI's GPT-3.5-turbo model to answer user questions based on a pre-loaded index. The AI's responses are stored in a chat history for a more interactive and context-aware experience.

### Speech Recognition and Text-to-Speech

The second section focuses on speech recognition and text-to-speech functionalities. The code uses the SpeechRecognition library for audio input and integrates OpenAI's ChatCompletion for generating responses. The text-to-speech feature is implemented using the gTTS (Google Text-to-Speech) library and pyttsx3.

## Getting Started

1. Clone the repository.
2. Install the required dependencies.
3. Replace the `APIKEY` and `api_key` variables with your OpenAI API key.
4. Run the code to interact with Oracle_AI.

## Usage

1. Execute the code.
2. Enter prompts or questions when prompted for user input.
3. Explore the conversational capabilities of Oracle.
4. Optionally, use speech recognition by saying "Friday" and follow the prompts (testing differnt names now, yes this is from Ironman).

## Notes

- Ensure your API key is securely stored and never shared publicly.
- Customize the code to further enhance Oracle_AI based on your preferences.
- I will eventually dabble in image recognition when I have practiced with this model more!

Enjoy Oracle_AI, and feel free to contribute or provide feedback!
