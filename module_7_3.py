import io

class WordsFinder:

    def __init__(self, *file_txt):

        self.file_names = file_txt


    def get_all_words(self):
        
        all_words = {}
        
        for i in self.file_names:
            with open(i, 'r', encoding='utf-8') as file:
                
                file = file.read().lower()
                #
                for j in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    
                    file = file.replace(j, '')
                
                words = file.split()
                
                all_words[i] = words
        
        return all_words

   
    def find(self, word):
        
        result = {}
        
        for i, word_ in self.get_all_words().items():
            
            for j, wd in enumerate(word_, 1):
                
                if wd == word.lower():
                
                    result[i] = j
                   
                    break
        
        return result

    
    def count(self, word):
        
        result_={}
        
        for i, word_ in self.get_all_words().items():
          
            result_[i] = word_.count(word.lower())
        
        return result_

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) 
print(finder2.find('TEXT')) 
print(finder2.count('teXT'))
