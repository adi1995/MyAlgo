#basic perceptron network for learning the OR logic

import numpy as np

class PerceptronNetwork:
    def __init__(self, inputSet, targetSet):
        
        #Neural Node Initialization code here

        self.mInputSet = inputSet
        self.mTargetSet = targetSet

        self.mDataSize = np.shape(self.mInputSet)[0]

        if np.ndim(self.mInputSet) > 1 :
            self.mInputCount = np.shape(self.mInputSet)[1]
        else :
            self.mInputCount = 1
        
        if np.ndim(self.mTargetSet) > 1 :
            self.mNodeCount = np.shape(self.mTargetSet)[1]
        else :
            self.mNodeCount = 1

        self.mWeights = np.random.rand(self.mInputCount + 1, self.mNodeCount) * 0.1 - 0.05
        
        print 'Initials '

        print'Weight'
        print self.mWeights
        print '\n'

        print 'Input Set'
        print self.mInputSet
        print '\n'

        print 'Target Set'
        print self.mTargetSet
        print '\n\n\n'

    def getActivations(self) :
        activations= np.dot(self.mInputSet, self.mWeights)
        return np.where(activations > 0, 1, 0)
    
    def train(self, learningRate, niterations) :
        self.mInputSet = np.concatenate((self.mInputSet, -np.ones((self.mDataSize, 1))), axis = 1)

        for i in range(niterations) :
            print 'Iteration: ', i
            activations = self.getActivations()
            self.mWeights -= learningRate * np.dot(np.transpose(self.mInputSet), activations - self.mTargetSet)

            print 'Final Output: '
            print activations
            print '\n'