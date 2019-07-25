"""
Main driver for BFB model simulation of a biomass pyrolysis reactor.
"""
import argparse
import importlib
import logging
import pathlib

from bfblib.solver import Solver
from bfblib.plotter import Plotter
from bfblib.printer import print_report


def main(args):

    logging.basicConfig(format='%(message)s', level=logging.INFO)
    logging.info('Start BFB calculations')

    # Path to project folder which contains parameters for each case
    project_path = pathlib.Path(args.infile)
    case_paths = [p for p in project_path.iterdir() if p.is_dir()]

    # Solve using parameters for each case
    if args.run:

        for path in case_paths:
            params_str = str(path / 'params').replace('/', '.')
            params = importlib.import_module(params_str)

            solver = Solver(params, path)
            solver.solve_params()
            solver.solve_temps()
            solver.save_results()
            print_report(params, solver, path)

        plotter = Plotter(project_path, case_paths)
        plotter.plot_geldart()
        plotter.plot_tdevol_temps()
        plotter.plot_umf_bed()
        plotter.plot_ut_temps()
        plotter.plot_intra_particle_heat_cond()

    # Clean up generated files from previous runs
    if args.clean:
        logging.info('Clean up generated files from previous runs')

        for path in case_paths:
            for file in path.iterdir():
                if not file.is_dir() and not file.suffix == '.py':
                    file.unlink()

        for file in project_path.iterdir():
            if file.suffix == '.pdf':
                file.unlink()

    logging.info('End')


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('infile', help='path to project folder')
    parser.add_argument('-r', '--run', action='store_true', help='run parameters')
    parser.add_argument('-c', '--clean', action='store_true', help='remove generated files')
    args = parser.parse_args()

    main(args)
