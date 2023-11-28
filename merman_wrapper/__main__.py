from .merman_wrapper import run

import argparse


def main():
    parser = argparse.ArgumentParser(
        description="Run wasm-wrpapped merman"
    )
    parser.add_argument("-o", "--output")
    parser.add_argument("input")

    args = parser.parse_args()

    run(args.input, args.output)


if __name__ == "__main__":
    main()
