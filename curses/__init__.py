import random

nouns = ['mom', 'mike', 'dean', 'grandma']
adjectives = ['stupid', 'fat', 'great', 'married']
pronouns = ['my', 'your', 'our']
verbs = ['is', 'was', 'likes', 'brings']

def spew():
    print random.choice(pronouns), random.choice(nouns), random.choice(verbs), random.choice(adjectives)        
