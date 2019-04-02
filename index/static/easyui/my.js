function newUser(){
	$('#dlg').dialog('open').dialog('setTitle','新增主机');
	$('#fm').form('clear');
	url = 'add/';
}
function saveUser(){
	$('#fm').form('submit',{
		url:url,
		onSubmit: function(){
			return $(this).form('validate');
		},
		success: function(result){
			var result = eval('('+result+')');
			if (result.errorMsg){
				$.messager.show({
					title: 'Error',
					msg: result.errorMsg
				});
			} else {
				$('#dlg').dialog('close');		// close the dialog
				$('#dg').datagrid('reload');	// reload the user data
			}
		}
	});
}
function editUser(){
var row = $('#dg').datagrid('getSelected');	
if (row){
	$('#dlg').dialog('open').dialog('setTitle','编辑主机信息');
	$('#fm').form('load',row);
	url = 'edit?id='+row.id;
}	
}
function detailinfo(){
	var row = $('#dg').datagrid('getSelected');	
	if (row){
		window.open("hostinfo/"+row.instanceid);
	}	
	}
function destroyUser(){
	var row = $('#dg').datagrid('getSelected');
	if (row){
		$.messager.confirm('Confirm','确定要删除这台主机吗?',function(r){
			if (r){
				$.post('delete',{id:row.id},function(result){
					if (result=='1'){
						$('#dg').datagrid('reload');	// reload the user data
					} else {
						$.messager.show({	// show error message
							title: 'Error',
							msg: result.errorMsg
						});
					}
				},'json');
			}
		});
	}
}
