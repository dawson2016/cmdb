function auditaction(proname,env,action) {
       // var proname=$(arg).parent().parent().find("td").eq(0).text();
        console.log(proname)
        console.log(env)
        //var proname=$(arg).parent().parent().parent().html();
        //var proenv=$(arg).parent().parent().find("td").eq(1).text();
        //var action=$(arg).attr('id');
	*$.post("/auditapi/", { proname: proname, proenv: env,action:action},
        function(arg1){
		       alert(arg1);
                       location.reload(); 
	});
}


