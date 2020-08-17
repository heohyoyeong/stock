function categoryChange(selectbox,companyDictionary) {

  var companyList = companyDictionary[selectbox.value];

  var nextSelectBox = document.getElementById("machingstock");

  nextSelectBox.options.length = 0;
 
  for (x in companyList) {
    var optionElement = document.createElement("option");
    optionElement.value = companyList[x];
    optionElement.innerHTML = companyList[x];
    nextSelectBox.appendChild(optionElement);
  } 
}



