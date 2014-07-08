$(document).ready(ini);


function ini(){

	get_students_data();
}

function get_students_data () {

    var tok = $("#token").attr("value");
    var code_class = $("#code").attr("value");
    var query = $.ajax({
    url:"lista_cargar/",
    type:'POST',
    dataType:"json",
    data:{
          
          csrfmiddlewaretoken: tok,
          name:'name',
          last_name:'last_name',
          subject_name:'subject_name'

         

    }, 

    "success":function(data){
        create_table_students(data);
      }

    })
  
} /*cierro function get_students_data*/

function create_table_students() {


	//if(data['type'] == 'success'){  
    var output_thead = "";                                                 
    output_thead +="<tr>";
    output_thead +="<th>Nombre</th>";                                                   
    output_thead +="<th>Apellido</th>";
    output_thead +="<th>Meta cognitivo</th>";
    output_thead +="<th>Cognitivo</th>";
    output_thead +="<th>Socio afectivo</th>";

  /*  for (var s in data["dictionary_subjects"]){
        output_thead += "<th>";  
        output_thead += (data["dictionary_subjects"][e]['subject_name']); 
        output_thead += "</th>";
    }
    output_thead +="</tr>";*/
    
 
  var output = "";
  for (var x in data["dictionary_students"]){
      output += "<tr>";      
      (data["dictionary_students"][x]['name'] == "0") ? output += "<td></td>": output += "<td>"+data["dictionary_students"][x]['name']+"</td>";
      (data["dictionary_students"][x]['last_name'] == "0") ? output += "<td></td>": output += "<td>"+data["dictionary_students"][x]['last_name']+"</td>";
      

    output += "</tr>";
    }/*cierro for dictionary_students*/

   // if (output != ""){
      $("#dt_alumnos > tbody ").html(output);
      $("#dt_alumnos > thead").html(output_thead);
      $('#dt_alumnos').dataTable();
   // }

    

}/*CIERRO function create_table_students*/

/*for (var y in data["dictionary_students_exercises"]){
        if (data["dictionary_students"][x]['id_student'] == data["dictionary_students_exercises"][y]['student']  ) {
          
          (data["dictionary_students_exercises"][y]['points'] == '') ? output += "<td></td>": output += "<td>"+data["dictionary_students_exercises"][y]['points']+"</td>";
          }/*cierro if*/
       
       /* }cierro for dictionary_students_exercises*/