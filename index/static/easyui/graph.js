var create_graph = function (monitortype) {
    var unit=(monitortype.indexOf('Percent')>0)?'%':'';
    var type=(monitortype.indexOf('Percent')<0&&monitortype.indexOf('Tcp')<0)?'area':'line';
    var hostid=$("#hostid").text();
    var common_options={
    	        lang:{ 
    	    	    loading:'正在加载...',
    	    	    noData:'暂无数据'
    	        },    
    		   chart: {
    		            renderTo: 'testgraph',
    		            type: 'line'
    		         },	
    		         credits:{
    	    		     enabled:false // 禁用版权信息
    	    		},
    	    		title : {
    	                text : monitortype
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
    	                    formatter: function() {
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
    	                    }
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
    mychart.showLoading();
    $.getJSON('/bcmdata/'+hostid+'/'+monitortype, function (data) {
        var arrdata=[]
        for(var i in data)  
           {  
             arrdata.push([data[i][0]*1000+57600000,data[i][1]]);
           }
    	mychart.series[0].setData(arrdata);
        mychart.hideLoading();
    });
}
create_graph('CpuLoadAvg5');