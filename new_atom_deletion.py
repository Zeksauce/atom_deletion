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

degree_6 = (
    r"1.2.5 cutoff\6\SrTiO3_0.5_0.data",
    r"1.2.5 cutoff\6\SrTiO3_0.5_0.txt",
    6,
)

degree_10 = (
    r"1.2.5 cutoff\10\SrTiO3_0.5_0.data",
    r"1.2.5 cutoff\10\SrTiO3_0.5_0.txt",
    10,
)

degree_22 = (
    r"1.2.5 cutoff\22\SrTiO3_0.5_0.data",
    r"1.2.5 cutoff\22\SrTiO3_0.5_0.txt",
    22,
)

degree_36 = (
    r"1.2.5 cutoff\36\SrTiO3_0.5_0.data",
    r"1.2.5 cutoff\36\SrTiO3_0.5_0.txt",
    45,
)

degree_45 = (
    r"1.2.5 cutoff\45\SrTiO3_0.5_0.data",
    r"1.2.5 cutoff\45\SrTiO3_0.5_0.txt",
    45,
)

run = [degree_1, degree_2, degree_4, degree_6, degree_10, degree_22, degree_36, degree_45]
#run = [degree_1]
if __name__ == "__main__":
    for degree in run:
        deleter = AtomDeleter(*degree)
        deleter.main()
