from __future__ import annotations

from typing import List

from src.models.chord import Chord


def create_msg(header: str, msg: str) -> None:
    """
    Create a message to print to terminal.

    Parameters:
        header (str): Message header
        msg (str): Message to print
    """
    return f"=== {header} ===\n{msg}"


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
        self._scale_notes: List[str]
        self._step_sizes: List[int]
        self._chords: List[Chord]

    def __str__(self) -> str:
        """
        Print scale information.
        """
        _header = f"{self.root_note} {self.mode_name}:"
        _chords_formatted = "\n".join(f"{chord}" for chord in self._chords)
        return create_msg(_header, _chords_formatted)

    @property
    def root_note(self) -> str:
        return self._scale_notes[0]

    @property
    def mode_name(self) -> str:
        return self.MODES[self._mode - 1]

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
        scale._generate_scale_steps()
        scale._generate_scale_notes()
        scale._generate_chords()
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

    def _generate_scale_steps(self) -> None:
        """
        Generate distances between root note and each note in the scale.
        """
        _n = self._mode - 1
        _rotated_steps = self.STEP_SIZES[_n:] + self.STEP_SIZES[:_n]
        self._scale_steps = [sum(_rotated_steps[:index]) for index in range(len(_rotated_steps))]

    def _generate_scale_notes(self) -> None:
        """
        Generate scale notes from distances from root note.
        """
        _step_list = [(self._start_pos + step) % len(self.NOTES) for step in self._scale_steps]
        self._scale_notes = [self.NOTES[pos] for pos in _step_list]

    def _generate_chords(self) -> None:
        """
        Generate chords in scale.
        """
        self._chords = []
        _num_notes = len(self._scale_notes)
        for _index in range(_num_notes):
            root_note = self._scale_notes[_index % _num_notes]
            third_note = self._scale_notes[(_index + 2) % _num_notes]
            fifth_note = self._scale_notes[(_index + 4) % _num_notes]
            self._chords.append(Chord.scale_chord(index=_index, notes=[root_note, third_note, fifth_note]))

    def print_chord_progression(self, progression: List[int]) -> None:
        """
        Print a chord progression from a specified list of chord indices.

        Parameters:
            progression (List[int]): List of chord indices i.e. [1, 4, 5, 1]
        """
        _chord_strs = []
        for _index in progression:
            _chord_strs.append(str(self._chords[_index - 1]))
        print(create_msg("Chord Progression", "\n".join(_chord_strs)))
