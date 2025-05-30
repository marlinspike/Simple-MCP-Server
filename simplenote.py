# server.py
from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
import os
load_dotenv()

NOTES_FILE="/tmp/notes.md"
# Create an MCP server
mcp = FastMCP("SimpleNotes", "1.0.0")

def ensure_notes_file():
    """Ensure the notes file exists."""
    if not os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, 'w') as f:
            f.write("")

@mcp.tool()
def add_note(note: str) -> dict:
    """
    Add a note to the notes file.
    
    This tool appends a new note to the notes file and returns a confirmation message.
    
    Args:
        note (str): The note to add
    
    Returns:
        str: Confirmation message indicating the note was added
    """
    ensure_notes_file()
    with open(NOTES_FILE, 'a') as f:
        f.write(note + "\n")
    return {"msg": "Note added successfully."}

@mcp.tool()
def get_notes() -> dict:
    """
    Retrieve all notes from the notes file.
    
    This tool reads the notes file and returns its contents.
    
    Returns:
        list: A list of all notes in the file, or an error message if the file is empty
    """
    ensure_notes_file()
    with open(NOTES_FILE, 'r') as f:
        notes = f.readlines()
    
    if not notes:
        return {"error": "No notes found."}
    
    return {"notes": [note.strip() for note in notes]}

@mcp.tool()
def get_last_note() -> dict:
    """
    Retrieve the last note from the notes file.
    
    This tool reads the notes file and returns the last note added.
    
    Returns:
        str: The last note in the file, or an error message if the file is empty
    """
    ensure_notes_file()
    with open(NOTES_FILE, 'r') as f:
        notes = f.readlines()
    
    if not notes:
        return {"error": "No notes found."}
    
    return {"last_note": notes[-1].strip()}