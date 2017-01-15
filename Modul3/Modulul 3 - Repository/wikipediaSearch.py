import wikipedia
import sys


def search(*args): #pot avea: 1 subiect / 1 subiect+1/mai multe proprietati
	if len(args)==1:
		try:
			foundPages=wikipedia.search(args[0])
			print(foundPages)
			foundPages=wikipedia.summary(foundPages, sentences="2")
			encodedRes=foundPages.encode("utf-8", 'replace')
			print (encodedRes.decode("ascii", 'ignore'))
		except wikipedia.exceptions.DisambiguationError as e:
			pagini=e.options			
			paginaAleasa=pagini[0]
			foundPages=wikipedia.summary(paginaAleasa, sentences="2")
			encodedRes=foundPages.encode("utf-8", 'replace')
			print (encodedRes.decode("ascii", 'ignore'))
		except wikipedia.exceptions.PageError:
				print("404")
	elif len(args)>1:
		try:
			foundPages=wikipedia.search(args[0])
			print(foundPages) #folosesc si wikipedia.search deoarece face implicit si autosuggest
						
			if len(foundPages)>0:
						
				mypage=wikipedia.WikipediaPage((foundPages[0]))
				content=mypage.content
				#print(content.encode("utf-8", 'replace'))
				findItem=content.find(args[1]) #presupun ca la linia de comanda primesc 2 argumente: subiect si proprietate a subiectului ( as putea insa sa caut si mai multe proprietati ale subiectului)
				#print(findItem)
				containingSentenceStart=content.rfind(".",0,findItem)
				#print("last dot before searched word",containingSentenceStart)
				containingSentenceEnd=content.find(".",findItem, len(content))
				sentence=""
				for i in range(containingSentenceStart, containingSentenceEnd+1):
					sentence+=content[i]
				print(sentence.encode("utf-8", 'replace').decode("ascii", 'ignore'))
			else:
				print("No results")
		except Exception as e: 
			print("error",str(e))

	

search("Obama","birth")

#probleme: daca nu gasesc  pagina corecta la dezambiguizare
#selectez prima aparitie a proprietatii din articol : daca nu aflu rasp. dorit?
#splitarea dupa punct spliteaza si prescurtarile