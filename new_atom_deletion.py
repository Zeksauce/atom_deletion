from atom_deleter import AtomDeleter

degree_9 = (
    r"new\9.4623\SrTiO3_0_0.data",
    r"new\9.4623\SrTiO3_0_1.data",
)

degree_11 = (
    r"new\11.310\SrTiO3_0_0.data",
    r"new\11.310\SrTiO3_0_1.data",
)

degree_14 = (
    r"new\14.036\SrTiO3_0_0.data",
    r"new\14.036\SrTiO3_0_1.data",
)

degree_18 = (
    r"new\18.435\SrTiO3_0_0.data",
    r"new\18.435\SrTiO3_0_1.data",
)

degree_26 = (
    r"new\26.565\SrTiO3_0_0.data",
    r"new\26.565\SrTiO3_0_1.data",
)

# degree_45 = (
#     r"new\45\SrTiO3_0_0.data",
#     r"new\45\SrTiO3_0_1.data",
# )

run = [degree_9, degree_11, degree_14, degree_18, degree_26, ]#degree_45]
if __name__ == "__main__":
    for degree in run:
        deleter = AtomDeleter(*degree)
        deleter.main()
