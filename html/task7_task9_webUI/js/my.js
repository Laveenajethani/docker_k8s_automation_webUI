function DCrunning_list_output(){
    var xhr = new XMLHttpRequest();
    xhr.open("GET","http://192.168.214.190/cgi-bin/docker-cgifiles/DCrunning.py",false);
    xhr.send();
    var output = xhr.responseText;
    document.getElementById("child2").innerHTML=output;
    
}

function DIpull_output(){
    var xhr = new XMLHttpRequest();
    xhr.open("GET","http://192.168.214.190/cgi-bin/docker-cgifiles/DIpull.py",false);
    xhr.send();
    var output = xhr.responseText;
    document.getElementById("child2").innerHTML=output;
    
}


function DI_list_output(){
    var xhr = new XMLHttpRequest();
    xhr.open("GET","http://192.168.214.190/cgi-bin/docker-cgifiles/DIlist.py",false);
    xhr.send();
    var output = xhr.responseText;
    document.getElementById("child2").innerHTML=output;
    
}


