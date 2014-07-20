$(document).ready(ini);


function ini(){

  $("#select_unit").attr('disabled','disabled');
  $("#select_subject").attr('disabled','disabled');
  
  $('#select_area').change(load_fiters);
  
}

function load_fiters(){
    var id_area = $(this).val();
    load_filter_subjects(id_area);
}

function load_filter_subjects(id_area){
	var cg = $('#code').val();
	var tok = $("#token").attr("value");
	var query = $.ajax({
    //url:"lista/A8o6/materias/",
	    url:"lista/"+cg+"/materias/",
	    type:'POST',
	    dataType:"json",
	    data:{
	        csrfmiddlewaretoken: tok,
	        state:'inactive',
	        id_area: id_area,
	        name: 'y.name',
	        id:'y.id',
	    },
	    "success":function(data){
			$('#select_subject').removeAttr('disabled');
			var output_select = "";
			output_select += '<option value="0" selected="" disabled="">Materia</option>'
			for (var y in data["dictionary_subjects"]){
				output_select += "<option value="+(data["dictionary_subjects"][y]['id'])+">";
				output_select += (data["dictionary_subjects"][y]['name']); 
				output_select += "</option>";
			}/*Cierro for dictionary_subjects*/
			$("#select_subject").html(output_select);
		}
	});
    $("#select_subject").change(load_units);
}

function load_units(){
	var cg = $('#code').val();
	var id_subject = $(this).val();
	var tok = $("#token").attr("value");  
	var query = $.ajax({
		url:"lista/"+cg+"/unidades/",
		type:'POST',
		dataType:"json",
		data:{
			csrfmiddlewaretoken: tok,
			state:'inactive',
			id_subject: id_subject,
			name: 'p.name',
			id:'p.id',
		},
		"success":function(data){
			$('#select_unit').removeAttr('disabled');
			var output_select_unit="";
			output_select_unit +='<option value="0" selected="" disabled="">Unidad</option>'
			for (var p in data["dictionary_units"]){
				output_select_unit += "<option value="+(data["dictionary_units"][p]['id'])+">";
				output_select_unit += (data["dictionary_units"][p]['name']); 
				output_select_unit += "</option>";
			}/*Cierro for dictionary_subjects*/
			$("#select_unit").html(output_select_unit);
		}
	});
	$('#select_unit').change(get_contents_data);
}/*cierro funcion load_units*/

function get_contents_data () {

    var code_class = $("#code").attr("value");
    var id_unit = $(this).val();
    var tok = $("#token").attr("value");
    var query = $.ajax({
    url:"contenidos/"+code_class+"/alumnos/",
    type:'post',
    dataType:"json",
    data:{
          csrfmiddlewaretoken: tok,
          state:'inactive',
          id_unit: id_unit,
          img:'img',
          exercise_id:'exercise_id',
          matriz:'matriz'

    }, 

    "success":function(data){
        create_table_students(data);
      }

    })
  
}