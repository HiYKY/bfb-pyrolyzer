import argparse
import importlib
import logging
import multiprocessing
import pathlib

from solver import Solver
from plotter import Plotter
from printer import print_report


def run_solver(path, ncase=None):
    """
    Perform calculations for each case.
    """

    if ncase is None:
        logging.info('Solve for case parameters.')
    else:
        logging.info(f'Solve for case {ncase} parameters.')

    spec = importlib.util.spec_from_file_location('params', path / 'params.py')
    params = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(params)

    solver = Solver(params, path)
    solver.solve_params()
    solver.solve_temps()
    solver.save_results()
    print_report(params, solver, path)

    plotter = Plotter(solver, path)
    plotter.plot_geldart()
    plotter.plot_intra_particle_heat_cond()
    plotter.plot_umb_umf_ut_params()
    plotter.plot_tdevol_temps()
    plotter.plot_umb_umf_temps()
    plotter.plot_ut_temps()
    plotter.plot_velocity_temps()


def main():
    """
    Main entry point for program.
    """

    # Command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('project', help='project folder')
    parser.add_argument('-r', '--run', action='store_true', help='run parameters in serial')
    parser.add_argument('-mp', '--mprun', action='store_true', help='run parameters in parallel')
    parser.add_argument('-c', '--clean', action='store_true', help='remove generated files')
    args = parser.parse_args()

    # Setup logging
    logging.basicConfig(format='%(message)s', level=logging.INFO)
    logging.info('Start BFB calculations')

    # Path to project folder which contains parameters for each case
    project_path = pathlib.Path(args.project)
    case_paths = [p for p in project_path.iterdir() if p.is_dir()]

    # Solve using parameters for each case (serial)
    if args.run:
        for n, path in enumerate(case_paths):
            run_solver(path, ncase=n + 1)

    # Solve using parameters for each case (parallel)
    if args.mprun:
        with multiprocessing.Pool() as pool:
            pool.map(run_solver, case_paths)

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
    main()
