def autoCompletePrompt(fileType: str, prefix: str):
    return f"Autocomplete the rest of the line for following code in a file with the extension: {fileType}. The code is: {prefix}"