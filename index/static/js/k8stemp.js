function addconf(arg) {
	var appname = $('#appname').val();
	var appport = $('#appport').val();
        var webrpc = $('#webrpc').val()
	$.post("/addk8sconf/", { appname: appname,appport:appport,webrpc:webrpc },
			   function(arg){
                           $("#confview").html('<pre  id="conf" contenteditable="true">'+arg);
			   });
}

