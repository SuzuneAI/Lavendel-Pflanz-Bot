#!/usr/bin/env python3

import sys

# Dummy-Implementierung für Testzwecke
def pflanze_lavendel(x, z):
    print(f"Pflanze Lavendel an Position x={x}, z={z}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Pflanze Lavendel.")
    parser.add_argument("--x", type=float, required=True, help="X-Koordinate.")
    parser.add_argument("--z", type=float, required=True, help="Z-Koordinate.")
    parser.add_argument("--art", type=str, required=True, help="Art der Pflanze.")

    args = parser.parse_args()

    if args.art == "lavendel":
        pflanze_lavendel(args.x, args.z)
    else:
        print(f"Unbekannte Pflanzenart: {args.art}")
