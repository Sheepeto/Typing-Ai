from random import choice, random, randint
import sys
import json

def BreakScript(bad_letter):
    print("{} isn't allowed".format(bad_letter))
    input()
    sys.exit()
def loop():
    while True:
        # Detects if files exist if not creates new ones in current directory
        try:
            with open('words.txt') as f:
                finished_words = json.load(f)
        except FileNotFoundError:
            print("Could not load amounts.json")
            finished_words = []

        try:
            with open('numbers.txt') as f:
                finished_numbers = json.load(f)
        except FileNotFoundError:
            print("Could not load amounts.json")
            finished_numbers = []
        # Generates random number to pick if the ai will use numbers or words
        numbers_or_words = randint(1,2)

        if numbers_or_words == 1:
            # Determines current word or sentence and population for the algorithm
            print("Type what word or sentence you want the ai to type out then press enter")
            population_Size = randint(50,200)
            Genes = '''ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()~-_=+?/><,.;:'"\\|]}[{`1234567890 '''
            Word = str(input())
            
        else:
            # Determines current number and population for the algorithm
            print("Type what number you want the ai to type out then press enter")
            population_Size = randint(50,200)
            letters = []
            bad_words = '''ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()~-_=+?/><,.;:'"\\|]}[{`'''
            Genes = '1234567890'
            Word = str(input())
            
            for letter in Word:
                
                if letter in bad_words:
                    letters.append(letter)
                    bad_letter = letter
                    print("bad")
                    BreakScript(bad_letter)
                    
                
                else:
                    letters.append(letter)
        # If a word is used and is already in the files then prints the word back
        if Word in finished_words or Word in finished_numbers:
            print(Word)
            print("I have achieved memory")

        else:


            class Individual:
                def __init__(self, chromosome):
                    self.chromosome = chromosome
                    self.fitness = self.calc_fitness()

                def calc_fitness(self):
                    global Word
                    fitness = 0
                    
                    for i in range(len(Word)):
                        
                        if Word[i] == self.chromosome[i]:
                            fitness += 1
                    return fitness

                @classmethod
                def create_gnome(self):
                    global Genes
                    return [choice(Genes) for i in Word]

                def reproduce(self, parent_2):
                    child_chromosome=[]
                    
                    for a, b in zip(self.chromosome, parent_2.chromosome):
                        prob = random()
                        
                        if prob > 0.9:
                            child_chromosome += [choice(Genes)]
                            
                        else:
                            child_chromosome += [choice([a, b])]
                    return Individual(child_chromosome)

            Gen = 1
            terminate = False

            population = []
            
            for i in range(population_Size):
                population += [Individual(Individual.create_gnome())]

            while not terminate:
                population = sorted(population,key=lambda x:len(Word)-x.fitness)
                
                if "".join(population[0].chromosome) == Word:
                    print(f'{Gen:04}: {"".join(population[0].chromosome)}')
                    print("I have achieved learn")
                    
                    if numbers_or_words == 1:
                        finished_words.append(Word)

                        with open('words.txt', 'w+') as f:
                            json.dump(finished_words, f)
                        terminate = True
                        break
                    
                    else:
                        finished_numbers.append(Word)

                        with open('numbers.txt', 'w+') as f:
                            json.dump(finished_numbers, f)
                        terminate = True
                        break

                if Gen > 10000:
                    print("I have failed sorry")
                    terminate = True
                    break

                new_generation = []
                s = int(0.1*population_Size)
                new_generation.extend(population[:s])

                s = population_Size-s
                
                for i in range(s):
                    parent_1 = choice(population[:population_Size//2+1])
                    parent_2 = choice(population[:population_Size//2+1])
                    child = parent_1.reproduce(parent_2)
                    new_generation += [child]

                population = new_generation
                print(f'{Gen:04}: {"".join(population[0].chromosome)}')
                Gen += 1

            print(f'{Gen:04}: {"".join(population[0].chromosome)}')
            input()
loop()