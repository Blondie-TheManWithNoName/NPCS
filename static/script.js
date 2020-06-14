var slider = document.getElementById("healthRange");
var output = document.getElementById("slider");
if (slider != null)
{

	output.innerHTML = slider.value;

	slider.oninput = function()
	{
	  output.innerHTML = this.value;
	}
}


/*const addData = (data, dbTable) => {
	(dbName == "exhibidor") ? db = requestE.result : db = requestP.result; 
	const transaction = db.transaction([dbName], "readwrite");
	const objectStore = transaction.objectStore(dbName);
	const request = objectStore.add(data);
	request.onsuccess = () =>
	{
		notification("Añadido correctamente.");
		readData(dbName);
	}
	request.onerror = () =>
	{
		notification("Se ha producido un error al añadir.");
	}
}


form.addEventListener("submit", (e) => {
	e.preventDefault();
	const data = {
		name: e.target.name.value,
		sex: e.target.sex.value,
		color: e.target.color.value
		height: e.target.height.value
		health: e.target.health.value
		id: e.target.id.value
		namereg: e.target.namereg.value
	}
	if (e.target.button.dataset.action == "add") addData(data, "npc");
	else if (e.target.button.dataset.action == "update") updateData(data, "npc");

	form.reset();
});
*/


function getDataNpcs (item0, item1, item2, item3, item4, item5, item6) {
	document.getElementById("form").action = "?id=" + item5 + "&namereg=" + item6;
	window.scrollTo(0, 850);
	output.innerHTML = item4;
	form.name.value = item0;
	form.sex.value = item1;
	form.color.value = item2;
	form.height.value = item3;
	form.health.value = item4;
	form.id.value = item5;
	form.namereg.value = item6;

	updateMode();
}

function getDataFaces (item0, item1, item2, item3, item4, item5, item6) {
	document.getElementById("form").action = "?id=" + item0;
	window.scrollTo(0, 775);
	form.id.value = item0;
	form.mouthFile.value = item1;
	form.eyesFile.value = item2;
	form.noseFile.value = item3;
	form.earsFile.value = item4;
	form.hairFile.value = item5	;
	form.color.value = item6;
	
	updateMode();
}

function getDataHairs (item0, item1) {
	document.getElementById("form").action = "?hairFile=" + item0 + "&color=" + item1;
	window.scrollTo(0, 650);
	form.hairFile.value = item0;
	form.color.value = item1;
	
	updateMode();
}

function getDataRegions (item0, item1) {
	document.getElementById("form").action = "?nameReg=" + item0;
	window.scrollTo(0, 650);
	form.nameReg.value = item0;
	form.weather.value = item1;
	
	updateMode();
}


function updateMode ()
{
	form.submit.value = "update";
	form.submit.textContent = "Update";
	document.getElementById("form-title").textContent = "Update";
	form.button_r.textContent = "Cancel";

}


form.button_r.onclick = function () {
	document.getElementById("form-title").textContent = "Create";
	document.getElementById("form").action = "";
	form.submit.value = "create";
	form.submit.textContent = "Create";
	form.button_r.textContent = "Restore";
}

form.submit.onclick = function () {
	// notification("test")
}

if (document.getElementById("notifyType") != null)
{
	console.log(document.getElementById("notifyType").innerHTML)
	if (document.getElementById("notifyType").innerHTML.startsWith("An"))
	{		
		setTimeout(function(){
			document.getElementsByClassName("notify")[0].classList.add("inactive");
		},10000);	
	}
	else
	{
		setTimeout(function(){
			document.getElementsByClassName("notify")[0].classList.add("inactive");
		},2000);	
	}

}

function notification (message)
{
	document.getElementsByClassName("notify")[0].classList.toggle("active");
	var not = document.getElementById("notifyType");
	not.classList.add("succes");
	not.innerHTML = message;

}