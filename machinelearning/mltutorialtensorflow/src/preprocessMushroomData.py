import pandas as pd

df = pd.read_csv('../data/secondary_data.csv', sep=';')

# preprocess data
# especially strings can not be an input to a ml-model. therefore we need to transform the strings.
df['class'] = df['class'].apply(lambda x: 1 if x=='p' else 0)
df['cap-shape'] = df['cap-shape'].apply(
    lambda letter: {'b': 1.0, 'c': 2.0, 'x': 3.0, 'f': 4.0, 's': 5.0, 'p': 6.0, 'o': 7.0}.get(letter, 0.0))
df['cap-surface'] = df['cap-surface'].apply(
    lambda letter: {'i': 1.0, 'g': 2.0, 'y': 3.0, 's': 4.0, 'h': 5.0, 'l': 6.0, 'k': 7.0,
                    't': 8.0, 'w': 9.0, 'e': 10.0}.get(letter, 0.0))
df['cap-color'] = df['cap-color'].apply(
    lambda letter: {'n': 1.0, 'b': 2.0, 'g': 3.0, 'r': 4.0, 'p': 5.0, 'u': 6.0, 'e': 7.0,
                    'w': 8.0, 'y': 9.0, 'l': 10.0, 'o': 11.0, 'k': 12.0}.get(letter, 0.0))
df['does-bruise-or-bleed'] = df['does-bruise-or-bleed'].apply(lambda x: 1 if x=='t' else 0)
df['gill-attachment'] = df['gill-attachment'].apply(
    lambda letter: {'a': 1.0, 'x': 2.0, 'd': 3.0, 'e': 4.0, 's': 5.0, 'p': 6.0, 'f': 7.0, '?': 8.0}.get(letter, 0.0))
df['gill-spacing'] = df['gill-spacing'].apply(
    lambda letter: {'c': 1.0, 'd': 2.0, 'f': 3.0}.get(letter, 0.0))
df['gill-color'] = df['gill-color'].apply(
    lambda letter: {'n': 1.0, 'b': 2.0, 'g': 3.0, 'r': 4.0, 'p': 5.0, 'u': 6.0, 'e': 7.0,
                    'w': 8.0, 'y': 9.0, 'l': 10.0, 'o': 11.0, 'k': 12.0, 'f': 13.0}.get(letter, 0.0))
df['stem-root'] = df['stem-root'].apply(
    lambda letter: {'b': 1.0, 's': 2.0, 'c': 3.0, 'u': 4.0, 'e': 5.0, 'z': 6.0, 'r': 7.0}.get(letter, 0.0))
df['stem-surface'] = df['stem-surface'].apply(
    lambda letter: {'i': 1.0, 'g': 2.0, 'y': 3.0, 's': 4.0, 'h': 5.0, 'l': 6.0, 'k': 7.0,
                    't': 8.0, 'w': 9.0, 'e': 10.0, 'f': 11.0}.get(letter, 0.0))
df['stem-color'] = df['stem-color'].apply(
    lambda letter: {'n': 1.0, 'b': 2.0, 'g': 3.0, 'r': 4.0, 'p': 5.0, 'u': 6.0, 'e': 7.0,
                    'w': 8.0, 'y': 9.0, 'l': 10.0, 'o': 11.0, 'k': 12.0, 'f': 13.0}.get(letter, 0.0))
df['veil-type'] = df['veil-type'].apply(lambda x: 1 if x=='p' else 0)
df['veil-color'] = df['veil-color'].apply(
    lambda letter: {'n': 1.0, 'b': 2.0, 'g': 3.0, 'r': 4.0, 'p': 5.0, 'u': 6.0, 'e': 7.0,
                    'w': 8.0, 'y': 9.0, 'l': 10.0, 'o': 11.0, 'k': 12.0, 'f': 13.0}.get(letter, 0.0))
df['has-ring'] = df['has-ring'].apply(lambda x: 1 if x=='t' else 0)
df['ring-type'] = df['ring-type'].apply(
    lambda letter: {'c': 1.0, 'e': 2.0, 'r': 3.0, 'g': 4.0, 'l': 5.0, 'p': 6.0, 's': 7.0,
                    'z': 8.0, 'y': 9.0, 'm': 10.0, 'f': 11.0, '?': 12.0}.get(letter, 0.0))
df['spore-print-color'] = df['spore-print-color'].apply(
    lambda letter: {'n': 1.0, 'b': 2.0, 'g': 3.0, 'r': 4.0, 'p': 5.0, 'u': 6.0, 'e': 7.0,
                    'w': 8.0, 'y': 9.0, 'l': 10.0, 'o': 11.0, 'k': 12.0}.get(letter, 0.0))
df['habitat'] = df['habitat'].apply(
    lambda letter: {'g': 1.0, 'l': 2.0, 'm': 3.0, 'p': 4.0, 'h': 5.0, 'u': 6.0, 'w': 7.0,
                    'd': 8.0}.get(letter, 0.0))
df['season'] = df['season'].apply(
    lambda letter: {'s': 1.0, 'u': 2.0, 'a': 3.0, 'w': 4.0}.get(letter, 0.0))

print(df)

df.to_csv('../data/mushrooms.csv', index=False)