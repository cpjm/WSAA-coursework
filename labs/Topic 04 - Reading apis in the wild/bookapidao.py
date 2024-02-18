import requests
url="http://andrewbeatty1.pythonanywhere.com/books"
def getAllBooks():
    response = requests.get(url)
    return response.json()

def getBookById(id):
    geturl = url + "/" + str(id)
    response = requests.get(geturl)
    return response.json()

def createBook(book):
    response = requests.post(url,json=book)
    return response.json()

def updateBook(id, bookdiff):
    updateurl = url + "/" + str(id)
    response = requests.put(updateurl, bookdiff)
    return response.json()

def deleteBook(id):
    deleteurl = url + "/" + str(id)
    response = requests.delete(deleteurl)
    return response.json()

if __name__ =="__main__":
    book = {
        'Author':"Test",
        'Title':"Test book title",
        'Price': 123
    }
    bookdiff = {
        'Price': 123
    }
    print(getAllBooks())
    print(getBookById(1))
    print(updateBook(1, jason=bookdiff))
    
    print(createBook(book))

