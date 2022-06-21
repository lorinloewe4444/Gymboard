//alert("this is from js");

const faecher =['Biologie', 'BG', 'Chemie', 'Chinastudien', 'Deutsch', 'Englisch', 'WR',
'Französisch', 'Geschichte', 'Geografie', 'Griechisch', 'Italienisch', 'Informatik',
'Latein', 'Mathematik', 'Musik', 'Physik', 'PAM', 'PPP', 'Russisch', 'Spanisch', 'Sport'];

const sub = [['Einsprachig', 'Immersion', 'EF', 'GF', 'SF'], ['GF', 'SF', 'EF'], ['Einsprachig', 'Immersion', 'GF', 'SF'], [], ['Gym1', 'Gym2', 'Gym3', 'Gym4'], ['EF', 'GF', 'SF'], ['EF', 'EWR', 'SF'], [], ['Einsprachig', 'Immersion', 'EF'], ['Gym1', 'Gym2', 'Gym4', 'EF'], [], ['GF', 'SF', 'fakultativ'], ['Gym1', 'Gym2', 'fakultativ(archiv)', 'EF'], [], ['Gym1', 'Gym2', 'Gym3', 'Gym4'], ['fak', 'Gym1', 'Gym2', 'Gym3', 'Gym4', 'EF'], ['Gym2', 'Gym3', 'Gym4'], ['AM', 'Physik'], ['Philosophie', 'Psychologie', 'Pädagogik'], [], [], ['EF']];


async function getAndLoadChildren (parentId) {
  try {
    const root = 'test' + parentId;
    const response = await fetch(root);
    const data = await response.json();
    console.log(data);
    fillSubListNew(data);
  } catch (e) {
    console.log("Async func catch");
  }
}



function loadMainSubs() {
  var ul = document.getElementById("listSubjects");
  for (subjectIndex in faecher){
  var li = document.createElement("li");
  li.appendChild(document.createTextNode(faecher[subjectIndex]));
  li.setAttribute("id", "subject:"+subjectIndex);
  li.setAttribute("class", "subject");
  ul.appendChild(li);
  }
}

loadMainSubs();



function fillSubListNew(content){
  var ul = document.getElementById("subList");
  ul.innerHTML = ''//clears the ul
  console.log("of content")
  console.log(content)

  for (i in content[0]){ // für Ordner/Knoten
    const child = content[0][i];
    var li = document.createElement("li");
    li.appendChild(document.createTextNode(child[1]));
    li.setAttribute("id", child[0]);
    li.setAttribute("class", "node");
    ul.appendChild(li);
  }
  for (i in content[1]){ // für Ordner/Knoten
    const child = content[1][i];
    var li = document.createElement("li");
    li.appendChild(document.createTextNode(child[1]));
    li.setAttribute("id", child[0]);
    li.setAttribute("class", "file");
    ul.appendChild(li);
  }

}

//inaktiv
function fillSubList(subjectIndex){
  const content = sub[subjectIndex];
  var ul = document.getElementById("subList");
  ul.innerHTML = ''//clears the ul

  for (subIndex in content[0]){
    var li = document.createElement("li");
    li.appendChild(document.createTextNode(sub[subjectIndex][subIndex]));
    li.setAttribute("id", "SubOne:"+subIndex);
    li.setAttribute("class", "subOne");
    ul.appendChild(li);
  }
}


var subjects = document.getElementsByClassName("subject");


var applyClickSubjects = function() {
    var id = this.getAttribute("id");
    const subjectIndex = id.split(":")[1];
    getAndLoadChildren(10); // 10 muss durch id ersetzt werden, dafür muss aber zuerst die Datenbank ergäntzt werden.
};

for (var i = 0; i < subjects.length; i++) {
    subjects[i].addEventListener('click', applyClickSubjects, false);
}
