from __future__ import annotations

from typing import List


class Scale:
    NOTES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    STEP_SIZES = [2, 2, 1, 2, 2, 2, 1]
    MODES = ["Ionian", "Dorian", "Phrygian", "Lydian", "Mixolydian", "Aeolian", "Locrian"]

    def __init__(self, start_pos: int, mode: int) -> None:
        self._start_pos = start_pos
        self._mode = mode
        self._scale_notes: List[str]
        self._step_sizes: List[int]

    def __str__(self) -> str:
        _header = f"{self.root_note} {self.mode_name}:"
        return f"{_header}\n{', '.join(self._scale_notes)}"

    @property
    def root_note(self) -> str:
        return self._scale_notes[0]

    @property
    def mode_name(self) -> str:
        return self.MODES[self._mode - 1]

    def _generate_scale_steps(self) -> None:
        _n = self._mode - 1
        _rotated_steps = self.STEP_SIZES[_n:] + self.STEP_SIZES[:_n]
        self._scale_steps = [sum(_rotated_steps[:index]) for index in range(len(_rotated_steps))]

    def _generate_scale_notes(self) -> None:
        _step_list = [(self._start_pos + step) % len(self.NOTES) for step in self._scale_steps]
        self._scale_notes = [self.NOTES[pos] for pos in _step_list]

    @classmethod
    def generate_scale(cls, start_pos: int, mode: int) -> Scale:
        _len_notes = len(cls.NOTES)
        if start_pos < 0 or start_pos > _len_notes - 1:
            raise ValueError(f"Start position must be between 0 and {_len_notes-1}!")

        if mode < 1 or mode > 7:
            raise ValueError("Mode must be between 1 and 7!")

        _scale = cls(start_pos, mode)
        _scale._generate_scale_steps()
        _scale._generate_scale_notes()
        return _scale

    @classmethod
    def from_note(cls, start_note: str, mode: int) -> Scale:
        if start_note not in cls.NOTES:
            raise ValueError("Invalid starting note specified!")

        _start_pos = cls.NOTES.index(start_note)
        _scale = cls.generate_scale(_start_pos, mode)
        return _scale
