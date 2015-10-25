__author__ = 'root'
import Classification

class Drug:

    def __init__(self):
        self.primary_id = None
        self.other_ids = []
        self.name = ''
        self.description = ''
        self.indication = ''
        self.pharmacodynamics = ''
        self.classification = Classification()
        self.synonyms = []
        self.international_brands = []
        self.categories = []
        self.sequences = []
        self.molecular_weight = ''
        self.molecular_formula = ''

    def __init__(self, primary_id, other_ids, name, description, indication,
                 pharmacodynamics, classification, synonyms, international_brands,
                 categories, sequences, molecular_weight, molecular_formula):
        self.primary_id = primary_id
        self.other_ids = other_ids
        self.name = name
        self.description = description
        self.indication = indication
        self.pharmacodynamics = pharmacodynamics
        self.classification = classification
        self.synonyms = synonyms
        self.international_brands = international_brands
        self.categories = categories
        self.sequences = sequences
        self.molecular_weight = molecular_weight
        self.molecular_formula = molecular_formula


    def addClassificaion(self, classification):
        self.classification = classification

    def printout(self):
        print '--------Drug:--------'
        print 'Primary id: ' + self.primary_id
        print 'Other ids: '
        for ids in self.other_ids: print '\t> '+ ids
        print 'Name: ' + self.name
        print 'Description: ' + self.description
        print 'Indication: ' + self.indication
        print 'Pharmacodynamics: ' + self.pharmacodynamics
        self.classification.printout()
        print 'Synonyms: '
        for syn in self.synonyms: print '\t> '+ syn
        print 'International brands: '
        for ib in self.international_brands: print '\t> '+ ib
        print 'Categories: '
        for ct in self.categories: print '\t> '+ ct
        print 'Sequences: '
        for seq in self.sequences: seq.printout()
        #print 'Molecular weight: %f' %self.molecular_weight
        print 'Molecular weight: ' +self.molecular_weight
        print 'Molecular formula: ' + self.molecular_formula
        print '\n----------------\n'