from __future__ import annotations

from typing import List


class Chord:
    INDICES = ["I", "II", "III", "IV", "V", "VI", "VII"]

    def __init__(self, index: int, notes: List[str], chord_type: str) -> None:
        self._index = index
        self._notes = notes
        self._type = chord_type

    def __str__(self) -> str:
        _notes_str = " ".join(self._notes)
        return f"{self.chord_index}: \t{_notes_str}  \t({self._notes[0]} {self._type})"

    @property
    def chord_index(self) -> str:
        _chord_index = ""
        if self._type == "Major":
            _chord_index = self.INDICES[self._index]
        elif self._type == "Minor":
            _chord_index = self.INDICES[self._index].lower()
        elif self._type == "Diminished":
            _chord_index = self.INDICES[self._index].lower() + "°"
        return _chord_index
