function addconf(arg) {
	var domain = $('#domain').val();
	var backend = $('#backend').val();
	$.post("/addconf/", { domain: domain,backend:backend },
			   function(arg){
                           $("#confview").html('<pre  id="conf" contenteditable="true">'+arg);
			   });
}

function pushconf(arg) {
	var res = $('#conf').text();
	var file_name = $('#file_name').val();
        var serverip = $('#serverip').val()
	$.post("/pushconf/", { conf_file: res,file_name:file_name,serverip:serverip},
			   function(arg){
                           if(arg.search("success") != -1 ){alert('推送加载成功')}
                           else{alert('配置文件有误，请检查！')}
			   });
}
