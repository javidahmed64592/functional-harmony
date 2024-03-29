import argparse

from src.scale import Scale

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Musical Scale Tool")
    parser.add_argument("--start_note", type=str, help="Root note of scale", default="C")
    parser.add_argument("--mode", type=int, help="Scale mode (1-7)", default=1)
    parser.add_argument(
        "--progression", type=int, nargs="*", help="Chord progression i.e. 1 4 5 1", default=[1, 4, 5, 1]
    )
    args = parser.parse_args()

    scale = Scale.from_note(start_note=args.start_note, mode=args.mode)
    scale.print_chord_progression(progression=args.progression)
