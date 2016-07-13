"""This is the entry point of the program."""

from .languages import LANGUAGES


def detect_language(text, languages=LANGUAGES):
	"""Returns the detected language of given text."""
	max_common_words = 0
	for language in languages:
		common_words = language["common_words"]
		common_words_count = getCount(text, common_words)
		print(language["name"], common_words_count)
		if common_words_count > max_common_words:
			max_common_words = common_words_count
			ans = language["name"]
	return ans

def getCount(text, words):
	ans = 0
	lower_text = text.lower()
	for word in words:
		ans+= lower_text.count(word)
	return ans/(len(lower_text.split(" ")))

