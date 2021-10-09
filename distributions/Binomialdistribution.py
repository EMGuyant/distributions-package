import math
import matplotlib.pyplot as plt
from .Generaldistribution import Distribution

class Binomial(Distribution):
    """ Binomial distribution class for calculating and 
    visualizing a Binomial distribution.
    
    Attributes:
        mean (float) representing the mean value of the distribution
        stdev (float) representing the standard deviation of the distribution
        data_list (list of floats) a list of floats to be extracted from the data file
        p (float) representing the probability of an event occurring
                
    """
    
    def __init__(self, prob = 0.5, size = 20):
        self.p = prob
        self.n = size

        Distribution.__init__(self, self.calculate_mean(), self.calculate_stdev())
   
    def calculate_mean(self):
        """
        Function to calculate the mean from p and n
        
        Arguments: 
            None
        
        Returns: 
            float: mean of the data set
    
        """
        self.mean = self.p * self.n

        return self.mean

    def calculate_stdev(self):
        """
        Function to calculate the standard deviation from p and n.
        
        Arguments: 
            None
        
        Returns: 
            float: standard deviation of the data set
    
        """

        self.stdev = math.sqrt(self.n * self.p * (1 - self.p))

        return self.stdev

    def replace_stats_with_data(self):
        """
        Function to calculate p and n from the data set. The function updates the p and n variables of the object.
        
        Arguments: 
            None
        
        Returns: 
            float: the p value
            float: the n value
    
        """ 

        self.n = len(self.data)
        self.p = 1.0 * sum(self.data) / len(self.data)
        self.mean = self.calculate_mean()
        self.stdev = self.calculate_stdev()

        return self.p, self.n

    def plot_bar(self):
        """
        Function to output a histogram of the instance variable data using 
        matplotlib pyplot library.
        
        Arguments:
            None
            
        Returns:
            None
        """

        plt.bar(x = ['0', '1'], height = [(1 - self.p) * self.n, self.p * self.n])
        plt.title('Bar Chart of Data')
        plt.xlabel('outcome')
        plt.ylabel('count')

    def pdf(self, k):
        """
        Probability density function calculator for the binomial distribution.
        
        Arguments:
            k (float): point for calculating the probability density function
            
        
        Returns:
            float: probability density function output
        """
        a = math.factorial(self.n) / (math.factorial(k) * (math.factorial(self.n - k)))
        b = (self.p ** k) * (1 - self.p) ** (self.n - k)

        return a * b

    def plot_bar_pdf(self):
        """
        Function to plot the pdf of the binomial distribution
        
        Arguments:
            None
        
        Returns:
            list: x values for the pdf plot
            list: y values for the pdf plot
            
        """

        x = []
        y = []

        #Calculate the x value to be visualized
        for i in range(self.n + 1):
            x.append(i)
            y.append(self.pdf(i))

        #Create the plot
        plt.bar(x, y)
        plt.title('Distribution of Outcomes')
        plt.xlabel('Outcome')
        plt.ylabel('Probability')

        plt.show()

        return x, y

    def __add__(self, other):
        """
        Function to add together two Binomial distributions with equal p
        
        Arguments:
            other (Binomial): Binomial instance
            
        Returns:
            Binomial: Binomial distribution
            
        """
        
        try:
            assert self.p == other.p, 'p values are not equal'
        except AssertionError as error:
            raise
        
        result = Binomial()
        result.n = self.n + other.n
        result.p = self.p
        result.calculate_mean()
        result.calculate_stdev()

        return result

    def __repr__(self):                 
        """
        Function to output the characteristics of the Binomial instance
        
        Arguments:
            None
        
        Returns:
            string: characteristics of the Binomial object
        
        """
        return f'mean {self.mean}, standard deviation {self.stdev}'