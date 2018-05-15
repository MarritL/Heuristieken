from classes.Protein import Protein
from classes.algorithm.BranchNBound import BranchNBound
from classes.algorithm.Randomizer import Randomizer
from classes.algorithm.DepthFirst import DepthFirst


def main():
    """ Implements random algorithms in order to most efficiently fold a protein """

    # TODO: Change these numbers per protein / run !!
    number = 5
    iterations = 1000
    dimensions = 2
    writeCsv = "OFF"


    #iteration: 300000(stability - 23.0)(foldpattern[
                      #                      '0', '+Y', '-Z', '-Y', '-Y', '-Z', '-Y', '-X', '-Y', '-X', '-Y', '-X', '+Z', '+X', '+Y', '+Z', '-X', '-X', '-Z', '-Z', '-Y', '-Z', '+X', '-Y', '-Y', '+Z', '-X', '+Y', '+Z', '+Y', '+Z', '-Y', '+X', '+Y', '+X', '+X'])

    # TODO: Optional parameter for branch n bound or depth first to limit the amount of iterations
    maxIterations = 1000000

    # run random algorithm
    protein = Protein(number, dimensions)
    randomAlgorithm = Randomizer(protein, writeCsv, iterations)
    randomAlgorithm.runAlgorithm()

    # # run depth first algorithm
    # protein = Protein(number, dimensions)
    # depthFirstAlgorithm = DepthFirst(protein, writeCsv)
    # depthFirstAlgorithm.runAlgorithm()
    #
    # # run branch n bound algorithm
    # protein = Protein(number, dimensions)
    # branchNBoundAlgorithm = BranchNBound(protein, writeCsv)
    # branchNBoundAlgorithm.runAlgorithm()

    # print solutions
    randomAlgorithm.printBest()
    # depthFirstAlgorithm.printBest()
    # branchNBoundAlgorithm.printBest()

if __name__ == "__main__":
    main()