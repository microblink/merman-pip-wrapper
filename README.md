# Merman Wrapper

This project exposes wasm-compiled `merman` tool

## Build instructions

Build the `mearman.wasm` file ( This is the tool from https://github.com/microblink/merman )

Copy the `merman.wasm` file to `merman_wrapper/wasm_files/merman.wasm`

Build the pip package:

```bash
python -m build
```