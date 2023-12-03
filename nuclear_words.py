import itertools
from collections import Counter
from typing import Tuple

with open('words_alpha.txt') as word_file:
    valid_words = set(word_file.read().split())


def get_parity(letter) -> int:
    return (ord(letter.lower()) - ord('a')) % 2


def count_parity(word) -> Tuple[int, int]:
    return count_parity_counter(Counter(word.lower()))


def count_parity_counter(counter) -> Tuple[int, int]:
    r = sum(counter[l] for l in counter if not get_parity(l))
    b = sum(counter[l] for l in counter if get_parity(l))
    return r, b


import itertools
from collections import Counter
from wordfreq import zipf_frequency


def get_parity(letter):
    return (ord(letter.lower()) - ord('a')) % 2


def count_parity(word):
    return count_parity_counter(Counter(word.lower()))


def count_parity_counter(counter):
    r = sum(counter[l] for l in counter if not get_parity(l))
    b = sum(counter[l] for l in counter if get_parity(l))
    return r, b


freq_threshold = 2

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


def search_parity(input_word, output_counts):
    input_count = count_parity(input_word)
    if len(output_counts) == 1:
        if input_count != output_counts[0]:
            return None
        if output_counts[0][0] + output_counts[0][1] <= 2:
            return [input_word] # don't bother checking for the word
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
