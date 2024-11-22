# test-kotoba-whisper-v2.0

## Windowsでのセットアップ

### GPUの使用に必要な諸々のツールをインストール

- 参考 https://note.com/hcanadli12345/n/nb8cf59ca2596
  - NVIDIAドライバの最新版, Build Tools for Visual Studio, CUDA Toolkit, cuDNN をインストール
  - （重要！）ただしCUDA Toolkit は、PyTorch が対応しているバージョンが限られるため現在の最新対応バージョン 12.4 系をインストールしましょう
  - CUDA Toolkit の過去バージョンはここにあります
    - https://developer.nvidia.com/cuda-toolkit-archive
  - 参考: PyTorch のCUDA対応バージョン https://pytorch.org/get-started/locally/#start-locally
  - cuDNN は 9.5.1 をインストールしました
    - 参考: Support Matrix https://docs.nvidia.com/deeplearning/cudnn/latest/reference/support-matrix.html#support-matrix
-  CUDA Toolkit をインストールすると自動的にパスが通ると思いますが、もし通ってなかったら通しましょう。デフォルトでは下記のパスになるはず
  - `/c/Program Files/NVIDIA GPU Computing Toolkit/CUDA/v12.4/bin`
  - `/c/Program Files/NVIDIA GPU Computing Toolkit/CUDA/v12.4/libnvvp`

### uvのインストール

- コマンドプロンプトで以下を実行
  - `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/0.5.2/install.ps1 | iex"`
- （ぼんやはgit bashを使っているので）.bash_profile に下記を追記
  - `export PATH="${PATH}:${HOME}/.local/bin"`
- python3.12をインストール
  - `$ uv python install cpython-3.12`

### セットアップ
- `$ uv sync --group torch`
- `$ uv sync --group torch --group flash-attn`

### メモ: pyproject.toml 作成手順

- 下記を参考に pyproject.toml に torch の依存を書く。ただし dependency-groups を分ける
  - https://zenn.dev/yashikota/articles/45b4892d6acb10
- `$ uv add transformers accelerate datasets`
- `$ uv add llvmlite`
- `$ uv add numba`
- `$ uv add -U openai-whisper`
- `$ uv add soundfile numpy`
- `$ uv add hatchling editables wheel`

### 参考
- uvでflash-attentionをinstallする
  https://zenn.dev/colum2131/articles/342b7bdb20c54e

