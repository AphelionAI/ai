from transformers import pipeline as pipe
import torch

class Model:
    """Wrapper class for all model types"""
    def __init__(self, model_name: str, model_dir: str):
        super().__init__()

        self.model_name = model_name
       
        self.model = pipe(
            "text-generation",
            model=model_dir,
            model_kwargs={"torch_dtype": torch.bfloat16},
            device_map="auto",
        )

            

    def call(self, prompt: str) -> str:
        response = self.model(prompt)
        return response[0]["generated_text"[-1]["content"]]
