$(document).ready(ini);


function ini(){

	get_students_data();
}

function get_students_data () {

    var tok = $("#token").attr("value");
    var code = $("#code").attr("value");
    var query = $.ajax({
    url:"listas/"+code+"/lista_cargar/",
    type:'POST',
    dataType:"json",
    data:{
          
          csrfmiddlewaretoken: tok,
          name:'name',
          last_name:'last_name',
          subject_name:'subject_name',
          metacognitive:'metacognitive',
          cognitive:'cognitive',
          socio_affective:'socio_affective',
          subj:'subj',
          subject_id:'subject_id',
          average:'average'

    }, 

    "success":function(data){
        create_table_students(data);
      }

    })
  
} /*cierro function get_students_data*/

function create_table_students(data) {


	
    var output_thead = "";                                                 
    output_thead +="<tr>";
    output_thead +="<th>Nombre</th>";                                                   
    output_thead +="<th>Apellido</th>";
    output_thead +="<th>Meta cognitivo</th>";
    output_thead +="<th>Cognitivo</th>";
    output_thead +="<th>Socio afectivo</th>";

    for (var s in data["dictionary_subjects"]){
        output_thead += "<th>";  
        output_thead += (data["dictionary_subjects"][s]['subject_name']); 
        output_thead += "</th>";
    }
    output_thead +="</tr>";
   
 	
  var output = "";
  for (var x in data["dictionary_students"]){
      output += "<tr>";      
      (data["dictionary_students"][x]['name'] == "0") ? output += "<td></td>": output += "<td>"+data["dictionary_students"][x]['name']+"</td>";
      (data["dictionary_students"][x]['last_name'] == "0") ? output += "<td></td>": output += "<td>"+data["dictionary_students"][x]['last_name']+"</td>";
      for (var y in data["dictionary_students_profiles"]){
        if (data["dictionary_students"][x]['id_student'] == data["dictionary_students_profiles"][y]['student']  ) {        
           (data["dictionary_students_profiles"][y]['metacognitive'] == '') ? output += "<td></td>": output += "<td>"+data["dictionary_students_profiles"][y]['metacognitive']+"</td>";
           (data["dictionary_students_profiles"][y]['cognitive'] == '') ? output += "<td></td>": output += "<td>"+data["dictionary_students_profiles"][y]['cognitive']+"</td>";
           (data["dictionary_students_profiles"][y]['socio_affective'] == '') ? output += "<td></td>": output += "<td>"+data["dictionary_students_profiles"][y]['socio_affective']+"</td>";
          }/*cierro if*/
       
        }/*cierro for dictionary_students_profiles*/
      for (var sb in data["dictionary_subjects"]){
      	for (var sbj in data["dictionary_subjects_students_average"]){
      	if (data["dictionary_subjects"][sb]['subject_id'] == data["dictionary_subjects_students_average"][sbj]['subj']  ) {        
           (data["dictionary_students_profiles"][sbj]['average'] == '') ? output += "<td></td>": output += "<td>"+data["dictionary_students_profiles"][sbj]['average']+"</td>";
      }  /*cierro id*/
  		}/*cierro for */
}/*cierro for */
    output += "</tr>";
    }/*cierro for dictionary_students*/

    if (output != ""){
      $("#dt_students > tbody ").html(output);
      $("#dt_students > thead").html(output_thead);
      $('#dt_students').dataTable();
    }

    

}/*CIERRO function create_table_students*/
