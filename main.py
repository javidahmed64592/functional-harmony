from src.scale import Scale

if __name__ == "__main__":
    scale = Scale.from_note(start_note="E", mode=1)
    progression = [1, 4, 5, 1]
    scale.print_chord_progression(progression=progression)
