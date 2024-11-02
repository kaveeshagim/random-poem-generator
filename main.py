import random

# Step 1: Define word lists
nouns = ["moon", "love", "heart", "dream", "shadow"]
verbs = ["whispers", "dances", "sings", "fades", "shines"]
adjectives = ["dark", "beautiful", "mysterious", "silent", "endless"]

# Step 2: Define a poem structure
def generate_poem():
    poem = []
    
    # AABB structure
    line1 = f"The {random.choice(adjectives)} {random.choice(nouns)} {random.choice(verbs)} in the night,"
    line2 = f"With {random.choice(adjectives)} {random.choice(nouns)} taking flight."
    line3 = f"Whispers of {random.choice(nouns)} float in the air,"
    line4 = f"While the {random.choice(nouns)} glows with a {random.choice(adjectives)} flair."

    poem.append(line1)
    poem.append(line2)
    poem.append(line3)
    poem.append(line4)

    return "\n".join(poem)

# Step 4: Generate and print the poem
if __name__ == "__main__":
    print(generate_poem())
