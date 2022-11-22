import logging
import typer
import os
import zipfile

from pathlib import Path, PosixPath
from tqdm import tqdm
from typing import Optional


log = logging.getLogger()


def unzip_file_with_password(rentgen: PosixPath, password: str, destination):
    with zipfile.ZipFile(rentgen, 'r') as zf:
        zf.extractall(pwd=password.encode(), path=destination)


def main(password: str, directory: Optional[str]=".", destination: Optional[str]=None):
    p = Path(directory)
    for rentgen in tqdm(list(p.glob('**/*.zip'))):
        try:
            unzip_file_with_password(rentgen, password, destination)
            os.remove(rentgen)
        except Exception:
            log.exception(f"Unzipt failed for file: {rentgen}")

def runscript():
    typer.run(main)

if __name__ == "__main__":
    runscript()
