#!/usr/bin/env python3

from huggingface_hub import snapshot_download
from pathlib import Path

models = Path('models')
sd1_4 = models / 'sd1_4'
sd1_4.mkdir(exist_ok=True, parents=True)
snapshot_download("CompVis/stable-diffusion-v1-4", repo_type="model", local_dir=sd1_4, ignore_patterns=["*.safetensors"])