function postman(arg) {
	var testurl = $('#domain').val();
	$.get("/postmanapi/", { testurl: testurl },
			   function(myarg){
			arg=JSON.stringify(myarg,null, '  ');
         $("#confview").html('<pre><code id="json">'+arg+'</code></pre>');
			   });
}
