from typing import List
from pydantic import BaseModel, Field, field_validator
import re

class ComposerOutput(BaseModel):
    """
    Pydantic schema for the output of a Composer Agent.

    Attributes:
        tempo (int): Beats per minute, must be greater than 0.
        key (str): Musical key, e.g., "C", "G#m", "Am". Must match a regex pattern.
        scale (str): Scale type, e.g., "major", "minor", "dorian".
        chord_progression (List[str]): List of at least 4 chord strings, e.g., "Cmaj7", "Am7".
        melody_notes (List[str]): List of at least 8 melody notes in simplified LilyPond format,
            e.g., "C4q", "D4e", "G#4h".
    """

    tempo: int = Field(..., gt=0, description="Beats per minute, must be greater than 0")
    key: str = Field(..., description='Musical key, e.g., "C", "G#m", "Am"')
    scale: str = Field(..., description='Scale type, e.g., "major", "minor", "dorian"')
    chord_progression: List[str] = Field(..., min_items=4, description="Chord progression with at least 4 chords")
    melody_notes: List[str] = Field(..., min_items=8, description="Melody notes with at least 8 notes in simplified LilyPond format")

    @field_validator('key')
    def validate_key(cls, v: str) -> str:
        # Accept keys like C, Cm, C#, C#m, Am, G#m, etc.
        pattern = r"^[A-G](#|b)?m?$"
        if not re.match(pattern, v):
            raise ValueError('Key must be a valid musical key like "C", "G#m", "Am"')
        return v

    @field_validator('chord_progression', mode='after')
    def non_empty_chords(cls, chords: List[str]) -> List[str]:
        for chord in chords:
            chord_stripped = chord.strip()
            if not chord_stripped:
                raise ValueError('Chord strings must be non-empty and not just whitespace')
        return chords

    @field_validator('melody_notes', mode='after')
    def non_empty_melody_notes(cls, notes: List[str]) -> List[str]:
        for note in notes:
            note_stripped = note.strip()
            if not note_stripped:
                raise ValueError('Melody note strings must be non-empty and not just whitespace')
        return notes
