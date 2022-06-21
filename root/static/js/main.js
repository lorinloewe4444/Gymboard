//alert("this is from js");

const faecher =['Biologie', 'BG', 'Chemie', 'Chinastudien', 'Deutsch', 'Englisch', 'WR',
'Französisch', 'Geschichte', 'Geografie', 'Griechisch', 'Italienisch', 'Informatik',
'Latein', 'Mathematik', 'Musik', 'Physik', 'PAM', 'PPP', 'Russisch', 'Spanisch', 'Sport'];

const sub = [['Einsprachig', 'Immersion', 'EF', 'GF', 'SF'], ['GF', 'SF', 'EF'], ['Einsprachig', 'Immersion', 'GF', 'SF'], [], ['Gym1', 'Gym2', 'Gym3', 'Gym4'], ['EF', 'GF', 'SF'], ['EF', 'EWR', 'SF'], [], ['Einsprachig', 'Immersion', 'EF'], ['Gym1', 'Gym2', 'Gym4', 'EF'], [], ['GF', 'SF', 'fakultativ'], ['Gym1', 'Gym2', 'fakultativ(archiv)', 'EF'], [], ['Gym1', 'Gym2', 'Gym3', 'Gym4'], ['fak', 'Gym1', 'Gym2', 'Gym3', 'Gym4', 'EF'], ['Gym2', 'Gym3', 'Gym4'], ['AM', 'Physik'], ['Philosophie', 'Psychologie', 'Pädagogik'], [], [], ['EF']];


async function getAndLoadChildren (parentId) {
  console.log("parentId is:");
  console.log(parentId);
  try {
    const root = 'test' + parentId;
    const response = await fetch(root);
    const data = await response.json();
    console.log(data);
    console.log("HEY");
    fillSubListNew(data);
    console.log("BYE");
  } catch (e) {
    console.log("Async func catch");
  }
}

async function loadMainSubs (parentId) {
  try {
    const root = 'test' + 0;
    const response = await fetch(root);
    const data = await response.json();
    var ul = document.getElementById("listSubjects");
    console.log(data);
    for (subjectIndex in data[0]){
      subjectContent = data[0][subjectIndex];
      var li = document.createElement("li");
      li.appendChild(document.createTextNode(subjectContent[1]));
      li.setAttribute("id", "subject:"+subjectContent[0]);
      li.setAttribute("class", "subject");
      ul.appendChild(li);

    }
    var subjects = document.getElementsByClassName("subject");
    for (var i = 0; i < subjects.length; i++) {
        subjects[i].addEventListener('click', mainSubClicked, false);
    }

  } catch (e) {
    console.log("Fail in LoadMainSubs");
  }
}

loadMainSubs();



function fillSubListNew(content){
  var ul = document.getElementById("subList");
  ul.innerHTML = '';//clears the ul
  console.log("of content");
  console.log(content);

  for (i in content[0]){ // für Ordner/Knoten // hat problem
    const child = content[0][i];
    var li = document.createElement("li");
    li.appendChild(document.createTextNode(child[1]));
    li.style.backgroundColor = "yellow";// provisorische line
    li.setAttribute("id", child[0]);
    li.setAttribute("class", "node");
    ul.appendChild(li);
  }

  for (i in content[1]){ // für Ordner/Knoten
    const child = content[1][i];
    var li = document.createElement("li");
    li.appendChild(document.createTextNode(child[1]));
    li.style.backgroundColor = "red";// provisorische line
    li.setAttribute("id", child[0]);
    li.setAttribute("class", "file");
    ul.appendChild(li);
  }
  addEventToSubs();
}

function addEventToSubs(){
  const nodes = document.getElementsByClassName("node");
  for (var i = 0; i < nodes.length; i++) {
    nodes[i].addEventListener('click', nodeClicked, false);
  }
  const files = document.getElementsByClassName("file");
  for (var i = 0; i < files.length; i++) {
    nodes[i].addEventListener('click', fileClicked, false);
  }




}

/* Veraltet
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
*/

var fileClicked = function (){
  console.log("file was clicked");
}


var nodeClicked = function(){
  console.log("node clicked");
  console.log(this);
  var id = this.getAttribute("id");
  const nodeIndex = id.split(":")[1];
  console.log(nodeIndex);
  getAndLoadChildren(nodeIndex);
}

var mainSubClicked = function() {
    console.log("This: ")
    console.log(this);
    var id = this.getAttribute("id");
    const subjectIndex = id.split(":")[1];
    console.log("Index is is");
    console.log(subjectIndex);
    console.log(id);
    getAndLoadChildren(subjectIndex);
};
