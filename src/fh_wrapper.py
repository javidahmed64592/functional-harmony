from __future__ import annotations

from typing import Any, Dict, List

from src.helpers.general import create_msg, load_config
from src.models.chord import Chord
from src.models.scale import Scale


class FHWrapper:
    def __init__(self, config_filepath: str) -> None:
        """
        Initialise FHWrapper with config using filepath.

        Parameters:
            config_filepath (str): Path to config file
        """
        self._config_filepath = config_filepath
        self._config: Dict[str, Any] = {}
        self._chord: Chord
        self._scale: Scale

    @classmethod
    def initialise(cls, config_filepath: str) -> FHWrapper:
        """
        Create FHWrapper object and set Chord and Scale attributes.

        Parameters:
            config_filepath (str): Path to config file

        Returns:
            wrapper (FHWrapper): Wrapper with attributes set
        """
        wrapper = cls(config_filepath)
        wrapper._initialise_chord()
        wrapper._initialise_scale()
        return wrapper

    @property
    def config(self):
        if not self._config:
            self._config = self._load_config(self._config_filepath)
        return self._config

    def _load_config(self, config_filepath: str) -> Dict[str, Any]:
        """
        Load config from filepath.

        Parameters:
            config_filepath (str): Path to config file

        Returns:
            config (Dict[str, Any]): Config file
        """
        config = load_config(config_filepath)
        return config

    def _initialise_chord(self) -> None:
        """
        Set Chord attributes.
        """
        Chord.NOTES = self.config["notes"]
        Chord.INDICES = self.config["chord_indices"]
        Chord.LABELS = self.config["chord_labels"]
        Chord.SECONDARY_LABELS = self.config["chord_secondary_labels"]
        Chord.CHORD_TYPES = self.config["chord_types"]

    def _initialise_scale(self) -> None:
        """
        Set Scale attributes.
        """
        Scale.NOTES = self.config["notes"]
        Scale.STEP_SIZES = self.config["scale_steps"]
        Scale.MODES = self.config["scale_modes"]

    def create_scale(self, start_note: str, mode: int) -> None:
        """
        Create a scale using a root note and scale mode.

        Parameters:
            start_note (str): Root note of scale
            mode (int): Scale mode
        """
        self._scale = Scale.from_note(start_note=start_note, mode=mode)
        print(create_msg(header="Scale Info", msg=f"{self._scale.scale_info} - {self._scale.note_info}"))
        print(create_msg(header="Scale Chords", msg=self._scale.chord_info))

    def print_chord_progression(self, progression: List[int]) -> None:
        """
        Print a chord progression from a specified list of chord indices.

        Parameters:
            progression (List[int]): List of chord indices i.e. [1, 4, 5, 1]
        """
        print(create_msg(header="Chord Progression", msg=self._scale.create_chord_progression(progression=progression)))

    def identify_chord(self, notes: List[str]) -> None:
        """
        Identify a chord from a set of notes.

        Parameters:
            notes (List[str]): List of notes in chord
        """
        self._chord = Chord(notes)
        print(
            create_msg(header="Chord Identification", msg=f"Chord: {self._chord.notes_str}\nType: {self._chord.type}")
        )
