$("table tbody tr").each(function(){
	var status=$(this).children('td:eq(4)').text();
	if (status==1){
		$(this).children('td:eq(4)').html("<button id=1 onclick=\"openshutport(this)\" type=\"button\" class=\"btn btn-danger btn-xs\">关闭</button>");	
	}
	else if (status==2){
		$(this).children('td:eq(4)').html("<button id=2 onclick=\"openshutport(this)\" type=\"button\" class=\"btn btn-danger btn-xs disabled\">关闭</button>");	
	}
	else{
		$(this).children('td:eq(4)').html("<button id=0 onclick=\"openshutport(this)\" type=\"button\" class=\"btn btn-success btn-xs\">开启</button>");	
	}
});

function isPort(str) {
	var parten = /^(\d)+$/g;
	if (parten.test(str) && parseInt(str) <= 65535 && parseInt(str) >= 0) {
		return true;
	} else {
		alert("请输入有效端口号!!");
	}
}
function search(arg) {
	var data = $('#searchport').val();
	if (isPort(data) == true) {
		location.href = '/port/'+data
	}
}
function addport(arg) {
	var ipaddr = $('#ipaddr').val();
	var wanport = $('#wanport').val();
	var lanport = $('#lanport').val();
	$.post("/addport/", { ipaddr: ipaddr, lanport: lanport,wanport:wanport },
			   function(arg){
		         if (arg=='000')
			     {$("#tip").html("<p style=\"color:green\" class=\"fa fa-check fa-1x\">更新成功</p>");
			     }
			     else
		         {$("#tip").html("<p style=\"color:red\" class=\"fa fa-times fa-1x\">"+" "+ arg+"</p>");}
			   });
}
function openshutport(arg) {
        var ip=$(arg).parent().parent().find("td").eq(0).text();
        var wanport=$(arg).parent().parent().find("td").eq(2).text();
        var action=$(arg).attr('id');
	$.post("/editport/", { ipaddr: ip, wanport: wanport,action:action},
			   function(arg1){
		         if (arg1=='close')
                             {
        $(arg).parent().html("<button id=0 onclick=\"openshutport(this)\" type=\"button\" class=\"btn btn-success btn-xs\">开启</button>");
        console.log($(arg).attr('id'));
			   }
		        else if  (arg1=='open')
                             {
        $(arg).parent().html("<button id=1 onclick=\"openshutport(this)\" type=\"button\" class=\"btn btn-danger btn-xs\">关闭</button>");
			   }
		      else
		         {alert('error');
                      window.location.reload();
                                   }
			   });
      /* $.ajax({
	 type: "POST",
	 url: "/editport/",
	 data: {ipaddr: ip, wanport: wanport,action:action},
	 dataType: "json",
	 success: function(data){
				 if (data=='close')
				 {
	$(arg).parent().html("<button onclick=\"openshutport(this)\" type=\"button\" class=\"btn btn-success btn-xs\">开启</button>");
	$(arg).parent().attr('statuscode','0');
				 }
				else if  (data=='open')
					{
	$(arg).parent().html("<button onclick=\"openshutport(this)\" type=\"button\" class=\"btn btn-danger btn-xs\">关闭</button>");
	$(arg).parent().attr('statuscode','1');
					}
				else
					 {alert('error');
				  window.location.reload();
							   }

			  }
 });*/
}
function editport(arg) {
    var data=$(arg).parent().parent().find("td").eq(3).text();
    var id=$(arg).parent().parent().find("td").eq(2).text();
    $('#usage').val(data);
    $('#myModalLabel-id').text(id);
}
function saveport(arg) {
	var data=$('#usage').val();
	var wanport=$('#myModalLabel-id').text();
	$.post("/portusage", { wan: wanport, usage: data },
			   function(arg){
		         if (arg=='ok')
			     {alert("更新成功!!");
			     location.reload();}
			     else
		         {alert("失败请重试!!");}
			   });
}
function syncport(){
        $("<div id='shade' style='opacity:0.55;background:white url(../../static/img/loading.gif) no-repeat;background-position:50% 50%; '></div>").css({
  position:'absolute',
  top:0,  
  left:0, 
  zIndex:300,
  height:'100%',
  width:'100%'
}).appendTo('#myshade');
	$.get("/syncport/",
			   function(arg){
		         if (arg=='ok')
			     {//alert("同步成功!!");
			     location.reload();}
			     else
		         {alert("失败请重试!!");}
			   });
}
