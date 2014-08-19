$(document).ready(ini);


function ini(){
	$("#user").on('blur',validar);
}

function validar(){
	var tok = $("#token").attr("value");
	var user = $("#user").val();
	
	var query = $.ajax({
		url:"validacion/",
		type:'POST',
		dataType:'json',
		data:{
			csrfmiddlewaretoken: tok,
        	state:'inactive',
        	user:user,
		},
		"success":function(data){
			alert('entre al  success');
			var output = '';
			if (data["exist_user"]){
				output+="<p style='color:#f00;'>Ya existe usuario</p>"
			}
			else{
				output+="";
			}
			$("#user_msg").html(output);
		}
	});
}