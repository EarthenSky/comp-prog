def readint(filepath: str):
    with open(filepath, "r") as f:
        return int(f.readline())