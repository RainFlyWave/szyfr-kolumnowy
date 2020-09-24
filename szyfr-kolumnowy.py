# Szyfrowanie kolumnowe jest jedną z metod szyfrowania przestawieniowego, polegającego na
# zmianie kolejności znaków w szyfrowanym tekście. W tej metodzie jest wykorzystywana
# tabela o dodatniej liczbie wierszy równej k. Liczba k jest nazywana kluczem. Wiersze i kolumny
# tabeli są numerowane liczbami naturalnymi, począwszy od 1. Znaki tekstu, który ma być
# zaszyfrowany, wpisujemy do kolejnych kolumn tabeli, zaczynając od jej lewego górnego rogu.
# W kolumnach nieparzystych znaki wpisujemy od góry do dołu, a w parzystych od dołu do góry.
# Puste miejsca w ostatniej rozpoczętej kolumnie wypełniamy znakiem „_” oznaczającym spację.
# Następnie odczytujemy kolejne wiersze od góry do dołu (każdy z nich od lewej do prawej),
# w wyniku czego uzyskujemy szyfrogram.
# Przykład: dla klucza k=3 i tekstu MATURA_Z_INFORMATYKI budujemy tabelę:

# 									M A _ F O Y K
# 									A R Z N R T I
# 									T U _ I M A _

# i otrzymujemy szyfrogram MA_FOYKARZNRTITU_IMA_. 


code = "MA_FOYKARZNRTITU_IMA_"	#	tekst przeznaczony do enkrypcji
key = 3					#	key w jakim tekst został zacodeowany
code = list(code)			#	zamieniamy stringa na tablice	

#	liczymy ilość znaków w tablicy code
# 	liczbę dzielimy odrazu bez części dziesiętnej 
# 	i konwertujemy dla pewności w inta
#	ułatwi nam to potem deklaracje poniższych tablic
#	tej zmiennej używamy do określania ilości przebiegów pętli
number_of_chars = int(len(code)//key) 	 
		

#	deklarujemy 2 tablice

#	w tablicy 'temporary' tworzymy tyle tablic
# 	ile wynosi wartosc zmiennej 'key'

#	'temporary' wypełniana jest ciągiem 0 aby nie było problemu
# 	z przypisaniem indeksu

#	tablica 'connect_letter' zawiera w sobie tyle tablic 
#	ile wynosi zmienna 'number_of_chars'

#	tablica 'temporary' będzie użyta do posortowania liter
# 	tablica 'connect_letter' będzie użyta do połączenia liter w zdania

temporary = [  [0 for i in range(number_of_chars)]for j in range(key) ]
connect_letter = [ [] for i in range(number_of_chars) ]

for i in range(key):
	for j in range(number_of_chars):
		temporary[i][j] = code[j] 	#	wszystkie litery wrzucamy do tablicy 
									#	dwuwymiarowej

	del code[0:number_of_chars]		# 	co każdy przebieg pętli usuwamy 
									#	z tablicy 'code' wartości zapisane przez
									#	nas do tablicy 'temporary'




for j in range(number_of_chars):	
	for i in range(key):
		connect_letter[j].append(temporary[i][j])	#	zapisujemy do tablicy 
													#	posortowane pojedyncze znaki

	if((j+1) % 2 != 0):
		connect_letter[j] = "".join(connect_letter[j])	#	łączymy pojedyncze komórki
														#	tablicy w całe zdania
	else:
		connect_letter[j] = "".join(connect_letter[j][::-1])	# parzyste kolumny łączymy 
																# przy okazji zamnieniając
																# kolejność znaków


dekrypcja = ("".join(connect_letter)).replace("_"," ")	#	łączymy tablice connect_letter w jeden ciąg znaków
														#	przy okazji zamieniamy znak podłogi na spacje  '_' -> ' '
print(dekrypcja)


