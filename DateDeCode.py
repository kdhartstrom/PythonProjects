# Caleb's Decoding Program, Feb 14, 2016

#Date Pattern that we use to decode / encode, should be all numeric, any length
pattern = '2182016'

#either 'add' or 'subtract'
method ='add'

#this can ether be clear text, to encode, or coded text to decode
string_in = """
Dear Caleb,
I just wanted you to know that I'm pleased with how you are learning to be a responsible man, 
and I appreciate it when you show kindness to your brothers and sisters.
Love,
Your Dad
"""


#the rest of this stuff should just work
string_out = ''
pattern_position = 0
for c in string_in:
	#change our character to an ascii code
	n = ord(c)
	# test to see if it's a letter
	if 67 <= n <= 90 or 97 <= n <= 122:
		if method == 'subtract' :
			n_out = n - int(pattern[pattern_position])
			#check if we still have an alphabet character
			if 67 <= n_out <= 90 or 97 <= n_out <= 122 :
				c_out = chr(n_out)
			else:
				#we have to start the alphabet over because we are out of range
				c_out = chr(n_out + 26)
				
		if method == 'add' :
			n_out = n + int(pattern[pattern_position])
			#check if we still have an alphabet character
			if 67 <= n_out <= 90 or 97 <= n_out <= 122 :
				c_out = chr(n_out)
			else:
				#we have to start the alphabet over because we are out of range
				c_out = chr(n_out - 26)

		#append our character to the string out
		string_out += c_out
		
		#check to see if we are at the end of the pattern
		pattern_position += 1
		if pattern_position == len(pattern): pattern_position = 0
	else:
		#we had a non alphabet character, so we just copy it over unchanged
		string_out += c

print string_out
