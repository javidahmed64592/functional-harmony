import argparse

from src.fh_wrapper import FHWrapper

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Musical Scale Tool")
    parser.add_argument("--start_note", type=str, help="Root note of scale", default="C")
    parser.add_argument("--mode", type=int, help="Scale mode (1-7)", default=1)
    parser.add_argument(
        "--progression", type=int, nargs="*", help="Chord progression i.e. 1 4 5 1", default=[1, 4, 5, 1]
    )
    args = parser.parse_args()

    fh_wrapper = FHWrapper.create_scale(
        config_filepath="config/music_data.json", start_note=args.start_note, mode=args.mode
    )
    fh_wrapper.print_chord_progression(args.progression)
