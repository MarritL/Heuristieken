# Protein folding
Proteins are strings of aminoacids. (Dis)fuctioning of proteins is known to be determined by the dimensional folding structure. In a simplified model, the aminoacids can be represented by H (hydrophobic) and P (polar). In this model the stability of a folding structure is measured by the amount of H-bonds present in the structure. An H-bond is defined as two Hs that are adjecent to each other in the structure, while not in the aminoacid-sequence. Each H-bonds has a score of -1. A more advanced protein can also have aminoacid represented by a C (cysteine). These kan form C-bonds with a stability score of -5 and C-H bonds with a stability score of -1. The lower the stability score of the total structure, the more stable the protein is and the better the folding structure is (see figure).

![best random folding pattern of protein1](https://github.com/Jara555/Proteins/blob/master/doc/randomizer_protein7.png)

This program implements algorithms, all with the aim to find the best possible folding structure for a benchmark of proteins as listed below. Proteins can be fold in 2D as well as 3D. Furthermore, besides these benchmark proteins, the program can be run for any custum created protein.
1) HHPHHHPH
2) HHPHHHPHPHHHPH 
3) HPHPPHHPHPPHPHHPPHPH 
4) PPPHHPPHHPPPPPHHHHHHHPPHHPPPPHHPPHPP 
5) HHPHPHPHPHHHHPHPPPHPPPHPPPPHPPPHPPPHPHHHHPHPHPHPHH 
6) PPCHHPPCHPPPPCHHHHCHHPPHHPPPPHHPPHPP
7) CPPCHPPCHPPCPPHHHHHHCCPCHPPCPCHPPHPC
8) HCPHPCPHPCHCHPHPPPHPPPHPPPPHPCPHPPPHPHHHCCHCHCHCHH
9) HCPHPHPHCHHHHPCCPPHPPPHPPPPCPPPHPPPHPHHHHCHPHPHPHH

## Getting Started

### Prerequisites
This code is written in [Python3.6.3](https://www.python.org/downloads/). 
Furthermore the code uses the following packages: matpotlib. This is easy to install using the following instruction:

```
pip3 install matplotlib
```

### Structure

This code uses three classes: AminoAcid, Protein and Algorithm. These can together with their corresponding methods be found in the map classes. The map algorithms contains al algorithm subclasses of the superclass Algorithm. All benchmark proteins can be found in the map data and the results will be saved as a .csv or .log files in the results map. The main script for running the program can be found in proteins.py.

### Running

To run the program with the standardconfigurations use the following instructions:

```
python proteins.py -a <algorithm> -p <protein> -d <dimensions> -i <iterations> -c <csv>

```

        :argument -a <algorithm> : First letters of algorithm names
                                        R = Randomizer
                                        HC = HillClimber
                                        SA = SimulatedAnnealing
                                        DF = DepthFirst
                                        BB = BranchNBound
        :argument -p <protein> : Protein to be fold
                                 Can be an integer reflecting 1 of the benchmark proteins 
                                 Or a custom string reflecting a list of amino acids
                                        int options = 1/2/3/ ... 9
                                        str options  = H/P/C
        :argument -d <dimensions> : dimensions to be fold in
                                        2 = 2D
                                        3 = 3D (default)
        :argument -i <iterations> : Maximal iterations to be run 
                                    Required for R and HC, optional for DF and BB
                                        default = None 
        :argument -c <csv> : Write solutions to .csv file
                                        ON = write
                                        OFF = not write (default)

### Experiment

After each run a .log file is created containing the running info of the algorithm for the specific protein. To analyze the log results the program experiment.py can be used, found in the map /experiment. The experiment program will analyze the running info of all algorithms for which .log files exist.  

To run the experiment with the standardconfigurations use the following instructions:

```
python experiment.py -p <protein> -d <dimensions>

```
        :argument -p <protein> : Protein to be analyzed
                                 Integer reflecting 1 of the proteins in the /data folder
        :argument -d <dimensions> : dimension to be analyzed
                                        2 = 2D
                                        3 = 3D (default)


## Authors

* Amber Brands 
* Jara Linders
* Marrit Leenstra

## Acknowledgments

* Minor programmeren van de UvA
* Special thanks to our TA Bram van den Heuvel

