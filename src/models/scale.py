from __future__ import annotations

from typing import List

from src.models.chord import Chord


class Scale:
    NOTES: List[str]
    STEP_SIZES: List[int]
    MODES: List[str]

    def __init__(self, start_pos: int, mode: int) -> None:
        """
        Initialise Scale with start position and mode.

        Parameters:
            start_pos (int): Position of root note 0-11
            mode (int): Scale mode to use 1-7
        """
        self._start_pos = start_pos
        self._mode = mode
        self._scale_notes: List[str] = []
        self._scale_steps: List[int] = []
        self._chords: List[Chord] = []

    @property
    def scale_info(self) -> str:
        return f"{self.root_note} {self.mode_name}"

    @property
    def chord_info(self) -> str:
        return "\n".join(f"{chord}" for chord in self.chords)

    @property
    def root_note(self) -> str:
        return self.notes[0]

    @property
    def mode_name(self) -> str:
        return self.MODES[self._mode - 1]

    @property
    def notes(self) -> List[str]:
        if not self._scale_notes:
            _step_list = [(self._start_pos + step) % len(self.NOTES) for step in self.scale_steps]
            self._scale_notes = [self.NOTES[pos] for pos in _step_list]
        return self._scale_notes

    @property
    def scale_steps(self) -> List[int]:
        if not self._scale_steps:
            _n = self._mode - 1
            _rotated_steps = self.STEP_SIZES[_n:] + self.STEP_SIZES[:_n]
            self._scale_steps = [sum(_rotated_steps[:index]) for index in range(len(_rotated_steps))]
        return self._scale_steps

    @property
    def chords(self) -> List[Chord]:
        if not self._chords:
            _num_notes = len(self.notes)
            for _index in range(_num_notes):
                root_note = self.notes[_index % _num_notes]
                third_note = self.notes[(_index + 2) % _num_notes]
                fifth_note = self.notes[(_index + 4) % _num_notes]
                self._chords.append(Chord.scale_chord(index=_index, notes=[root_note, third_note, fifth_note]))
        return self._chords

    @classmethod
    def generate_scale(cls, start_pos: int, mode: int) -> Scale:
        """
        Generate Scale from start position and mode.

        Parameters:
            start_pos (int): Position of root note 0-11
            mode (int): Scale mode to use 1-7

        Returns:
            scale (Scale): Scale with notes in key
        """
        _len_notes = len(cls.NOTES)
        if start_pos < 0 or start_pos > _len_notes - 1:
            raise ValueError(f"Start position must be between 0 and {_len_notes-1}!")

        if mode < 1 or mode > 7:
            raise ValueError("Mode must be between 1 and 7!")

        scale = cls(start_pos, mode)
        return scale

    @classmethod
    def from_note(cls, start_note: str, mode: int) -> Scale:
        """
        Generate Scale from start position and mode.

        Parameters:
            start_note (str): Root note of scale
            mode (int): Scale mode to use 1-7

        Returns:
            scale (Scale): Scale with notes in key
        """
        if start_note not in cls.NOTES:
            raise ValueError("Invalid starting note specified!")

        _start_pos = cls.NOTES.index(start_note)
        scale = cls.generate_scale(_start_pos, mode)
        return scale

    def create_chord_progression(self, progression: List[int]) -> str:
        """
        Create a chord progression from a specified list of chord indices.

        Parameters:
            progression (List[int]): List of chord indices i.e. [1, 4, 5, 1]

        Returns:
            chord_progression (str): Chord progression using scale chords
        """
        _chord_strs = []
        for _index in progression:
            _chord_strs.append(str(self.chords[_index - 1]))
        chord_progression = "\n".join(_chord_strs)
        return chord_progression
