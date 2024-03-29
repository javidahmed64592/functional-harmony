from __future__ import annotations

from typing import List


class Chord:
    INDICES = ["I", "II", "III", "IV", "V", "VI", "VII"]
    LABELS = ["Tonic", "Supertonic", "Mediant", "Subdominant", "Dominant", "Submediant", "Leading Tone"]
    SECONDARY_LABELS = ["Tonic", "Predominant", "Tonic", "Predominant", "Dominant", "Tonic", "Dominant"]

    def __init__(self, index: int, notes: List[str], chord_type: str) -> None:
        """
        Initialise Chord with index, chord notes and chord type.

        Parameters:
            index (int): Position of chord
            notes (List[str]): List of notes in chord
            chord_type (str): Chord type ['Major', 'Minor', 'Diminished']
        """
        self._index = index
        self._notes = notes
        self._type = chord_type

    def __str__(self) -> str:
        _notes_str = " ".join(self._notes)
        return f"{self.chord_index:<4}: {_notes_str:<8} ({self._notes[0]:<1} {self._type:<1}) \t- {self.label:<12} -> {self.next_chord}"

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

    @property
    def label(self) -> str:
        return self.LABELS[self._index]

    @property
    def secondary_label(self) -> str:
        return self.SECONDARY_LABELS[self._index]

    @property
    def next_chord(self) -> str:
        if self.secondary_label == "Tonic":
            return "Can move anywhere"
        elif self.secondary_label == "Predominant":
            return "Resolves into dominant, tonic or predominant"
        elif self.secondary_label == "Dominant":
            return "Resolves into tonic"
