This is a coding sample of the Viterbi algorithm

There are a total of 3 scripts to run in this example:
prepDataUtil.py: Processes the data in "test.txt" and saves the tokenized sentences without tags in procTest
	Run: python prepDataUtil,py <test file>
             python prepDataUtil.py test.txt 
viterbi.py: The majority of the code in this sample. Implements the Viterbi Algorithm for Parts-of-Speech tag prediction used pre-trained weights. Saves a file with all the predicted tags in "results.txt"
	Run: python viterbi.py <weightsfile> <processedTest file>
	     python viterbi.py featureSet.txt procTest.txt
accuracyUtil.py: Calculates the accuracy of the Parts-of-Speech tag prediction saved to "results.txt". This is largely determined by the quality of the weights trained.
	Run: python accuracyUtil.py <prediction results file> <gold standard file> 
	     python accuracyUtil.py results.txt test.txt

The runtime of the Viterbi algorithm is expected given that the algorithm has time complexity O(N^2T).