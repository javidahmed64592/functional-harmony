from __future__ import annotations

from typing import Dict, List


class Chord:
    NOTES: List[str]
    INDICES: List[str]
    LABELS: List[str]
    SECONDARY_LABELS: List[str]
    CHORD_TYPES: Dict[str, List[int]]

    def __init__(self, notes: List[str]) -> None:
        """
        Initialise Chord with index, chord notes and chord type.

        Parameters:
            notes (List[str]): List of notes in chord
        """
        self._notes = notes
        self._index: int

    def __str__(self) -> str:
        _notes_str = " ".join(self._notes)
        _chord_str = f"({self._notes[0]:<1} {self.type:<1})"
        _label_str = f"{self.label:<12} ({self.secondary_label})  \t -> {self.next_chord:>1}"
        return f"{self.chord_index:<4}: {_notes_str:<8} {_chord_str} \t- {_label_str}"

    @property
    def type(self) -> str:
        _n = self.NOTES.index(self._notes[0])
        _notes = self.NOTES[_n:] + self.NOTES[:_n]
        _note_pos = [_notes.index(note) for note in self._notes]
        for chord_type, chord_profile in self.CHORD_TYPES.items():
            if _note_pos == chord_profile:
                return chord_type
        return "Unknown"

    @property
    def chord_index(self) -> str:
        _chord_index = ""
        if self.type == "Major":
            _chord_index = self.INDICES[self._index]
        elif self.type == "Minor":
            _chord_index = self.INDICES[self._index].lower()
        elif self.type == "Diminished":
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
        _next_chord = ""
        if self.secondary_label == "Tonic":
            _next_chord = "Tonic | Dominant | Predominant"
        elif self.secondary_label == "Predominant":
            _next_chord = "Dominant | Tonic | Predominant"
        elif self.secondary_label == "Dominant":
            _next_chord = "Tonic"
        return _next_chord

    @classmethod
    def scale_chord(cls, index: int, notes: List[str]) -> Chord:
        """
        Create a chord with position in scale.

        Parameters:
            index (int): Position in scale
            notes (List[str]): Notes in chord

        Returns:
            chord (Chord): Chord with assigned index
        """
        chord = cls(notes)
        chord._index = index
        return chord
