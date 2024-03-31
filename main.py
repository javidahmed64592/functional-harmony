import argparse

from src.fh_wrapper import FHWrapper


def main(args):
    fh_wrapper = FHWrapper.initialise(config_filepath=args.config_file)

    if args.scale:
        fh_wrapper.create_scale(start_note=args.start_note, mode=args.mode)
        if args.progression:
            fh_wrapper.print_chord_progression(args.progression)
    elif args.chord:
        if args.identify_chord:
            fh_wrapper.identify_chord(args.identify_chord)
    else:
        print("Must specify -scale or -chord!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Musical Scale Tool")
    parser.add_argument("--config_file", type=str, help="Config file with music data", default="config/music_data.json")

    parser.add_argument("-scale", action="store_true", help="Use scale tools")
    parser.add_argument("--start_note", type=str, help="Root note of scale")
    parser.add_argument("--mode", type=int, help="Scale mode (1-7)")
    parser.add_argument("--progression", type=int, nargs="*", help="Chord progression i.e. 1 4 5 1")

    parser.add_argument("-chord", action="store_true", help="Extract a message from an image")
    parser.add_argument("--identify_chord", type=str, nargs="*", help="Notes in chord")

    args = parser.parse_args()
    main(args)
