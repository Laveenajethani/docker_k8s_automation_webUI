var IP = "192.168.99.101";
var filepath = "cgi-bin/k8s-cgifiles/";

function PODlist_output(){
    var filename = "PODlist.py";
    var xhr = new XMLHttpRequest();
    ns = document.getElementsByName("ns_name")[0].value;
    url = "http://"+IP+"/"+filepath+filename+"?"+"ns_name="+ns; 
    xhr.open("GET",url,false);
    xhr.send();
    var output = xhr.responseText;
    document.getElementById("child2").innerHTML=output;
}

function CreateNS_output(){
    var filename = "CreateNS.py";
    var xhr = new XMLHttpRequest();
    ns = document.getElementsByName("create_ns_name")[0].value;
    url = "http://"+IP+"/"+filepath+filename+"?"+"create_ns_name="+ns; 
    alert(url);
    xhr.open("GET",url,false);
    xhr.send();
    var output = xhr.responseText;
    document.getElementById("child2").innerHTML=output;
}

function CreateDeploy_output(){
    var filename = "CreateDeploy.py";
    var xhr = new XMLHttpRequest();
    ns = document.getElementsByName("CD_ns_name")[0].value;
    deploy = document.getElementsByName("CD_deploy_name")[0].value;
    image = document.getElementsByName("CD_image_name")[0].value;
    url = "http://"+IP+"/"+filepath+filename+"?"+"CD_ns_name="+ns+"&"+"CD_deploy_name="+deploy+"&"+"CD_image_name="+image; 
    alert(url);
    xhr.open("GET",url,false);
    xhr.send();
    var output = xhr.responseText;
    document.getElementById("child2").innerHTML=output;
}