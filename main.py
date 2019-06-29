"""
Main driver for BFB model simulation of a biomass pyrolysis reactor.
"""

import argparse
import importlib
import pathlib

from bfblib import run_params
from bfblib import run_temps


def main(args):

    # Path to project folder is same as parameters directory
    name = args.infile.split('/')[0]
    path = pathlib.Path.cwd() / name

    # Get parameters from a Python module
    infile = args.infile.replace('/', '.')[:-3]
    params = importlib.import_module(infile)

    # Run simulation for parameters only
    if args.params:
        run_params(params)

    # Run simulation for parameters only and save figures to path
    if args.params and args.figs:
        run_params(params, path)

    # Run a simulation for temperatures case and save figures to path
    if args.temps:
        run_temps(params, path)

    # Cleanup project directory
    if args.clean:
        for file in path.iterdir():
            if file.suffix == '.pdf':
                file.unlink()
        print(f'Cleaned up files in the `{name}` folder.')


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('infile', help='path to parameters module file')
    parser.add_argument('-p', '--params', action='store_true', help='run parameters only')
    parser.add_argument('-t', '--temps', action='store_true', help='run temperatures case')
    parser.add_argument('-f', '--figs', action='store_true', help='build and save plot figures')
    parser.add_argument('-c', '--clean', action='store_true', help='remove results folder')
    args = parser.parse_args()

    main(args)
