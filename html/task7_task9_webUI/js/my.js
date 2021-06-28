var IP = "192.168.18.190";
var filepath = "cgi-bin/docker-cgifiles/";

function DI_list_output(){
    var filename = "DIlist.py";
    var url = "http://"+"192.168.18.190"+"/"+filepath+filename;
    var xhr = new XMLHttpRequest();
    xhr.open("GET",url,false);
    xhr.send();
    var output = xhr.responseText;
    document.getElementById("child2").innerHTML=output;
}

function Drun_output(){
    var filename = "Drun.py";
    var xhr = new XMLHttpRequest();
    container = document.getElementsByName("Launch_container")[0].value;
    image = document.getElementsByName("Launch_container_image")[0].value;
    url = "http://"+IP+"/"+filepath+filename+"?"+"Launch_container="+container+"&"+
    "Launch_container_image="+image; 
    xhr.open("GET",url,false);
    xhr.send();
    var output = xhr.responseText;
    document.getElementById("child2").innerHTML=output;
}

function DCrunning_list_output(){
    var filename = "DCrunning.py";
    var xhr = new XMLHttpRequest();
    var url = "http://"+IP+"/"+filepath+filename;
    xhr.open("GET",url,false);
    xhr.send();
    var output = xhr.responseText;
    document.getElementById("child2").innerHTML=output;
}

function DCexec_output(){
    var filename = "DCexec.py";
    var xhr = new XMLHttpRequest();
    container = document.getElementsByName("exec_container")[0].value;
    command = document.getElementsByName("exec_command")[0].value;
    url = "http://"+IP+"/"+filepath+filename+"?"+"exec_container="+container+"&"+
    "exec_command="+command; 
    xhr.open("GET",url,false);
    xhr.send();
    var output = xhr.responseText;
    document.getElementById("child2").innerHTML=output;

}

function DCstop_output(){
    var filename = "DCstop.py";
    var xhr = new XMLHttpRequest();
    container = document.getElementsByName("stop_container")[0].value;
    url = "http://"+IP+"/"+filepath+filename+"?"+"stop_container="+container; 
    xhr.open("GET",url,false);
    xhr.send();
    var output = xhr.responseText;
    document.getElementById("child2").innerHTML=output;
}

function DCstopped_output(){
    var filename = "DCstopped.py";
    var xhr = new XMLHttpRequest();
    var url = "http://"+IP+"/"+filepath+filename;
    xhr.open("GET",url,false);
    xhr.send();
    var output = xhr.responseText;
    document.getElementById("child2").innerHTML=output;
}

function DCremove_output(){
    var filename = "DCremove.py";
    var xhr = new XMLHttpRequest();
    container = document.getElementsByName("remove_container")[0].value;
    url = "http://"+IP+"/"+filepath+filename+"?"+"remove_container="+container; 
    xhr.open("GET",url,false);
    xhr.send();
    var output = xhr.responseText;
    document.getElementById("child2").innerHTML=output;
}

function DIremove_output(){
    var filename = "DIremove.py";
    var xhr = new XMLHttpRequest();
    image = document.getElementsByName("remove_image")[0].value;
    url = "http://"+IP+"/"+filepath+filename+"?"+"remove_image="+image; 
    xhr.open("GET",url,false);
    xhr.send();
    var output = xhr.responseText;
    document.getElementById("child2").innerHTML=output;
}

function DCstart_output(){
    var filename = "DCstart.py";
    var xhr = new XMLHttpRequest();
    image = document.getElementsByName("start_container")[0].value;
    url = "http://"+IP+"/"+filepath+filename+"?"+"start_container="+container; 
    alert(url);
    xhr.open("GET",url,false);
    xhr.send();
    var output = xhr.responseText;
    document.getElementById("child2").innerHTML=output;
}











