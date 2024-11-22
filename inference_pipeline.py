# -*- coding: utf-8 -*-

import io, sys
import torch
from transformers import pipeline
from datasets import load_dataset

# 日本語を標準出力する
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

# モデルの設定
model_id = "kotoba-tech/kotoba-whisper-v2.0"

torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32
#torch_dtype = torch.float32

device = "cuda:0" if torch.cuda.is_available() else "cpu"
#device = "cpu"

model_kwargs = {"attn_implementation": "flash_attention_2"} if torch.cuda.is_available() else {}
#model_kwargs = {"attn_implementation": "sdpa"} if torch.cuda.is_available() else {}
#model_kwargs = {}

generate_kwargs = {"language": "japanese", "task": "transcribe"}

print(f"model_id: {model_id}")
print(f"torch_dtype: {torch_dtype}")
print(f"device: {device}")
print(f"model_kwargs: {model_kwargs}")

# モデルのロード
pipe = pipeline(
    "automatic-speech-recognition",
    model=model_id,
    torch_dtype=torch_dtype,
    device=device,
    model_kwargs=model_kwargs
)

# 推論の実行
result = pipe("sdRQT35Inp0_1min.wav", chunk_length_s=15, generate_kwargs=generate_kwargs)
print(result["text"])
