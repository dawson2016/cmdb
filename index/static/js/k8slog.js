function showlog(arg) {
    var id=$(arg).parent().parent().find("td");
    var line=$(arg).parent().find("#logline").val();
    var para={ns:id.eq(0).text(),pod:id.eq(1).text(),lines:line}
 $('#showdiv').show();  //显示弹窗
    $('#cover').css('display','block'); //显示遮罩层
    $('#cover').css('height',document.body.clientHeight+'px'); //设置遮罩层
$("#k8slog").empty();
 $.ajax({
            type:'get',
            url:"/k8slogapi/",
            async:true,
            data:para,
            success:function (strs) {　　　　　　
     $("#k8slog").append(strs+'</br>');
            },
            error:function (e) {
alert('参数错误,请刷新页面重试!')
closelog();
            }
        });
var para1={ns:id.eq(0).text(),pod:id.eq(1).text(),times:10}
var count=0
function rtlog(){
$.get("/k8slogapi/", para1 ,function(strs){
    count++;
if (count>100){ clearInterval(myrtlog);alert('已超时,请刷新页面重新获取日志')}
    $("#k8slog").append(strs+'</br>')}
)
}
myrtlog=setInterval(rtlog,10000)
}
function closelog(){
  $('#showdiv').hide();
  $('#cover').css('display','none');
  clearInterval(myrtlog);
}
function downlog(arg){
var id=$(arg).parent().parent().find("td");
var para={ns:id.eq(0).text(),pod:id.eq(1).text()}
var url = '/k8slogdown/?ns='+id.eq(0).text()+'&pod='+id.eq(1).text();
var xhr = new XMLHttpRequest();
xhr.open('GET', url, true); 
xhr.responseType = "blob"; 
xhr.onload = function () {
if (this.status === 200) {
var blob = this.response;
var reader = new FileReader();
reader.readAsDataURL(blob);
reader.onload = function (e) {
        var a = document.createElement('a');
        a.download = id.eq(0).text()+'-'+id.eq(1).text()+'-log.txt';
        a.href = e.target.result;
        $("body").append(a);
        a.click();
        $(a).remove();
      }
    }
else {alert('未知错误,请刷新页面重试!')}
  };
  xhr.send()
}
function syncapp(){
        $("<div id='shade' style='opacity:0.55;background:white url(../../static/img/loading.gif) no-repeat;background-position:50% 50%; '></div>").css({
  position:'absolute',
  top:0,
  left:0,
  zIndex:500,
  height:'100%',
  width:'100%'
}).appendTo('#myshade');
location.reload();
}
