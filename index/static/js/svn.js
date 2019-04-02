function addproject(arg) {
	var proname = $('#project').val();
	//alert (proname)
	$.post("/svnadd/", { proname:proname},
			   function(arg){
		         if (arg=='ok')
			     {$("#tip").html("<p style=\"color:green\" class=\"fa fa-check fa-1x\">更新成功</p>");
			     location.reload();}
			     else
		         {$("#tip").html("<p style=\"color:red\" class=\"fa fa-times fa-1x\">"+" "+ arg+"</p>");}
			   });
}
function adduser(arg) {
	var username = $.trim($('#user').val());
        var reg = /^[0-9a-zA-Z]+$/
        if(!reg.test(username)){
         alert("你输入的字符不是数字或者字母")
         }
         else{
	$.post("/svnadd/", { username:username },
			   function(arg){
		         if (arg=='ok')
			     {$("#tip").html("<p style=\"color:green\" class=\"fa fa-check fa-1x\">成功</p>");
			     location.reload();}
			     else
		         {$("#tip").html("<p style=\"color:red\" class=\"fa fa-times fa-1x\">"+" "+ arg+"</p>");}
			   });}
}
function addgroup(arg) {
	var groupname = $('#group').val();
	//alert(groupname)
	$.post("/svnadd/", { groupname:groupname },
			   function(arg){
		         if (arg=='ok')
			     {$("#tip").html("<p style=\"color:green\" class=\"fa fa-check fa-1x\">成功</p>");
			     location.reload();}
			     else
		         {$("#tip").html("<p style=\"color:red\" class=\"fa fa-times fa-1x\">"+" "+ arg+"</p>");}
			   });
}
function userchange(){
var checkText=$("#select_user").find("option:selected").text();
$("button#btnuser").removeAttr("style"); 
$("button#btnuser").html('所选用户为:'+checkText);
$.post("/svninfo/", { username:checkText},
		   function(arg){
    var jsondata = $.parseJSON(arg)
    if (arg=='[]')	
    	{$("#select_utogroup").empty();
    	$("#select_utogroup").append("<option>空</option>");}
    else{
    $("#select_utogroup").empty(); 
    $.each(jsondata,function(key,val){ 
 	   var data=val.fields.name
 	   $("#select_utogroup").append("<option>"+data+"</option>");
 	});}
	   });
}
function groupchange(){
	var checkText=$("#select_group").find("option:selected").text();
	$("button#btngroup").removeAttr("style"); 
	$("button#btngroup").html('所选用户组为:'+checkText);
}
function clickuser(){
	var checkText=$("#select_utogroup").find("option:selected").text();
	$("button#btngroup").removeAttr("style"); 
	$("button#btngroup").html('所选用户组为:'+checkText);
}
function groupchange1(){
	var checkText=$("#select_group1").find("option:selected").text();
	$("button#btngroup1").removeAttr("style");
	$("button#btngroup1").html('所选用户组为:'+checkText);
	$.post("/svninfo/", {groupname:checkText},
			   function(arg){
    var jsondata = $.parseJSON(arg)
    if (arg=='[]')	
    	{$("#select_gtopro").empty();	
    	$("#select_gtopro").append("<option>空</option>");}
    else{
    $("#select_gtopro").empty(); 
    $.each(jsondata,function(key,val){ 
 	   var data=val.fields.name
 	   $("#select_gtopro").append("<option>"+data+"</option>");
 	});}
			   });
}
function prochange(){
	var checkText=$("#select_pro").find("option:selected").text();
	$("button#btnproject").removeAttr("style");
	$("button#btnproject").html('所选项目为:'+checkText);
}
function clickpro(){
	var checkText=$("#select_gtopro").find("option:selected").text();
	$("button#btnproject").removeAttr("style");
	$("button#btnproject").html('所选项目为:'+checkText);
}
function addusertogroup(){
	var user=$("button#btnuser").html().split(':')[1];	
	var group=$("button#btngroup").html().split(':')[1];
	$.post("/svnutg/", { user:user,group:group },
			   function(arg){
		         if (arg=='ok')
			     {$("#tip").html("<p style=\"color:green\" class=\"fa fa-check fa-1x\">成功</p>");}
			     //location.reload();
			     else
		         {$("#tip").html("<p style=\"color:red\" class=\"fa fa-times fa-1x\">"+" "+ arg+"</p>");}
			   });
}
function deleteusertogroup(){
	var user=$("button#btnuser").html().split(':')[1];	
	var group=$("button#btngroup").html().split(':')[1];
	$.post("/svndutg/", { user:user,group:group },
			   function(arg){
		         if (arg=='ok')
			     {$("#tip").html("<p style=\"color:green\" class=\"fa fa-check fa-1x\">成功</p>");}
			     //location.reload();
			     else
		         {$("#tip").html("<p style=\"color:red\" class=\"fa fa-times fa-1x\">所选用户不属此用户组</p>");}
			   });
}
function usertolist(){
	var user=$("button#btnuser").html().split(':')[1];	
	$.post("/svndeluser/", {user:user},
			   function(arg){
		         if (arg=='ok')
			     {$("#tip").html("<p style=\"color:green\" class=\"fa fa-check fa-1x\">成功</p>");}
			     //location.reload();
			     else
		         {$("#tip").html("<p style=\"color:red\" class=\"fa fa-times fa-1x\">未知错误</p>");}
			   });
}
function addgrouptopro(){
	var group=$("button#btngroup1").html().split(':')[1];	
	var pro=$("button#btnproject").html().split(':')[1];
	$.post("/svngtp/", { group:group,pro:pro },
			   function(arg){
		         if (arg=='ok')
			     {$("#tip").html("<p style=\"color:green\" class=\"fa fa-check fa-1x\">成功</p>");}
			     //location.reload();
			     else
		         {$("#tip").html("<p style=\"color:red\" class=\"fa fa-times fa-1x\">所选用户不属此用户组</p>");}
			   });
}
function deletegrouptopro(){
	var group=$("button#btngroup1").html().split(':')[1];	
	var pro=$("button#btnproject").html().split(':')[1];
	$.post("/svndgtp/", { group:group,pro:pro },
			   function(arg){
		         if (arg=='ok')
			     {$("#tip").html("<p style=\"color:green\" class=\"fa fa-check fa-1x\">成功</p>");}
			     //location.reload();
			     else
		         {$("#tip").html("<p style=\"color:red\" class=\"fa fa-times fa-1x\">所选用户组不属此项目</p>");}
			   });
}

function syncsvn(){
        $("<div id='shade' style='opacity:0.55;background:white url(../../static/img/loading.gif) no-repeat;background-position:50% 50%; '></div>").css({ 
  position:'absolute', 
  top:0, 
  left:0, 
  zIndex:300,
  height:'100%',
  width:'100%'
}).appendTo('#myshade');
        $.get("/syncsvn/",
                           function(arg){
                         if (arg=='ok')
                             {
                             //alert("同步成功!!");
                             location.reload();
                             }
                             else
                         {alert("失败请重试!!");}
                           });
}
