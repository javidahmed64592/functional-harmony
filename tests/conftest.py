from typing import Any, Dict

import pytest

from src.models.chord import Chord
from src.models.scale import Scale


@pytest.fixture
def config() -> Dict[str, Any]:
    return {
        "notes": ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"],
        "scale_steps": [2, 2, 1, 2, 2, 2, 1],
        "scale_modes": ["Ionian", "Dorian", "Phrygian", "Lydian", "Mixolydian", "Aeolian", "Locrian"],
        "chord_indices": ["I", "II", "III", "IV", "V", "VI", "VII"],
        "chord_labels": ["Tonic", "Supertonic", "Mediant", "Subdominant", "Dominant", "Submediant", "Leading Tone"],
        "chord_secondary_labels": ["Tonic", "Predominant", "Tonic", "Predominant", "Dominant", "Tonic", "Dominant"],
        "chord_types": {"Major": [0, 4, 7], "Minor": [0, 3, 7], "Diminished": [0, 3, 6]},
    }


@pytest.fixture
def chord_class(config) -> Chord:
    chord = Chord
    chord.NOTES = config["notes"]
    chord.INDICES = config["chord_indices"]
    chord.LABELS = config["chord_labels"]
    chord.SECONDARY_LABELS = config["chord_secondary_labels"]
    chord.CHORD_TYPES = config["chord_types"]
    return chord


@pytest.fixture
def scale_class(config) -> Scale:
    scale = Scale
    scale.NOTES = config["notes"]
    scale.STEP_SIZES = config["scale_steps"]
    scale.MODES = config["scale_modes"]
    return scale
