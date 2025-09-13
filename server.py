from flask import Flask
from flask import render_template, send_from_directory, request, redirect, send_file
import model



app = Flask(__name__)

characters = []
list_a = []

#opens muppet data file, to preserve the commas in the data all commas were changed to |, and have to be changed back here
data_file = open('muppets.data','r', encoding = 'utf-8')

for line in data_file:
    character = line.strip("\n")
    character = character.split(',')
    name = character[0]
    actor = character[1]
    actor = actor.replace("|", ",")
    desc = character[2]
    desc = desc.replace("|", ",")
    image = character[3]
    image = image.replace("|", ",")
    
    creature = model.Muppet(name, actor, desc, image)
    
    characters.append(creature)

    
#opens index (home page)
@app.route("/", methods=["GET", "POST"])
def home():
  return render_template("index.html")





#opens result page for search/clicking on a muppet
@app.route("/result", methods=["GET", "POST"])
def result():
  search = request.form['character']
  try:
    character_id = model.search(search,characters)
  except: 
    error = "That is not a character's name"
    return render_template("error.html", error = error)
  else:
    name = model.Muppet.get_name(characters[character_id])
    actor = model.Muppet.get_actor(characters[character_id])
    desc = model.Muppet.get_desc(characters[character_id])
    image = model.Muppet.get_image(characters[character_id])
    return render_template("result.html",character_id=character_id, name=name, actor=actor, desc=desc, image=image)
  
  

#opens random result page
@app.route("/random", methods=["GET", "POST"])
def result_random():
    total = len(characters)
    character_id = model.random_result(total)
    name = model.Muppet.get_name(characters[character_id])
    actor = model.Muppet.get_actor(characters[character_id])
    desc = model.Muppet.get_desc(characters[character_id])
    image = model.Muppet.get_image(characters[character_id])
    return render_template("result.html",character_id=character_id, name=name, actor=actor, desc=desc, image=image)
  
  
  
#adds muppet to list and opens list
@app.route("/add_list", methods=["GET", "POST"])
def add_list():
    character_id = int(request.form['character_id'])
    if characters[character_id] not in list_a:
      list_a.append(characters[character_id])
      return model.list_output(list_a)
    else:
      return model.list_output(list_a)
  
  
  
#opens list
@app.route("/list", methods=["GET", "POST"])
def show_list():
  if len(list_a)!= 0:
    return model.list_output(list_a)
  else: 
    error = "There is nothing in your list"
    return render_template("error.html",error=error)
  
 

#saves a csv of your list
@app.route("/save_csv", methods=["GET", "POST"])
def save_csv():
  
  try:
    save_file = open('muppet_list.csv', 'w')
    save_file.write(',Name, Actors, Description, Image Link\n')
    k = 0
    
    csv_list = model.sort(list_a)
    while k < len(csv_list):
          name = model.Muppet.get_name(csv_list[k])
          actor = model.Muppet.get_actor(csv_list[k])
          desc = model.Muppet.get_desc(csv_list[k])
          image = model.Muppet.get_image(csv_list[k])
          
          save_file.write(f'{k+1}.,{name},"{actor}","{desc}", "{image}"\n')
          
          k+=1
    
    save_file.close()
    path = 'muppet_list.csv'
    return send_file(path, as_attachment=True)

  except Exception as error:
    return render_template("error.html", error = error)
  
  
  
#deletes a muppet from your list
@app.route("/delete_item", methods=["GET", "POST"])
def delete_item():
  try:
    character_id = int(request.form['character_id'])
    list_a.pop(character_id)
    return model.list_output(list_a)
  except:
    error = "The character could not be deleted"
    return render_template("error.html", error = error)
  
  
  
#prints the list
@app.route("/print", methods=["GET", "POST"])
def print():
  return model.print_list(list_a)
  
  
  
#shows a directory of all muppets
@app.route("/all_muppets", methods=["GET", "POST"])
def all(): 
  names, photos = model.names_and_photos(characters)
  return model.directory(names, photos)
  

  
  
if __name__ == "__main__":
  app.run()
