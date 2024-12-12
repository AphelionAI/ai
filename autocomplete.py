"""

Autocomplete Code:
Aphelion Autocomplete will automatically determine context based on the current cursor position

Must use following factors:
File prefix/suffix
Imported files (some)
Recent files
Surrounding code

Models: Codestral or Ollama

Referencing: https://github.com/continuedev/continue/blob/main/docs/docs/customize/deep-dives/autocomplete.md

Ignore jetbrains for the moment, get everything working for VSCode and then move on to jetbrains

"""

"""
PSEUDO:




"""


import model

class autoCompleter:
    def __init__(self, model, useFileAffixes: bool, debounceDelay: int):
        """
        AutoComplete class for Aphelion tab auto code completion.

        model: any -> The LLM model used for code auto-completion
        useFileAffixes: bool -> Use the current file prefix/suffix for predictions
        debounceDelay: bool -> The time (in ms) for the debounce delay
        """

    def autoComplete(self, model)