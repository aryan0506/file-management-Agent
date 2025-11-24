from pydantic_ai import Tool
import shutil 
import os
from logger import logger

@Tool  # this is the tool for list file in folder
def list_files(path: str = ".") -> list[str]:
    """List files in a folder."""
    try:
        logger.info(f"listing files in {path}") 
        return os.listdir(path)
    except Exception as e:
        return [f"Error: {e}"]


@Tool  # this is the folder that create file and then write content which i want 
def create_text_file(filename: str, content: str = "") -> str:
    """Create the text file with the given content"""
    try:
        logger.info(f"creating file {filename}")
        with open(filename, "w") as f:
            f.write(content)
        return f"created file: {filename}"
    except Exception as e:
        return f"Error: {e}"


@Tool # this is the tool that move file from source to destination
def move_file(src: str, dest: str) -> str:
    """Move the file from source to destination"""
    try:
        logger.info(f"moving file from {src} to {dest}")
        shutil.move(src, dest)
        return f"Moved file from {src} to {dest}"
    except Exception as e:
        return f"Error: {e}"


@Tool # this is the tool to delete the file
def delete_file(filepath: str) -> str:
    "Delete a file"
    try:
        logger.info(f"deleting file {filepath}")
        os.remove(filepath)
        return f"Deleted file: {filepath}"
    except Exception as e:
        return f"error: {e}"