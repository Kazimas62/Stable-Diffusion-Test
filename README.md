# Stable-Diffusion-Test
Stable Diffusionを試す

```sh
docker-compose build
docker-compose up -d
docker exec -it stable_diffusion bash

python /workspace/scripts/run_diffusion.py "テキスト"
```
