function editing(arg) {
    var id=$(arg).parent().parent().find("td");
    $('#usage').val(id.eq(1).text());
    var para={ns:id.eq(0).text(),host:id.eq(1).text(),ing_name:id.eq(2).text(),service_name:id.eq(3).text(),service_port:id.eq(4).text()}
    $('#myModalLabel-id').text(JSON.stringify(para))
}
function saveing(arg) {
	var data=$('#usage').val();
	var para=JSON.parse($('#myModalLabel-id').text());
	para.host=data
	$.post("/ingapi/",para,
			   function(arg){
		console.log(arg)
		         if (arg.indexOf('generation') != -1)
			     { alert("更新成功!!");
			location.reload();
                             }
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
location.reload();
}
