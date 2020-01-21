from . import Question
import re
class Sort(Question):
    def scripts(self):
        #return({'jquery': 'https://code.jquery.com/jquery-1.12.4.js', 'sortablejs': 'https://raw.githack.com/SortableJS/Sortable/master/Sortable.js', 'jquery-sortable': 'https://cdn.jsdelivr.net/npm/jquery-sortablejs@latest/jquery-sortable.js'})
        return(['https://code.jquery.com/jquery-1.12.4.js',
            'https://raw.githack.com/SortableJS/Sortable/master/Sortable.js',
            'https://cdn.jsdelivr.net/npm/jquery-sortablejs@latest/jquery-sortable.js',
            #'/static/js/swap_cards.js'
            ])

    def check_answer(self):
        params = self.params()
        shuffle = params['shuffle']
        print(self.form.answer.data)
        try:
            input_order = [int(i) for i in re.split(",",self.form.answer.data)]
        except:
            return(False)
        card_order = [shuffle[i] for i in input_order]
        print(input_order)
        print(params['solutions'])
        correct = input_order in params['solutions']
        print(correct)
        return(correct)
