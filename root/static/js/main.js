//alert("this is from js");


var nodePath = []



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


async function getAndLoadChildren (parentId) {
  try {
    const root = 'test' + parentId;
    const response = await fetch(root);
    const data = await response.json();
    fillSubListNew(data);
    createPath();
  } catch (e) {
    console.log("Async func catch");
  }
}

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

function createPath(){
  var ul = document.getElementById("nodePath");
  ul.innerHTML = '';
  for (i in nodePath){ // für Files
    const content = nodePath[i];
    var li = document.createElement("li");
    li.appendChild(document.createTextNode(content[1]));
    li.setAttribute("id", "pathNode:" + content[0]);
    li.setAttribute("class", "pathNode");
    ul.appendChild(li);
  }
  addEventToPath();
}

function addEventToPath(){
  const pathNodes = document.getElementById("nodePath").children;
  for (var i = 0; i < pathNodes.length; i++) {
    pathNodes[i].addEventListener('click', pathNodeClicked, false);
  }
}

var pathNodeClicked = function (){
  const id = this.getAttribute("id");
  const index = id.split(":")[1];
  getAndLoadChildren(index);
    // removes old Nodes
  const values = nodePath.map(object => object[0])
  const indexInArray = values.indexOf(index);
  while (nodePath.length-1 > indexInArray){
    nodePath.pop()
  }
}

var fileClicked = function (){
  console.log("file was clicked, id is:");
  console.log(this.getAttribute("id"));

}


var nodeClicked = function(){
  var id = this.getAttribute("id");
  const nodeIndex = id.split(":")[1];
  nodePath.push([nodeIndex, this.innerHTML]);
  console.log(nodePath);
  getAndLoadChildren(nodeIndex);
}

var mainSubClicked = function() {
    var id = this.getAttribute("id");
    const subjectIndex = id.split(":")[1];
    nodePath = [[subjectIndex, this.innerHTML]];
    getAndLoadChildren(subjectIndex);
};
