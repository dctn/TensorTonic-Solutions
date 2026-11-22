class SimpleTokenizer:
    def __init__(self):
        self.word_to_id = {}
        self.id_to_word = {}
        self.vocab_size = 0
        self.pad_token = "<PAD>"
        self.unk_token = "<UNK>"
        self.bos_token = "<BOS>"
        self.eos_token = "<EOS>"

    def build_vocab(self, texts: list[str]) -> None:
        """
        Builds the vocabulary in place.
        """
        self.word_to_id[self.pad_token] = 0
        self.word_to_id[self.unk_token] = 1
        self.word_to_id[self.bos_token] = 2
        self.word_to_id[self.eos_token] = 3
        self.vocab_size = 4

        word_list = []
        for text in texts:
            for word in text.split(" "):
                word_list.append(word.lower())

        for word in sorted(word_list):
            if word not in self.word_to_id:
                self.word_to_id[word.lower()] = self.vocab_size
                self.vocab_size += 1

        self.id_to_word = {id:word for word,id in self.word_to_id.items()}
        # print(self.id_to_word)
        # print(self.word_to_id)
        
    def encode(self, text: str) -> list[int]:
        """
        Returns token IDs for the input text.
        """
        if len(text) == 0:
            return []
        r = []
        text_list = text.split(" ")
        # self.build_vocab(text_list)
        # print(sorted(text_list))
        
        for word in text_list:
            word = word.lower()
            if word in self.word_to_id:
                r.append(self.word_to_id[word])
            else:
                r.append(1)
        return r
    def decode(self, ids: list[int]) -> str:
        """
        Returns the decoded, space-separated text.
        """
        r = []
        for id in ids:
            if id in self.id_to_word:
                r.append(self.id_to_word[id])
            else:
                r.append(self.unk_token)
        
        return " ".join(r)