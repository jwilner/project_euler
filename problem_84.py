
class Monopoly:
    '''
    class finding the probabilities of a Monopoly turn ending on every square for given dice (through simulation)
    problem 84
    '''
    def __init__(self,dice):
        '''
        requires dice passed (see helper function get_n_sided_dice), designates spots w/ special actions,
        creates lambdas expecting current position for every significant card
        '''
        self._cc_squares,self._ch_squares = {2,17,33}, {7,22,36}

        cc_cards = [lambda x,tar=tar:tar for tar in ['STAY']*14+[0,10]] #where the cc cards point
        random.shuffle(cc_cards)
        self._cc_cards = itertools.cycle(cc_cards) #itertools is awesome

        ch_cards = [lambda x,tar=tar:tar for tar in ['STAY']*6+[0,10,11,24,39,5]] #where the chance cards point
        next_rr = lambda x: {7:15,22:25,36:5}[x] #go to next railroad
        ch_cards.extend([next_rr,next_rr,lambda x: {7:12,22:28,36:12}[x],lambda x: x-3]) # next rr *2, next utility, go back 3
        random.shuffle(ch_cards)
        self._ch_cards = itertools.cycle(ch_cards)

        self._dice, self._doubles_counter = dice, 0

        self._current_position, self.end_positions = 0, collections.defaultdict(int)

    def play_turn(self):
        "only real interface with logic (makes sense -- neutered form of Monopoly might as well be Candyland, no decisions to be made)"
        roll = [random.choice(d) for d in self._dice]

        roll_target = None
        self._doubles_counter = 0 if not all(d == roll[0] for d in roll) else self._doubles_counter + 1  #checks for doubles, safe for 2+ dice, not for 1 die (feels silly to check length every time)
        if self._doubles_counter == 3: #checks for three doubles go to jail rule (would be fun to generalize for house rules)
            self._doubles_counter, roll_target = 0, 10 # go to jail
        else:
            new_spot = sum(roll)+self._current_position
            roll_target = new_spot if new_spot < 40 else new_spot-40 #this is the only place where 39-to-0 wrap around can happen, so address it here

        self._current_position = self._parse_move(roll_target) #pass dice roll to parse_move, save as current position
        self.end_positions[self._current_position] += 1 #tally current position

    def _parse_move(self,move):
        '''
        Where the action is. Recurses until a move isn't a chance or cc card requiring movement
        '''
        if move in self._cc_squares:
            result = next(self._cc_cards)(move) #calling returned lambda with argument of move (integer representing position)
        elif move in self._ch_squares:
            result = next(self._ch_cards)(move) #ditto
        elif move == 30: return 10 #go to jail square
        else: return move #if here, then move was just a regular old move
        return move if result == 'STAY' else self._parse_move(result) #Only CC and CH cards at this point; recursion if they don't have an action

    def print_end_position_percents(self):
        '''
        helper function prints results pretty-like
        '''
        total_moves = sum(self.end_positions.values())
        print('Total moves: ',total_moves)
        for i,v in sorted(self.end_positions.items(),key=lambda x:x[1],reverse=True):
            print(i,' ',100*v/total_moves,'%')

    def get_n_sided_dice(n,s=2):
        '''
        generate s dice-tuples with n sides (not actual method, doesn't need self argument)
        '''
        if s < 2:
            raise ValueError('Monopoly can only be played with two or more dice.') #doubles rule will break if less than s
        return tuple(tuple(i for i in range(1,n+1)) for j in range(0,s))
