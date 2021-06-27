function cmd_output(){
	var xhr = new XMLHttpRequest();
	xhr.open("GET","http://192.168.43.236/cgi-bin/DCstopped.py",false);
	xhr.send();
	var output=xhr.responseText();
    document.getElementsById("child2").innerHTML=output;

}

