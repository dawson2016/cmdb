$("table tbody tr").each(function(){
	var status=$(this).children('td:eq(2)').text();
	var os=$(this).children('td:eq(3)').text();
	if (status=='Running'){
		$(this).children('td:eq(2)').html("<p style=\"color:green\" class=\"fa fa-check fa-1x\"></p>");	
	}
	else{
		$(this).children('td:eq(2)').html("<p style=\"color:red\" class=\"fa fa-times fa-1x\"></p>")
	}
	if (os=='linux'){
		$(this).children('td:eq(3)').html("<p class=\"fa fa-linux fa-1x\"> Linux</p>");	
	}
	else{
		$(this).children('td:eq(3)').html("<p class=\"fa fa-windows fa-1x\"> Windows</p>")
	}
});
function edit(arg) {
    var data=$(arg).parent().parent().find("td").eq(5).text();
    var id=$(arg).parent().parent().find("td").eq(0).text();
    $('#usage').val(data);
    $('#myModalLabel-id').text(id);
}
function save(arg) {
	var data=$('#usage').val();
	var hostid=$('#myModalLabel-id').text();
	$.post("/edit/", { id: hostid, usage: data },
			   function(arg){
		         if (arg=='ok')
			     {alert("更新成功!!");
			     location.reload();}
			     else
		         {alert("失败请重试!!");}
			   });
}

$("#ostype").change(function(){
	data=$('#ostype').val();
	if (data!="请选择"){
    $.ajax({
        url:"/hostselect",
        data:{ostype:data},
        type:"GET",
        dataType:"JSON",
        success:function(data){
          str="";
          for(var j in data)//js中的遍历数组用for来表示
          {
            str +="<option value='"+data[j][1]+"'>"+data[j][0]+"</option>";
          }
          $("#hostip").html(str);
        }
      })
	}
})
$("#monitordetail").change(function(){
	data=$('#monitordetail').val();
	title=$('#monitordetail').find("option:selected").text()
	id=$('#hostip').val()
	create_graph(id,data,title)
})
$("#hostip").change(function(){
	data=$('#monitordetail').val();
	id=$('#hostip').val()
	title=$('#monitordetail').find("option:selected").text()
	create_graph(id,data,title)
})
