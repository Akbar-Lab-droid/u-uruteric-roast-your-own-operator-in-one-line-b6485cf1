"""Entry program for the u-uruteric-roast-your-own-operator-in-one-line-b6485cf1 make.fun bounty.

Copies the committed entry.txt into the harness output directory.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


# Entry point: copy the committed text into the output directory.
def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(os.path.join(HERE, "entry.txt"),
                    os.path.join(out_dir, "entry.txt"))


if __name__ == "__main__":
    main()
