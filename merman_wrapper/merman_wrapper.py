from wasmtime import Store, Module, WasiConfig, Linker

from typing import Optional
from os import path


def run(in_path: str, out_path: Optional[str] = None):

    input_path = path.abspath(in_path)
    input_dir = path.dirname(input_path)

    if out_path is None:
        output_path = None
        output_dir = None
    else:
        output_path = path.abspath(out_path)
        output_dir = path.dirname(output_path)

    wasi_config = WasiConfig()
    wasi_config.preopen_dir(input_dir, input_dir)
    if output_dir is not None:
        wasi_config.preopen_dir(output_dir, output_dir)
    args = ["exe"]
    if output_path is not None:
        args.append("-o")
        args.append(output_path)
    args.append(input_path)

    wasi_config.argv = args

    wasi_config.inherit_stdout()
    wasi_config.inherit_stderr()

    store = Store()

    store.set_wasi(wasi_config)

    basepath = path.dirname(__file__)
    wasm_file_path = path.abspath(path.join(basepath, "wasm_files", "merman.wasm"))

    with open(wasm_file_path, "rb") as f:
        module_content = f.read()

    module = Module(store.engine, module_content)

    linker = Linker(engine=store.engine)

    linker.define_wasi()
    linker.allow_shadowing = True

    instance = linker.instantiate(store, module)

    main = instance.exports(store)["_start"]

    # Run main
    main(store)
