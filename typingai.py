from random import choice, random, randint

print("Type what word or sentence you want the ai to type out then press enter")
population_Size = randint(50,200)
Genes = '''ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()~-_=+?/><,.;:'"\\|]}[{`1234567890 '''
Word = str(input())

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
    if population[0].fitness == len(Word) or Gen > 10000:
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