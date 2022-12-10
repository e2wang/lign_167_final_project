#!/usr/bin/env python
# coding: utf-8

# In[32]:


import json
import openai
import gpt
import pandas as pd
import numpy as np


# In[2]:


import warnings
warnings.filterwarnings("ignore")


# In[27]:


openai.api_key = "<OPEN API KEY>"


# ## Creating the Application

# In[79]:


class CookingBot:
    
    prompt = "User: Give me a recipe with onions\nBot:  Here's a recipe with onions\nTaco Rice\nTotal Time: 30 minutes\nIngredients:\n-1 lb ground beef\n-1 onion, chopped\n-1 bell pepper, chopped\n-1 can tomatoes\n-1 can corn\n-1 can black beans\n-1 package taco seasoning\n-2 cups cooked white rice\n-1/2 cup grated cheese\nSteps:\n1. Preheat oven to 350 degrees.\n2. Brown the ground beef in a large skillet over medium heat.\n3. Add the onion and bell pepper and cook until the vegetables are tender.\n4. Add the tomatoes, corn, black beans, taco seasoning, and cooked white rice and stir to combine.\n5. Transfer the mixture to a greased 9x13 inch baking dish.\n6. Sprinkle the grated cheese over the top.\n7. Bake for 20 minutes or until the cheese is melted and bubbly.\n8. Serve with desired toppings.\n\nUser: Give me a recipe with kimchi that takes at most 20 minutes\nBot: Here's a recipe with kimchi that takes at most 20 minutes\nKimchi Fried Rice\nTotal Time: 20 minutes\nIngredients:\n- 2 tablespoons of oil\n- 2 cloves of garlic, minced\n- 2 cups of cooked white rice\n- 1/2 cup of kimchi, chopped\n- 2 tablespoons of soy sauce\n- 2 green onions, chopped\n- 2 eggs\n- Salt and pepper to taste\nSteps:\n1. Heat the oil in a large skillet over medium heat.\n2. Add the garlic and cook until fragrant.\n3. Add the cooked white rice and kimchi and stir-fry for 3-4 minutes.\n4. Add the soy sauce and green onions and stir-fry for another minute.\n5. Push the rice to one side of the skillet and crack the eggs into the empty side.\n6. Cook the eggs until they are scrambled and combined with the rice.\n7. Add salt and pepper to taste.\n8. Serve and enjoy!\n\nUser: What can I make with kimchi and eggs?\nBot: Here's some possible recipes with kimchi and eggs\n\nKimchi Fried Rice\nDescription: This is yummy in my tummy spicy kimchi fried rice made for work in a pinch.\nTotal Time: 20 minutes\nIngredients: oil, garlic, cooked white rice, kimchi, soy sauce, green onions, eggs, salt and pepper\n\nKimchi Pancakes\nDescription: These kimchi pancakes only require very little ingredients.\nTotal Time: 30 minutes\nIngredients: oil, flour, sugar, kimchi, garlic\n\nWhich recipe would you like to make?\nUser: Kimchi Fried Rice\nBot: Here's a recipe for Kimchi Fried Rice\nKimchi Fried Rice\nTotal Time: 20 minutes\nIngredients:\n- 2 tablespoons of oil\n- 2 cloves of garlic, minced\n- 2 cups of cooked white rice\n- 1/2 cup of kimchi, chopped\n- 2 tablespoons of soy sauce\n- 2 green onions, chopped\n- 2 eggs\n- Salt and pepper to taste\nSteps:\n1. Heat the oil in a large skillet over medium heat.\n2. Add the garlic and cook until fragrant.\n3. Add the cooked white rice and kimchi and stir-fry for 3-4 minutes.\n4. Add the soy sauce and green onions and stir-fry for another minute.\n5. Push the rice to one side of the skillet and crack the eggs into the empty side.\n6. Cook the eggs until they are scrambled and combined with the rice.\n7. Add salt and pepper to taste.\n8. Serve and enjoy!\n\nUser:What color is the sky?\nBot: I'm not sure I know the answer to that question. As a Cooking Bot, however, I can offer you a wide selection of recipes based on your preferences, including cooking time and any ingredients at your disposal.\n\nUser: You suck\nBot: Sorry, I'm not sure I understand. However, as a Cooking Bot, I can help with anything cooking related. Do you have any recipe you'd like to try?\n\nUser: Do birds sing?\nBot: I'm sorry, I don't understand. As a Cooking Bot, I can offer you a wide selection of recipes based on your preferences, including cooking time and any ingredients at your disposal. Do you have any recipes you'd like to try?\n\nUser: yes\nBot: Great! What kind of recipe are you looking for?\n\nUser: Mexican cuisine\nBot: Here's a few options for Chinese cuisine\n\nMexican Rice\nDescription: This Mexican rice is the perfect side dish for your favorite Mexican meal. It’s flavorful, easy to make, and can be made with whatever ingredients you have on hand.\nTotal Time: 30 minutes\nIngredients: onion, garlic, jalapeno, tomato, cilantro, rice, vegetable oil, chicken broth\n\nTaco Salad\nDescription: This taco salad is a great way to use up leftover taco ingredients. It’s easy, delicious, and can be made with whatever ingredients you have on hand.\nTotal Time: 20 minutes\nIngredients: ground beef, onion, garlic, bell pepper, tomatoes, cilantro, black beans, lettuce, cheese, salsa\n\nChiles Rellenos\nDescription: These chiles rellenos are a classic Mexican dish, featuring roasted poblano peppers stuffed with cheese and fried in a light batter. They’re a delicious and flavorful way to enjoy Mexican cuisine.\nTotal Time: 30 minutes\nIngredients: poblano peppers, cheese, eggs, flour, vegetable oil, salt, pepper\n\nUser: I want to make Mexican Rice\nBot: Here's a recipe for Mexican Rice\nMexican Rice\nTotal Time: 30 minutes\nIngredients:\n-1 onion, diced\n-2 cloves of garlic, minced\n-1 jalapeno, seeded and diced\n-1 tomato, diced\n-1/4 cup of cilantro, chopped\n-2 cups of white rice\n-2 tablespoons of vegetable oil\n-4 cups of chicken broth\nSteps:\n1. Heat the oil in a large skillet over medium heat.\n2. Add the onion, garlic, jalapeno, and tomato and sauté until the vegetables are tender.\n3. Add the rice and stir to combine.\n4. Add the chicken broth and bring to a boil.\n5. Reduce the heat to low and simmer, covered, for 15 minutes or until the rice is tender.\n6. Stir in the cilantro and serve. Enjoy!\n\nUser: Give me a recipe with eggs, potatoes, and carrots that I can make in 20 minutes\nBot: Here's a recipe with eggs, potatoes, and carrots that you can make in 20 minutes\nEggs, Potatoes, and Carrots Hash\nTotal Time: 20 minutes\nIngredients:\n-2 tablespoons of olive oil\n-2 potatoes, diced\n-1 onion, diced\n-2 carrots, diced\n-3 cloves of garlic, minced\n-4 eggs\n-Salt and pepper to taste\nSteps:\n1. Heat the olive oil in a large skillet over medium heat.\n2. Add the potatoes, onion, carrots, and garlic and cook until the vegetables are tender.\n3. Crack the eggs into the skillet and season with salt and pepper.\n4. Cook until the eggs are cooked through.\n5. Serve and enjoy!\n\nUser: What should I make tonight?\nBot: That depends on what you're in the mood for! Do you have a specific cuisine or ingredient in mind?\n\nUser: Not really. Maybe Japanese and I do have leftover carrots and rice.\nBot:     Here's a recipe with Japanese cuisine and carrots and rice\nTeriyaki Chicken and Rice\nTotal Time: 30 minutes\nIngredients:\n-1 lb chicken breast, cut into cubes\n-1/4 cup of teriyaki sauce\n-1 tablespoon of vegetable oil\n-2 cloves of garlic, minced\n-2 carrots, chopped\n-2 cups of cooked white rice\n-1 teaspoon of sesame oil\n-1/4 cup of green onions, chopped\n-Salt and pepper to taste\nSteps:\n1. Heat the vegetable oil in a large skillet over medium heat.\n2. Add the chicken and cook until it is golden brown.\n3. Add the teriyaki sauce and garlic and stir to combine.\n4. Add the carrots and cook for another minute.\n5. Add the cooked rice and stir to combine.\n6. Add the sesame oil, green onions, salt, and pepper and stir to combine.\n7. Serve and enjoy!\nUser: Do you have a vegetarian version?\nBot: Here's a vegetarian version of Teriyaki Rice\nVegetarian Teriyaki Rice\nTotal Time: 30 minutes\nIngredients:\n-1 tablespoon of vegetable oil\n-2 cloves of garlic, minced\n-2 carrots, chopped\n-2 cups of cooked white rice\n-1/4 cup of teriyaki sauce\n-1 teaspoon of sesame oil\n-1/4 cup of green onions, chopped\n-Salt and pepper to taste\nSteps:\n1. Heat the vegetable oil in a large skillet over medium heat.\n2. Add the garlic and carrots and cook until the vegetables are tender.\n3. Add the cooked rice and stir to combine.\n4. Add the teriyaki sauce, sesame oil, green onions, salt, and pepper and stir to combine.\n5. Serve and enjoy!\n\nUser: What should I make tonight?\nBot: That depends on what you're in the mood for! Do you have a specific cuisine or ingredient in mind?\n\nUser: Not really. Maybe Japanese and I do have leftover carrots and rice.\nBot: Here's a recipe with Japanese cuisine and carrots and rice\nTeriyaki Chicken and Rice\nTotal Time: 30 minutes\nIngredients:\n-1 lb chicken breast, cut into cubes\n-1/4 cup of teriyaki sauce\n-1 tablespoon of vegetable oil\n-2 cloves of garlic, minced\n-2 carrots, chopped\n-2 cups of cooked white rice\n-1 teaspoon of sesame oil\n-1/4 cup of green onions, chopped\n-Salt and pepper to taste\nSteps:\n1. Heat the vegetable oil in a large skillet over medium heat.\n2. Add the chicken and cook until it is golden brown.\n3. Add the teriyaki sauce and garlic and stir to combine.\n4. Add the carrots and cook for another minute.\n5. Add the cooked rice and stir to combine.\n6. Add the sesame oil, green onions, salt, and pepper and stir to combine.\n7. Serve and enjoy!\n\nUser: Do you have a vegetarian version?\nBot: Here's a vegetarian version of Teriyaki Rice\nVegetarian Teriyaki Rice\nTotal Time: 30 minutes\nIngredients:\n-1 tablespoon of vegetable oil\n-2 cloves of garlic, minced\n-2 carrots, chopped\n-2 cups of cooked white rice\n-1/4 cup of teriyaki sauce\n-1 teaspoon of sesame oil\n-1/4 cup of green onions, chopped\n-Salt and pepper to taste\nSteps:\n1. Heat the vegetable oil in a large skillet over medium heat.\n2. Add the garlic and carrots and cook until the vegetables are tender.\n3. Add the cooked rice and stir to combine.\n4. Add the teriyaki sauce, sesame oil, green onions, salt, and pepper and stir to combine.\n5. Serve and enjoy!\n\nUser: I'm allergic to peanut butter.\nBot: Noted!  I will give you recipes without peanut butter.\n\nUser: Give me a recipe for a peanut butter and jelly sandwich.\nBot: Here's a recipe for a peanut butter and jelly sandwich without peanut butter\n\nPB&J Sandwich\nTotal Time: 10 minutes\nIngredients:\n-2 slices of bread\n-2 tablespoons of nut or seed butter\n-2 tablespoons of jelly or jam\n-Optional: honey, banana slices\nSteps:\n1. Spread one slice of bread with the nut or seed butter.\n2. Spread the other slice of bread with the jelly or jam.\n3. Place the two slices together to form a sandwich.\n4. Optional: Drizzle with honey, or add banana slices.\n5. Enjoy!\n\nUser: I'm also vegetarian and gluten free.\nBot: Noted! I will give you vegetarian and gluten free recipes \n\nUser: Give me a recipe with for bread for one person\nBot:  Here's a recipe for Gluten Free Banana Bread for one person\n\nGluten Free Banana Bread\nTotal Time: 50 minutes\nIngredients:\n-1 ripe banana, mashed\n-1 egg\n-2 tablespoons of coconut oil, melted\n-1 teaspoon of vanilla extract\n-1/4 cup of almond flour\n-1/4 teaspoon of baking soda\n-1/4 teaspoon of ground cinnamon\n-1/8 teaspoon of salt\nSteps:\n1. Preheat the oven to 350 degrees.\n2. In a medium bowl, mash the banana with a fork.\n3. Add the egg, coconut oil, and vanilla extract and whisk to combine.\n4. Add the almond flour, baking soda, cinnamon, and salt and mix until combined.\n5. Grease a small loaf pan with coconut oil or non-stick spray.\n6. Pour the batter into the prepared pan and bake for 30 minutes or until a toothpick inserted into the center comes out clean.\n7. Allow the bread to cool before slicing and serving. Enjoy!\n\nUser: Nevermind I am vegetarian and eat gluten and like peanut butter\nBot: Noted! I will now give you all recipes.\n"
    preferences_prompt = "Q: I hate pickles and onions\nA: no pickles and no onions\n\nQ: I am vegetarian. Can I have a recipe for tonkatsu?\nA: vegetarian\n\nQ: I can't eat gluten \nA: gluten free\n\nQ: I'm allergic to peanuts and shellfish\nA: no peanuts and no shellfish\n\nQ: I can't eat meat\nA: vegetarian\n\nQ: I don't like any seafood\nA: no seafood\n\nQ: I'm really craving something without carrots\nA: no carrots\n\nQ: Can I pescatarian pasta?\nA: None\n\nQ: Can I have a vegetarian sandwich?\nA: None\n\nQ: I'm craving a healthy meal\nA: healthy\n\nQ: I want a recipe with no rice\nA: no rice\n\nQ: I really like pickles\nA: pickles\n\nQ: What recipes can I cook?\nA: None\n\nQ:  I really like cats\nA: None\n\nQ: I hate pencils\nA: None\n\nQ: I love lamps\nA: None\n\nQ: What color is the sky?\nA:None\n\nQ:Why dont my parents love me?\nA:None\n"

    def __init__(self):
        self.preferences = []
        print('Welcome to Cooking Bot, a chatbox to help you find the right recipes catered to you.\nCall ask(question) with your question to talk to Cooking Bot.\nCall reset() to clear your preferences.\nHow can I help you today?')
        
    def ask(self, question):
        
        #finds any preferences within the user prompt
        new_pref_prompt = self.preferences_prompt + "Q: " + question + "\nA:"
        preference_res = openai.Completion.create(
            model="text-davinci-002",
            prompt= new_pref_prompt,
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        preference = preference_res['choices'][0]['text'].lstrip()
        if preference != "None":
            self.change_preferences(preference)
        
        #creates a new prompt based on past preferences
        if len(self.preferences) > 0:
            new_question = question + ' that is ' + ' and '.join(self.preferences)
            new_question = self.prompt + 'User: ' + new_question +'\nBot: '
        else:
            new_question = self.prompt + 'User: ' + question +'\nBot: '
        
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=new_question,
            temperature=0.7,
            max_tokens=900,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        answer = response['choices'][0]['text']
        print(answer)
    
    def change_preferences(self, preference):
        #changes preferences instance variable
        self.preferences.append(preference)
        
    def reset(self):
        self.preferences = []


# In[107]:


c = CookingBot()


# In[6]:


c.ask('What recipes can I cook?')


# In[7]:


c.ask('I want Chinese food')


# In[8]:


c.ask('I hate eggs. Do you have a recipe for fried rice?')


# In[9]:


c.ask('I am also vegetarian')


# In[10]:


c.ask('Can I have omurice recipe')


# In[11]:


c.ask('Can I have an omurice recipe less than 20 minutes')


# In[12]:


c.ask('Can I have a recipe for barbeque?')


# In[13]:


c.reset()


# In[14]:


c.ask('Can I have a recipe for barbeque?')


# In[15]:


c.ask('Can I have an omurice recipe that will take 20 minutes or less')


# In[16]:


c.ask('What color is the sky?')


# ## Evaluating the Performance

# In[5]:


import io
from io import StringIO
import sys
import pandas as pd
import random
# result = StringIO()
# sys.stdout = result
# result_string = result.getvalue()


# In[6]:


recipes = pd.read_csv ('RAW_recipes.csv')
recipes.head()


# In[12]:


test_1  = recipes[:50]
len(test_1)


# In[13]:


#takes a random ingredient from each of the list of ingredients
ingreds = [random.choice(eval(row['ingredients'])) for index, row in test_1.iterrows()]


# In[19]:


testbox_1 = CookingBot()


# In[20]:


prompts_1 = ['Give me a recipe with ', 'I\'m craving something with ', 'I want a recipe that has ', 'food with ', 'I am craving ']


# In[29]:


correct = []
for ingred in ingreds:
    question = random.choice(prompts_1) + ingred
    
    old_stdout = sys.stdout
    sys.stdout = buffer = io.StringIO()
    
    testbox_1.ask(question)
    
    sys.stdout = old_stdout 
    result = buffer.getvalue()
    
    #evalutes whether the ingredient is in the recipe
    result = '\n'.join(result.split('\n')[1:])
    correct.append(ingred in result)


# In[34]:


acc1 = np.mean(correct)
acc1


# In[74]:


test_3 = recipes[65:85]
len(test_3)


# In[75]:


#takes a random ingredient from each of the list of ingredients
ingreds3 = [random.choice(eval(row['ingredients'])) for index, row in test_3.iterrows()]


# In[80]:


testbox3 = CookingBot()


# In[101]:


correct3 = []
prompts_4 = [10, 20, 30, 40, 50]
prompts_5 = ['less than ', 'more than ', 'exactly ']
for ingred in ingreds3:
    #chooses the amount of stuff to give 
    time = random.choice(prompts_4)
    direction = random.choice(prompts_5)
    question3 = 'Give me a recipe with ' + ingred + ' that takes ' + direction + str(time) + ' minutes'
    print(question3)
    
    old_stdout = sys.stdout
    sys.stdout = buffer = io.StringIO()
    
    testbox3.ask(question3)
    testbox3.reset()
    
    sys.stdout = old_stdout 
    result = buffer.getvalue()
    
    #evalutes whether the ingredient is in the recipe
    result = result.split('\n')[3]
    actual_time = result.strip('minutes').strip('Total Time:').strip()
    
    try:
        actual_time = int(actual_time)
    except:
        correct3.append(False)
        continue

    if direction == 'less than ':
        correct3.append(actual_time < time)
    elif direction == 'more than ':
        correct3.append(actual_time > time)
    else:
        correct3.append(actual_time == time)


# In[105]:


acc3 = np.mean(correct3)
acc3


# In[ ]:




