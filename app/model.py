import random


class Muppet:
    
    #initialization
    def __init__(self, name, actor, desc, image):
        self.__name = name
        self.__actor = actor
        self.__desc = desc
        self.__image = image
        
    #getters
    
    def get_name(self):
        return self.__name
    
    def get_actor(self):
        return self.__actor
    
    def get_desc(self):
        return self.__desc
    
    def get_image(self):
        return self.__image


#returns lower cased names for search
def get_names(characters):
    
    names = []
    
    for a in range(len(characters)):
        name = Muppet.get_name(characters[a])
        name = name.lower()
        
        names.append(name)
    
    return names
 

#returns name and photo for directory
def names_and_photos(characters):
    
    names = []
    photos = []
    
    for a in range(len(characters)):
        name = Muppet.get_name(characters[a])
        photo = Muppet.get_image(characters[a])
        names.append(name)
        photos.append(photo)
    
    return names, photos
    
    
#searchs a muppet (the general search function)
def search(name, characters):
    names = get_names(characters)
    test = False
    while test == False:
        search = name.lower()
        
        if search in names:
            test = True
            
        else: 
            raise Exception
    
    n = len(names)
    low = 0
    high = n
    mid_n = (low+high)//2
    result = names[mid_n]
    
    while result != search:
        
        mid_n = (low+high)//2
        
        result = names[mid_n]
        
        if search > result:
            low = mid_n
    
        elif search < result:
            high = mid_n
        
    index = mid_n
    return index

  
#gives random muppet id based on how many muppets there are
def random_result(total):
  upper = total-1
  info_id = random.randint(0,upper)
  return info_id


#sorts list, is used to sort your list as you make it
def sort(my_list):
    
    sorting = get_names(my_list)
    
    unordered = list(sorting)
    
    n = len(sorting)
    
    for k in range(1,n):
        
        element = sorting[k]
        j = k-1
        while j >= 0 and element < sorting[j]:
            sorting[j+1] = sorting[j]
            j-= 1
        sorting[j+1] = element
        
    #the original positition of the elements in the sorted list
    order = []
    for a in sorting:
        m = unordered.index(a)
        order.append(m)
        
    #putting the original elements in the sorted order
    ordered = []
    for num in order: 
        ordered.append(my_list[num])
        
    return ordered




#show list page html
def list_output(list_a):
    k = 0
    html = ''
    html += '<html>\n'
    html += '<head>\n'
    html += '<title>Muppet Characters</title>\n'
    html += '<link rel="stylesheet" type="text/css" href="static/style.css">\n'
    html += '<script src="https://kit.fontawesome.com/b1efef281e.js" crossorigin="anonymous"></script>\n'
    html += '</head>\n'
    
    html += '<div class="topnav">\n'
    html += '<a href="/closed"> <i class="fa-solid fa-house"></i> Sesame Street Character Search  </a> \n'
    html += '<a id = "list" class="active" href="/list"><i class="fa-solid fa-list"></i> Show List </a> \n'
    html += '<a href="/random"><i class="fa-solid fa-shuffle"></i> Random Muppet </a> \n'
    html += '<a href="/all_muppets"><i class="fa-regular fa-address-book"></i> All Muppets </a>'
    html += '<form method="POST" action="result"> \n'
    html += '<button type="submit" id="search"> \n'
    html += '<i class="fa-solid fa-magnifying-glass"></i> \n'
    html += '</button> \n'
    html += '<input type="text" name="character" placeholder="Search by name..." /> \n'
    html += '</form> \n'
    html += '</div> \n'
    
    html += '<div class="main">'
    html += '<body>\n'
    
    html += '<form method="POST" action="save_csv">'
    html += '<button type="submit" id ="csv">'
    html += 'Save as CSV <i class="fa-solid fa-file-arrow-down"></i>'
    html += '</button>'
    html += '</form>'
    
    html += '<form method="POST" action="print">'
    html += '<button type="submit" id ="print">'
    html += 'Print <i class="fa-solid fa-print"></i>'
    html += '</button>'
    html += '</form>'
    html += '<br>'
    html += '<hr>'
    
    list_a = sort(list_a)
    while k < len(list_a):
        name = Muppet.get_name(list_a[k])
        actor = Muppet.get_actor(list_a[k])
        desc = Muppet.get_desc(list_a[k])
        image = Muppet.get_image(list_a[k])
        character_id = k
        
        
        html += '<div class="row">'
        html += '<div class="column" style="width: 5%; text-align: center;">\n'
        html += '<p>\n'
        html += f'<form method="POST" action="delete_item">\n'
        html += f'<input type="hidden" id="character_id" name="character_id" value="{character_id}">\n'
        html += '<button type="submit" id ="trash"/>\n'
        html += '<i class="fa-solid fa-trash"></i>\n'
        html += '</button>\n'
        html += '</form>\n'
        html += '</p>\n'
        html += '</div>\n'
        html += '<div class="column" style="width: 15%; text-align: center">\n'
        html += '<p>\n'
        html += f'<img src="{image}" class="img-responsive" alt="picture of {name}" width = "90%"/>\n'
        html += '</p>\n'
        html += '</div>\n'
        
        html += '<div class="column" style="width: 70%; float: right;">\n'
        html += '<p>\n'
        html += f'<b>{k+1}.</b> {name}\n'
        html += '<br>'
        html += f'<b>Actors:</b> {actor}\n'
        html += '<br>'
        html += f'<b>Description:</b> {desc}\n'
        html += '</p>\n'
        html += '</div>'
        html += '</div>'
        
        k+=1
  
    html += '</body>\n'
    html += '</div>\n'
    html += '</html>\n'
    
    return html
  
  
  
#print list page html  
def print_list(list_a):
  k = 0
  html = ''
  html += '<html>\n'
  html += '<head>\n'
  html += '<LINK rel="stylesheet" type"text/css" href="static/print.css" media="print">\n'
  html += '<link rel="stylesheet" type="text/css" href="static/style.css">\n'
  html += '<script src="https://kit.fontawesome.com/b1efef281e.js" crossorigin="anonymous"></script>\n'
  
  html += '</head>\n'
    
  html += '<div class="main">\n'
  html += '<body>\n'
    
  html += '<div class = "noprint">\n'
  html += '<div class="topnav">\n'
  html += '<a href="/closed"> <i class="fa-solid fa-house"></i> Sesame Street Character Search  </a> \n'
  html += '<a id = "list" class="active" href="/list"><i class="fa-solid fa-list"></i> Show List </a> \n'
  html += '<a href="/random"><i class="fa-solid fa-shuffle"></i> Random Muppet </a> \n'
  html += '<a href="/all_muppets"><i class="fa-regular fa-address-book"></i> All Muppets </a>'
  html += '<form method="POST" action="result"> \n'
  html += '<button type="submit" id="search"> \n'
  html += '<i class="fa-solid fa-magnifying-glass"></i> \n'
  html += '</button> \n'
  html += '<input type="text" name="character" placeholder="Search by name..." /> \n'
  html += '</form> \n'
  html += '</div>\n'
  html += '<form>\n'
  html += '<input type="button" id = "printer" value="Print me!" onClick="javascript:window.print()"/>\n'
  html += '</form>\n'
  html += '</div>\n'
  html += '<br>\n'
  
  html += '<div class = "container">'
  html += '<div class = "opening">'
  html += '<img src= "https://64.media.tumblr.com/acfe2c92f7ed2232a797b809bfdcaf7f/666ceac4e2748541-8b/s2048x3072/666aaee80cfa6a585626ae31d3ec6761cc32d01a.pnj"  class="img-responsive" id="logo" alt="My Sesame Street List"> ' 
  html += '</div>\n'
  html += '</div>\n'
  
  list_a = sort(list_a)
  while k < len(list_a):
      name = Muppet.get_name(list_a[k])
      actor = Muppet.get_actor(list_a[k])
      desc = Muppet.get_desc(list_a[k])
      image = Muppet.get_image(list_a[k])
      character_id = k
        
        
      html += '<div class="row">'
    
      html += '<div class="column" style="width: 23%; float:left">\n'
      html += '<p>\n'
      html += f'<img src="{image}" class="img-responsive" style ="max-width: 100%;" alt="picture of {name}" />\n'
      html += '</p>\n'
      html += '</div>\n'
        
      html += '<div class="column" style="width: 70%; float:right">\n'
      html += '<p>\n'
      html += f'{k+1}. {name}\n'
      html += '<br>'
      html += f'Actors: {actor}\n'
      html += '<br>'
      html += f'Description: {desc}\n'
      html += '</p>\n'
      html += '</div>'
      html += '</div>'
        
      k+=1
  
  html += '</body>\n'
  html += '</div>\n'
  html += '</html>\n'
    
  return html




#shows directory of all muppets
def directory(names, photos):
  
  alph = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a']
  k=0
  n = 0
  html = ''
  html += '<html>\n'
  html += '<head>\n'
  html += '<title>Muppet Characters</title>\n'
  html += '<link rel="stylesheet" type="text/css" href="static/style.css">\n'
  html += '<script src="https://kit.fontawesome.com/b1efef281e.js" crossorigin="anonymous"></script>\n'
  html += '</head>\n'
    
  html += '<div class="topnav">\n'
  html += '<a href="/"> <i class="fa-solid fa-house"></i> Sesame Street Character Search  </a> \n'
  html += '<a id = "list" href="/list"><i class="fa-solid fa-list"></i> Show List </a> \n'
  html += '<a href="/random"><i class="fa-solid fa-shuffle"></i> Random Muppet </a> \n'
  html += '<a class="active" href="/all_muppets"><i class="fa-regular fa-address-book"></i> All Muppets </a>'
  html += '<form method="POST" action="result"> \n'
  html += '<button type="submit" id="search"> \n'
  html += '<i class="fa-solid fa-magnifying-glass"></i> \n'
  html += '</button> \n'
  html += '<input type="text" name="character" placeholder="Search by name..." /> \n'
  html += '</form> \n'
  html += '</div> \n'
    
  html += '<div class="main">'
  html += '<body>\n'
  html += '<hr>'
  html += '<div class = "letter1">\n'
  html += 'Jump to: \n'
  html += '</div>'
  html += '<div class = "header">\n'
  num = len(alph)-1
  
  while n < num:
    html += '<div class = "letter">\n'
    html += f'<a href="#{alph[n]}">{alph[n]}</a>\n'
    html += '</div>'
    n += 1
  html += '</div>\n'
  n = 0
  
  while n < 25:
    while k < len(names):
      html += '<hr>'
      html += f'<div class = "label" id ="{alph[n]}">\n'
      html += f'{alph[n]}\n'
      html += '</div>'
      

      try:
        html += '<div class = "grid">\n'
        while names[k] < alph[n+1]:
          
          html += '<div class="box">\n'
          html += '<form method="POST" action="result">\n'
          html += f'<input type="hidden" id="character" name="character" value="{names[k]}">\n'
          html += '<button type="submit" id ="photo"> \n'
          html += '<figure>'
          html += f'<img src ="{photos[k]}" class="img-responsive" alt= "Photo of {names[k]}" style ="max-width: 100%">'
          html += f'<figcaption>{names[k]}</figcaption>'
          html += '</figure>'
          html += '</button>\n'
          html += '</form>\n'
          html += '</div>\n'
          k+=1
        html += '</div>'
      except:
        break
        
      finally:
          n+=1

  html += '</body>\n'
  html += '</div>\n'
  html += '</html>\n'

  return html

