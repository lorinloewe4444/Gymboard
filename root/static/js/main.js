//alert("this is from js");

const faecher =['Biologie', 'BG', 'Chemie', 'Chinastudien', 'Deutsch', 'Englisch', 'WR',
'Französisch', 'Geschichte', 'Geografie', 'Griechisch', 'Italienisch', 'Informatik',
'Latein', 'Mathematik', 'Musik', 'Physik', 'PAM', 'PPP', 'Russisch', 'Spanisch', 'Sport'];

const sub = [['Einsprachig', 'Immersion', 'EF', 'GF', 'SF'], ['GF', 'SF', 'EF'], ['Einsprachig', 'Immersion', 'GF', 'SF'], [], ['Gym1', 'Gym2', 'Gym3', 'Gym4'], ['EF', 'GF', 'SF'], ['EF', 'EWR', 'SF'], [], ['Einsprachig', 'Immersion', 'EF'], ['Gym1', 'Gym2', 'Gym4', 'EF'], [], ['GF', 'SF', 'fakultativ'], ['Gym1', 'Gym2', 'fakultativ(archiv)', 'EF'], [], ['Gym1', 'Gym2', 'Gym3', 'Gym4'], ['fak', 'Gym1', 'Gym2', 'Gym3', 'Gym4', 'EF'], ['Gym2', 'Gym3', 'Gym4'], ['AM', 'Physik'], ['Philosophie', 'Psychologie', 'Pädagogik'], [], [], ['EF']];




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


function fillLvlOne(subjectIndex){
  const content = sub[subjectIndex];
  var ul = document.getElementById("listLvl1");
  ul.innerHTML = ''//clears the ul
  for (subIndex in content){
    var li = document.createElement("li");
    li.appendChild(document.createTextNode(sub[subjectIndex][subIndex]));
    li.setAttribute("id", "SubOne:"+subIndex);
    li.setAttribute("class", "subOne");
    ul.appendChild(li);
  }
}

loadMainSubs();

var subjects = document.getElementsByClassName("subject");

var applyClickSubjects = function() {
    var id = this.getAttribute("id");
    const subjectIndex = id.split(":")[1];

    fillLvlOne(subjectIndex);
};

for (var i = 0; i < subjects.length; i++) {
    subjects[i].addEventListener('click', applyClickSubjects, false);
}
