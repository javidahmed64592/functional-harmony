class TestChord:
    def test_given_chords_when_categorising_type_then_check_chord_has_correct_type(self, chord_class):
        test_chords = [["E", "G#", "B"], ["A", "C", "E"], ["D", "F", "G#"]]
        expected_chord_types = ["Major", "Minor", "Diminished"]

        zipped_list = zip(test_chords, expected_chord_types)
        for chord, expected_type in zipped_list:
            test_chord = chord_class(notes=chord)
            assert test_chord.type == expected_type

    def test_given_scale_chords_when_creating_index_then_check_chord_has_correct_index(self, chord_class):
        test_chords = [["E", "G#", "B"], ["A", "C", "E"], ["D", "F", "G#"]]
        test_indices = [1, 3, 5]
        expected_indices = ["II", "iv", "vi°"]

        zipped_list = zip(test_chords, test_indices, expected_indices)
        for chord, index, expected_index in zipped_list:
            test_chord = chord_class.scale_chord(index=index, notes=chord)
            assert test_chord.chord_index == expected_index

    def test_given_scale_chords_when_creating_label_then_check_chord_has_correct_labels(self, chord_class):
        test_chords = [["E", "G#", "B"], ["A", "C", "E"], ["D", "F", "G#"]]
        test_indices = [1, 4, 5]
        expected_labels = ["Supertonic", "Dominant", "Submediant"]
        expected__secondary_labels = ["Predominant", "Dominant", "Tonic"]

        zipped_list = zip(test_chords, test_indices, expected_labels, expected__secondary_labels)
        for chord, index, expected_label, expected_secondary_label in zipped_list:
            test_chord = chord_class.scale_chord(index=index, notes=chord)
            assert test_chord.label == expected_label
            assert test_chord.secondary_label == expected_secondary_label
