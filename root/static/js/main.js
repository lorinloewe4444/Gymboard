//alert("this is from js");


var nodePath = []

async function getAndLoadChildren (parentId) {
  try {
    const root = 'test' + parentId;
    const response = await fetch(root);
    const data = await response.json();
    fillSubListNew(data);
  } catch (e) {
    console.log("Async func catch");
  }
}

async function loadMainSubs (parentId) {
  try {
    const root = 'test0';
    const response = await fetch(root);
    const data = await response.json();
    var ul = document.getElementById("listSubjects");
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
  for (i in content[0]){ // für Ordner/Knoten // hat problem
    const child = content[0][i];
    var li = document.createElement("li");
    li.appendChild(document.createTextNode(child[1]));
    li.style.backgroundColor = "blue";// provisorische line
    li.setAttribute("id", "node:" + child[0]);
    li.setAttribute("class", "node");
    ul.appendChild(li);
  }

  for (i in content[1]){ // für Files
    const child = content[1][i];
    var li = document.createElement("li");
    li.appendChild(document.createTextNode(child[1]));
    li.style.backgroundColor = "red";// provisorische line
    li.setAttribute("id", "file:" + child[0]);
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
    files[i].addEventListener('click', fileClicked, false);
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
  console.log("file was clicked, id is:");
  console.log(this.getAttribute("id"));
}


var nodeClicked = function(){
  var id = this.getAttribute("id");
  const nodeIndex = id.split(":")[1];
  nodePath.push(nodeIndex);
  console.log(nodePath);
  getAndLoadChildren(nodeIndex);
}

var mainSubClicked = function() {
    var id = this.getAttribute("id");
    const subjectIndex = id.split(":")[1];
    nodePath = [subjectIndex];
    getAndLoadChildren(subjectIndex);
};
