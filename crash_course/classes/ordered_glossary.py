from collections import OrderedDict

glossary = OrderedDict()
glossary['variable'] = 'named location in memory with specified type'
glossary['list'] = 'ordered sequence of values'
glossary['loop'] = 'series of repeating actions'
glossary['dictionary'] = 'collection of key-value pairs'
glossary['tuple'] = 'immutable sequence of values'
glossary['set'] = 'collection of non-repeating values'

for word, meaning in glossary.items():
    print(f"\n{word.title()}: {meaning}.")
