from atom_deleter import AtomDeleter
degree_1 = (
    r"1.2.5 cutoff\1\SrTiO3_0.5_0.data",
    r"1.2.5 cutoff\1\SrTiO3_0.5_0.txt",
    1,
)

degree_2 = (
    r"1.2.5 cutoff\2\SrTiO3_0.5_0.data",
    r"1.2.5 cutoff\2\SrTiO3_0.5_0.txt",
    2,
)

degree_4 = (
    r"1.2.5 cutoff\4\SrTiO3_0.5_0.data",
    r"1.2.5 cutoff\4\SrTiO3_0.5_0.txt",
    4,
)

run = [degree_1]

if __name__ == "__main__":
    for degree in run:
        deleter = AtomDeleter(*degree)
        deleter.main()
