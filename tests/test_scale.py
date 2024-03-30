from src.scale import Scale


class TestScale:
    def test_given_root_notes_when_creating_scale_then_check_scale_has_correct_root_note(self):
        test_root_notes = ["C", "D", "F", "F#", "A", "B"]
        for root_note in test_root_notes:
            test_scale = Scale.from_note(start_note=root_note, mode=1)
            assert test_scale.root_note == root_note

    def test_given_scale_modes_when_creating_scale_then_check_scale_has_correct_mode(self):
        test_scale_modes = [1, 2, 4, 6, 7]
        expected_modes = ["Ionian", "Dorian", "Lydian", "Aeolian", "Locrian"]
        for scale_mode, expected_mode in zip(test_scale_modes, expected_modes):
            test_scale = Scale.from_note(start_note="C", mode=scale_mode)
            assert test_scale.mode_name == expected_mode

    def test_given_key_when_creating_scale_chords_then_check_chords_have_correct_type(self):
        test_scale = Scale.from_note(start_note="E", mode=5)
        expected_chord_types = ["Major", "Minor", "Diminished", "Major", "Minor", "Minor", "Major"]
        for chord, expected_chord in zip(test_scale._chords, expected_chord_types):
            assert chord.type == expected_chord
