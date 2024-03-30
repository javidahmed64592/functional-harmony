class TestScale:
    def test_given_root_notes_when_creating_scale_then_check_scale_has_correct_root_note(self, scale_class):
        test_root_notes = ["C", "D", "F", "F#", "A", "B"]
        for root_note in test_root_notes:
            test_scale = scale_class.from_note(start_note=root_note, mode=1)
            assert test_scale.root_note == root_note

    def test_given_scale_modes_when_creating_scale_then_check_scale_has_correct_mode(self, scale_class):
        test_scale_modes = [1, 2, 4, 6, 7]
        expected_modes = ["Ionian", "Dorian", "Lydian", "Aeolian", "Locrian"]

        zipped_list = zip(test_scale_modes, expected_modes)
        for scale_mode, expected_mode in zipped_list:
            test_scale = scale_class.from_note(start_note="C", mode=scale_mode)
            assert test_scale.mode_name == expected_mode

    def test_given_keys_when_creating_scales_then_check_scales_have_correct_notes(self, scale_class):
        test_root_notes = ["C", "E", "G#", "A", "B"]
        test_scale_modes = [1, 2, 4, 6, 7]

        expected_scale_notes = [
            ["C", "D", "E", "F", "G", "A", "B"],
            ["E", "F#", "G", "A", "B", "C#", "D"],
            ["G#", "A#", "C", "D", "D#", "F", "G"],
            ["A", "B", "C", "D", "E", "F", "G"],
            ["B", "C", "D", "E", "F", "G", "A"],
        ]

        zipped_list = zip(test_root_notes, test_scale_modes, expected_scale_notes)
        for root_note, mode, expected_notes in zipped_list:
            test_scale = scale_class.from_note(start_note=root_note, mode=mode)
            assert test_scale.notes == expected_notes

    def test_given_key_when_creating_scale_chords_then_check_chords_have_correct_type(self, scale_class, chord_class):
        test_scale = scale_class.from_note(start_note="E", mode=5)
        expected_chord_types = ["Major", "Minor", "Diminished", "Major", "Minor", "Minor", "Major"]

        zipped_list = zip(test_scale._chords, expected_chord_types)
        for chord, expected_type in zipped_list:
            assert chord.type == expected_type

    def test_given_key_when_creating_scale_chords_then_check_chords_have_correct_index(self, scale_class, chord_class):
        test_scale = scale_class.from_note(start_note="E", mode=5)
        expected_chord_index = ["I", "ii", "iii°", "IV", "v", "vi", "VII"]

        zipped_list = zip(test_scale._chords, expected_chord_index)
        for chord, expected_index in zipped_list:
            assert chord.chord_index == expected_index

    def test_given_key_when_creating_scale_chords_then_check_chords_have_correct_labels(self, scale_class, chord_class):
        test_scale = scale_class.from_note(start_note="E", mode=3)
        expected_chord_label = [
            "Tonic",
            "Supertonic",
            "Mediant",
            "Subdominant",
            "Dominant",
            "Submediant",
            "Leading Tone",
        ]
        expected_chord_secondary_label = [
            "Tonic",
            "Predominant",
            "Tonic",
            "Predominant",
            "Dominant",
            "Tonic",
            "Dominant",
        ]

        zipped_list = zip(test_scale._chords, expected_chord_label, expected_chord_secondary_label)
        for chord, expected_label, expected_secondary_label in zipped_list:
            assert chord.label == expected_label
            assert chord.secondary_label == expected_secondary_label
