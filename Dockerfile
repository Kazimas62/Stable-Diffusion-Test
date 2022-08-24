FROM pytorch/pytorch:latest

RUN pip install diffusers transformers scipy ftfy
RUN mkdir -p /workspace/images /workspace/scripts

COPY run_diffusion.py /workspace/scripts/
