import itertools
from collections import Counter
from wordfreq import zipf_frequency
from math import prod

def get_parity(letter):
    return (ord(letter.lower()) - ord('a')) % 2


def count_parity(word):
    return count_parity_counter(Counter(word.lower()))


def count_parity_counter(counter):
    r = sum(counter[l] for l in counter if not get_parity(l))
    b = sum(counter[l] for l in counter if get_parity(l))
    return r, b


freq_threshold = 2  # 1 in 1e6 words

def is_word(word):
    return zipf_frequency(word, 'en') > freq_threshold


def best_word(letters):
    words = []
    for word in itertools.permutations(letters):
        word = ''.join(word)
        freq = zipf_frequency(word, 'en', 'small')
        if freq < freq_threshold:
            continue
        words.append((freq, word))
    if len(words) == 0:
        return None
    return max(words)[1]

# Assumes lowercase
def beta_decay(letter, shift):
    return chr(ord(letter) + shift)


def search_parity(input_word, output_counts, shift=0, remove=0):
    input_word = ''.join(sorted(input_word))

    # Handle beta decay shifts
    if shift != 0:
        results = []
        for letter in set(input_word):
            shifted_letter = beta_decay(letter, shift)
            if not shifted_letter.isalpha():
                continue
            shifted_word = input_word.replace(letter, shifted_letter, 1)
            results.extend(search_parity(shifted_word, output_counts, 0, remove))
        return results
        

    # Handle gamma emission removals
    if remove != 0:
        results = []
        for letter in set(input_word):
            removed_word = input_word.replace(letter, '', 1)
            results.extend(search_parity(removed_word, output_counts, shift, remove - 1))
        return results

    input_count = count_parity(input_word)
    if len(output_counts) == 1:
        if input_count != output_counts[0]:
            return []
        best_output_word = best_word(input_word)
        if best_output_word is None:
            return []
        return [best_output_word]

    output_count0 = output_counts[0]

    word0_len = sum(output_count0)

    # Check if parity is possible
    if input_count[0] < output_count0[0] or input_count[1] < output_count0[1]:
        return []

    solutions = []
    already_tried = set()
    for letters0 in itertools.combinations(input_word, word0_len):
        letters0 = ''.join(sorted(letters0))
        if letters0 in already_tried:
            continue
        else:
            already_tried.add(letters0)

        if count_parity(letters0) != output_count0:
            continue

        word0 = best_word(letters0)
        if word0 is None:
            continue

        other_letters = ''.join((Counter(input_word) - Counter(letters0)).elements())
        other_words = search_parity(other_letters, output_counts[1:])
        if len(other_words) == 0:
            continue
        solutions.append([word0] + other_words)

    return solutions


def print_solutions(solutions):
    scored_solutions = [
        (prod(zipf_frequency(w, 'en', 'small') for w in solution), solution)
        for solution in solutions
    ]
    for score, solution in sorted(scored_solutions, reverse=True):
        print(f"{score:.1f}: {solution}")
