PREREQUISITES:


1. Install Apache Spark(pyspark).

2. Downlaoad the training dataset and test dataset in kddcup99 format(features are given in "kddFeatures.txt").



INSTRUCTIONS:


1. Run makeModel.py using the command "/path/spark/bin/spark-submit --driver-memory 2g makeModel.py max_k data_file" , where "/path/" is the path to pyspark's spark folder, "max_k" is an integer and "data_file" is the training dataset("training").

2. makeModel.py saves the best model created using the k-means clustering in the folder "best_model". The working directory should not contain any folder or file with the name "best_model" in order to work.

3. Run predict.py using the command "Usage: /path/park/bin/spark-submit --driver-memory 2g predict.py data_file" , where "/path/" is the path to pyspark's spark folder and "data_file" is the test dataset("testing").

4. predict.py prints the cluster index for each test in the test data file.

5. Run compute.py using the command "Usage: /path/park/bin/spark-submit --driver-memory 2g predict.py data_file" , where "/path/" is the path to pyspark's spark folder and "data_file" is the test dataset, but each test is labelled("labelled_test").

6. compute.py uses the same code as predict.py and finds the number of false positives, false negatives, true positives and true negatives by comparing the cluster index and the label.
