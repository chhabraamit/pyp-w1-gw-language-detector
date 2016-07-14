# -*- coding: utf-8 -*-

"""This is the entry point of the program."""

from .languages import LANGUAGES


def detect_language(text, languages=LANGUAGES):
	"""Returns the detected language of given text."""
	max_common_words = 0
	for language in languages:
		common_words = language["common_words"]
		common_words_count = get_common_words_count(text, common_words)
		if common_words_count > max_common_words:
			max_common_words = common_words_count
			ans = language["name"]
	return ans

def get_common_words_count(text, words):
    """ returns number of words in list 'words' 
    are in string 'text' and normalize them"""
    ans = 0
    lower_text = text.lower()
    set_text = set(lower_text.split(" "))
    for word in words:
        if word in set_text:
            ans += 1
    return ans/(len(set_text))

