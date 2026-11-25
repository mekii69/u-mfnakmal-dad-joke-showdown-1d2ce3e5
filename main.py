"""Dad Joke Showdown entry: write one dad joke to /output/entry.txt."""

import os

JOKE = "My doctor told me to cut back on bread, so now I only loaf around on weekends."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
