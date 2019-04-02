var create_graph = function (hostid,monitortype,title) {
    var unit=(monitortype.indexOf('Percent')>0)?'%':'';
    var type=(monitortype.indexOf('Percent')<0&&monitortype.indexOf('Tcp')<0)?'area':'line';
    var common_options={
    	        lang:{ 
    	    	    loading:'正在加载...',
    	    	    noData:'暂无数据'
    	        }, 
                global:{useUTC:true },
    		   chart: {
    		            renderTo: 'graph',
    		            type: 'line'
    		         },	
    		         credits:{
    	    		     enabled:false // 禁用版权信息
    	    		},
    	    		title : {
    	                text : title
    	            },
    	            loading: {
    	                labelStyle: {
    	                    fontStyle: 'italic',
    	                    fontSize:'50px',
    	                    color: 'white'
    	                },
    	                style: {
    	                    backgroundColor: 'gray'
    	                }
    	            },
    	            yAxis: { 
    	            	labels: {
                        tickPixelInterval:10
    	                    /*formatter: function() {
    	                    	if (this.value>1024*1024*1024){
    	                    		 return parseInt(this.value/1024/1024/1024)+'G';
    	                    	}
    	                    	else if (this.value>1024*1024){
    	                    		 return parseInt(this.value/1024/1024)+'M'; 
    	                    	}
    	                    	else if (this.value>1024){
    	                   		     return parseInt(this.value/1024)+'K';	 
    	                   		}	 
    	                    	else {
    	                             return this.value+unit;
    	                        }
    	                    }*/
    	                }
    	            },
    	            tooltip:{
    	            	pointFormat: '{series.name}: <b>{point.y}</b><br/>'
    	            },
    	            series : [{
    	                name : monitortype,
    	                data : [],
    	                type: type,
    	                tooltip: {
    	                    valueDecimals: 2
    	                }
    	            }]            		  	
    	}
    var mychart = new Highcharts.stockChart(common_options)
    //mychart.showLoading();
    $.getJSON('/bcmdata/'+hostid+'/'+monitortype+'/', function (data) {
        var arrdata=[]
        for(var i in data)  
           {  
             arrdata.push([data[i][0]*1000+28800000+28800000,data[i][1]]);
             //arrdata.push([data[i][0]*1000,data[i][1]]);
             
           }
        //if (arrdata[0][1] !='null'){
    	mychart.series[0].setData(arrdata);
        //mychart.hideLoading();
    	//}
    });
}
create_graph('3c482490-32bb-4ff2-a673-08c65c7c7bd4','WebInBitsPerSecond','入口带宽');

function freshgraph(){
	data=$('#monitordetail').val();
	id=$('#hostip').val()
	title=$('#monitordetail').find("option:selected").text()
	if (id==null||data==null||title==null){
		create_graph('3c482490-32bb-4ff2-a673-08c65c7c7bd4','WebInBitsPerSecond','入口带宽');
	}
	else{create_graph(id,data,title)}
}
setInterval(freshgraph,60000);
