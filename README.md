# Significance-Based Essential Protein Discovery<br>
## Introduction<br>
SigEP can  identity the essential proteins from Protein-Protein Interaction network: we present a p-value calculation method for quantifying the statistical significance of each protein by considering both its degree and local clustering coefficient. To reduce the computational cost, we further present an upper bound of the p-value, which is less timeconsuming in practice. After calculating the p-value for each protein, we control the FDR of identified essential proteins using the well-known BH algorithm.
## Usage<br>
Implementation of SigEP is available in Python 2.7.<br>

Import the python code into Pycharm, and then load some datasets to test. By the way, the significance level alpha also could be user-specific (the default of significance level is 0.01 in our paper). After that complie and run the code. Finally, the result will be obtained.<br>

In addition, we also provide the four datasets (DIP, Gavin, Krogan and MIPS). And the file of essential in dataset file is used to assess the algorithm's performance.
