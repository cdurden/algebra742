from . import Question
import re
class Sort(Question):
    def scripts(self):
        #return({'jquery': 'https://code.jquery.com/jquery-1.12.4.js', 'sortablejs': 'https://raw.githack.com/SortableJS/Sortable/master/Sortable.js', 'jquery-sortable': 'https://cdn.jsdelivr.net/npm/jquery-sortablejs@latest/jquery-sortable.js'})
        return(['https://code.jquery.com/jquery-1.12.4.js', 'https://raw.githack.com/SortableJS/Sortable/master/Sortable.js', 'https://cdn.jsdelivr.net/npm/jquery-sortablejs@latest/jquery-sortable.js', '/static/js/swap_cards.js'])

    def check_answer(self):
        params = self.params()
        shuffle = params['shuffle']
        print(self.form.answer.data)
        input_order = [int(re.split("=",x)[1]) for x in re.split("&",self.form.answer.data)]
        card_order = [shuffle[i] for i in input_order]
        return(card_order in params['solutions'])

