# Caleb's Decoding Program, Feb 14, 2016
import operator

#Date Pattern that we use to decode / encode, should be all numeric, any length
pattern = '09192016'


#either operator.add or operator.sub if you are going up or down in the alphabet
updown = operator.sub


#this can ether be clear text, to encode, or coded text to decode
string_in = """
Dnba Eamkb,
Spbjub os mprpg xklu. J qqpf eod fwlozkd xva xitot jom K
cbt't fbrv tp yen zxw ahgiw gxt Cixibuvcs. Uu hnmy mefv
ods wcmfy sndagt, J'rl lbun ypa Fjmlqn. Eu yxv tpox chju
hqus mrjomra xgnct oqr Dnrrtcoat?


   Mhxtc (Reukr) 
"""


#the rest of this stuff should just work
upper = range(65,90)
lower = range(97,122)
if updown is operator.sub : opposite = operator.add
else : opposite = operator.sub
string_out = ''
pattern_position = 0
for c in string_in:
	if c.isalpha():
	 	if c.isupper() :
			n_out = updown(ord(c), int(pattern[pattern_position]))
			if n_out in upper : c_out = chr(n_out)
			else: c_out = chr(opposite(n_out, 26))
		if c.islower():
			n_out = updown(ord(c), int(pattern[pattern_position]))
			if n_out in lower : c_out = chr(n_out)
			else: c_out = chr(opposite(n_out, 26))
	
		#append our character to the string out
		string_out += c_out
		
		#check to see if we are at the end of the pattern
		pattern_position += 1
		if pattern_position == len(pattern): pattern_position = 0
	else:
		#we had a non alphabet character, so we just copy it over unchanged
		string_out += c

print string_out
