class Distribution:
	
	def __init__(self, mu=0, sigma=1):
		"""
		Generic distribution class for calculating and visualizing a
        probability distribution
        
        Attributes:
            mean (float) the mean value of the distribution
            stdev (float) the standard deviation of the distribution
            data_list (list of floats) a list of floats extracted from the data
            file 
		"""
		
		self.mean = mu
		self.stdev = sigma
		self.data = []


	def read_data_file(self, file_name):
		"""
		Function that reads text file of data. The text file should only have
        one float per line. The data read will get stored in the objects data
        attributes.
        
        Arguments:
            file_name (string): name of the data file

        Return:
            None
		"""
			
		with open(file_name) as file:
			data_list = []
			line = file.readline()
			while line:
				data_list.append(int(line))
				line = file.readline()
		file.close()
	
		self.data = data_list
