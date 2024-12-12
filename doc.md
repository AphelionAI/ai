# Project Overview

## 3. Vector Database
### 3.01. Chunking
Each file of code in the directory will be chunked according to a specified size and then embedded into a vector database which can then be indexed from according to specific queries.

## 2. Autocomplete
### 2.01. Autocomplete Process Overview
Step 1. Upon detecting the correct moment for an autocomplete suggestion (more on that later), Aphelion will gather several pieces of information. This information includes:
>1. The prefix/suffix of the file in which the user is coding. This will then be used with a lookup dictionary to determine the name of the language (e.g .py = Python)
>2. The code surrounding the current position of the cursor.
>3. A specified number of relevant code chunks indexed from the vector database based on the current line of code

Once these pieces of information are gathered, they will be combined into a prompt for the LLM to understand and then sent to the LLM for it to generate an autocomplete result.