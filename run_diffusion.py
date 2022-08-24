
import os
import sys
import torch
from diffusers import StableDiffusionPipeline

pipe = StableDiffusionPipeline.from_pretrained(
    "CompVis/stable-diffusion-v1-4", 
    revision="fp16", 
    torch_dtype=torch.float16, 
    use_auth_token=os.environ["DIFFUSION_TOKEN"]
)
pipe = pipe.to("cuda")

prompt = sys.argv[1]

filename = f'{prompt.replace(" ", "_")}.png'
with torch.autocast("cuda"):
    image = pipe(prompt)["sample"][0]
    image.save(f"/workspace/images/{filename}")

