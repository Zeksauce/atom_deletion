"Module to run all the deletions on all the files"
from lammps_init_1 import AtomDeleter

degree_1 = (
    r"1.2.5 cutoff\1\SrTiO3_0.5_0.data",
    r"1.2.5 cutoff\1\SrTiO3_0.5_0.txt",
    [
        (195.3, 1.9897, 1.9552, 0.25952),
        (473.5, 451.7, 1.96, 1.76),
        (420.162, 226.86, 1.96, 0.259),
    ],
)

degree_2 = (
    r"1.2.5 cutoff\2\SrTiO3_0.5_0.data",
    r"1.2.5 cutoff\2\SrTiO3_0.5_0.txt",
    [
        (96.68, 2.0, 1.94, 0),
        (211.1, 114.40, 1.943, 0),
        (323.55, 226.90, 1.98, 0),
        (379.0, 339.34, 1.97, 0),
    ],
)

run = [degree_1,degree_2,]

if __name__ == "__main__":
    for degree in run:
        deleter = AtomDeleter(*degree)
        deleter.main()
